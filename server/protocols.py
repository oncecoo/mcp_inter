from pydantic import BaseModel, Field
from typing import List


class WeatherRequest(BaseModel):
    location: str


class WeatherResponse(BaseModel):
    location: str = Field(description="城市名称")
    temperature: float = Field(description="温度")
    condition: str = Field(description="天气状况")
    humidity: float = Field(description="湿度")


class SearchRequest(BaseModel):
    query: str = Field(description="搜索关键词")


class SearchResponse(BaseModel):
    query: str = Field(description="搜索关键词")
    title: str = Field(description="标题信息")
    summary: str = Field(description="摘要信息")


