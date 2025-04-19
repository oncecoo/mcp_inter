from protocols import WeatherRequest, WeatherResponse, SearchRequest, SearchResponse 


async def get_weather(request: WeatherRequest) -> WeatherResponse:
    """获取天气信息"""
    return WeatherResponse(
        location=request.location,
        temperature=20, 
        condition="晴",
        humidity=50)


async def search(request: SearchRequest) -> SearchResponse:
    """搜索信息"""
    return SearchResponse(
        query=request.query, 
        title=f"关于{request.query}的标题信息", 
        summary=f"关于{request.query}的摘要信息"
    )