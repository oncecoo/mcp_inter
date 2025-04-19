# FastAPI MCP服务器

这是一个使用FastAPI实现的MCP（Multi-Component Protocol）服务器，集成了几个常用的工具函数，包括天气查询、信息搜索和数学计算。

## 功能特点

- RESTful API设计
- 集成了三个常用工具函数
  - 天气查询
  - 信息搜索
  - 数学计算
- 自动生成API文档
- 请求和响应验证
- 错误处理

## 安装

### 环境要求
- Python 3.7+

### 安装步骤

1. 克隆此仓库
2. 安装依赖项:

```bash
cd server
pip install -r requirements.txt
```

## 运行服务器

```bash
cd server
python fastapi_mcp_server.py
```

或者使用uvicorn直接运行:

```bash
cd server
uvicorn fastapi_mcp_server:app --reload
```

服务器默认在 http://localhost:8000 上运行。

## API文档

启动服务器后，可以通过以下URL访问自动生成的交互式API文档:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API端点

### 基础端点
- `GET /`: 返回欢迎信息

### 物品管理
- `GET /items/{item_id}`: 获取指定ID的物品
- `POST /items/`: 创建新物品
- `GET /items/`: 列出所有物品

### 工具函数
- `POST /tools/weather`: 获取天气信息
- `POST /tools/search`: 搜索信息
- `POST /tools/calculate`: 计算数学表达式

## 示例请求

### 获取天气信息

```bash
curl -X 'POST' \
  'http://localhost:8000/tools/weather' \
  -H 'Content-Type: application/json' \
  -d '{"location": "北京"}'
```

### 搜索信息

```bash
curl -X 'POST' \
  'http://localhost:8000/tools/search' \
  -H 'Content-Type: application/json' \
  -d '{"query": "人工智能"}'
```

### 计算表达式

```bash
curl -X 'POST' \
  'http://localhost:8000/tools/calculate' \
  -H 'Content-Type: application/json' \
  -d '{"expression": "(2 + 3) * 4"}'
```

## 在代码中使用工具函数

除了通过API调用外，您还可以在Python代码中直接使用这些工具函数:

```python
from fastapi_mcp_server import get_weather, search_info, calculate

# 获取天气
weather = get_weather("北京")
print(weather)

# 搜索信息
info = search_info("人工智能")
print(info)

# 计算表达式
result = calculate("(2 + 3) * 4")
print(result)
```