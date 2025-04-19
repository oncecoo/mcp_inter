import uvicorn

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from mcp.server.sse import SseServerTransport
from starlette.requests import Request
from starlette.routing import Mount, Route
from mcp.server import Server

from protocols import WeatherRequest, WeatherResponse, SearchRequest, SearchResponse
from models import get_weather, search

load_dotenv()

mcp = FastMCP("docs")

USER_AGENT = "docs-app/1.0"

# docs_urls = {
#     "langchain": "python.langchain.com/docs",
#     "llama-index": "docs.llamaindex.ai/en/stable",
#     "autogen": "microsoft.github.io/autogen/stable",
#     "agno": "docs.agno.com",
#     "openai-agents-sdk": "openai.github.io/openai-agents-python",
#     "mcp-doc": "modelcontextprotocol.io",
#     "camel-ai": "docs.camel-ai.org",
#     "crew-ai": "docs.crewai.com"
# }


@mcp.tool()
async def get_weather(query: WeatherRequest) -> WeatherResponse:
    """
    搜索指定地點的氣象信息。

    参数:
        query: 要查看的地方 (例如 "beijing")

    返回:
     天氣詳情
    """
    result = await get_weather(query)
    return result


@mcp.tool()
async def searcher(query: SearchRequest) -> SearchResponse:
    """
    搜索给定查询和库的最新文档。

    参数:
    query: 要搜索的查询 (例如 "React Agent")
    library: 要搜索的库 (例如 "agno")

    返回:
    文档中的文本
    """
    result = await search(query)
    return result

## sse传输
def create_starlette_app(mcp_server: Server, *, debug: bool = False) -> Starlette:
    """Create a Starlette application that can serve the provided mcp server with SSE."""
    sse = SseServerTransport("/messages/")

    async def handle_sse(request: Request) -> None:
        async with sse.connect_sse(
                request.scope,
                request.receive,
                request._send,  # noqa: SLF001
        ) as (read_stream, write_stream):
            await mcp_server.run(
                read_stream,
                write_stream,
                mcp_server.create_initialization_options(),
            )

    return Starlette(
        debug=debug,
        routes=[
            Route("/sse", endpoint=handle_sse),
            Mount("/messages/", app=sse.handle_post_message),
        ],
    )

if __name__ == "__main__":
    mcp_server = mcp._mcp_server

    import argparse

    parser = argparse.ArgumentParser(description='Run MCP SSE-based server')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to')
    parser.add_argument('--port', type=int, default=8020, help='Port to listen on')
    args = parser.parse_args()

    # Bind SSE request handling to MCP server
    starlette_app = create_starlette_app(mcp_server, debug=True)

    uvicorn.run(starlette_app, host=args.host, port=args.port)