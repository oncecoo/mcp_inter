import uvicorn

from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from loguru import logger
from models import get_weather, search
from protocols import WeatherRequest, WeatherResponse, SearchRequest, SearchResponse


app = FastAPI(title="fastapi_mcp_server测试案例")

mcp = FastApiMCP(
    app,
    name="Item API MCP",
    description="MCP server for the Item API",
    base_url="http://localhost:8000",
)

mcp.mount()


@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/weather")
async def weather(request: WeatherRequest) -> WeatherResponse:
    return get_weather(request)


@app.get("/search")
async def search(request: SearchRequest) -> SearchResponse:
    return search(request)


mcp.setup_server()  # 相当于update，更新mcp的配置


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)