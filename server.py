"""
Weather Api167 MCP Server

MCP server for accessing API.

Version: 1.0.0
Transport: stdio
"""
import os
import json
from pathlib import Path
import httpx
from fastmcp import FastMCP

# 服务器版本和配置
__version__ = "2.1.0"
__tag__ = "weather_api167/2.1.0"

# API 配置
API_KEY = os.getenv("API_KEY", "")

# 传输协议配置
TRANSPORT = "stdio"


# 从文件加载 OpenAPI 规范
def load_openapi_spec():
    """从 openapi.json 文件加载 OpenAPI 规范"""
    openapi_path = Path(__file__).parent / "openapi.json"
    with open(openapi_path, "r", encoding="utf-8") as f:
        return json.load(f)

# 创建 HTTP 客户端
# 设置默认 headers
default_headers = {}


# RapidAPI 必需的 headers
if API_KEY:
    default_headers["X-RapidAPI-Key"] = API_KEY
    default_headers["X-RapidAPI-Host"] = "weather-api167.p.rapidapi.com"
else:
    print("[WARNING] 未设置 API_KEY 环境变量")
    print("          RapidAPI 需要 API Key 才能正常工作")
    print("          请设置: export API_KEY=你的RapidAPI-Key")

# 对于 POST/PUT/PATCH 请求，自动添加 Content-Type
default_headers["Content-Type"] = "application/json"




client = httpx.AsyncClient(
    base_url="https://weather-api167.p.rapidapi.com", 
    timeout=30.0
)


# 从 OpenAPI 规范创建 FastMCP 服务器
openapi_dict = load_openapi_spec()
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_dict,
    client=client,
    name="weather_api167",
    version=__version__
)


# 注册请求拦截器，为所有请求添加 RapidAPI headers
_original_request = client.request

async def _add_rapidapi_headers(method, url, **kwargs):
    """拦截所有请求，添加必需的 RapidAPI headers"""
    # 确保 headers 存在
    if 'headers' not in kwargs:
        kwargs['headers'] = {}
    
    # 添加 RapidAPI 必需的 headers
    if API_KEY:
        kwargs['headers']['X-RapidAPI-Key'] = API_KEY
        kwargs['headers']['X-RapidAPI-Host'] = "weather-api167.p.rapidapi.com"
    else:
        print("[WARNING] API_KEY 未设置，请求可能失败")
    
    # 对于 POST/PUT/PATCH，添加 Content-Type
    if method.upper() in ['POST', 'PUT', 'PATCH']:
        if 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'
    
    return await _original_request(method, url, **kwargs)

# 替换 request 方法
client.request = _add_rapidapi_headers


def main():
    """主入口点"""
    print(f"[START] Weather Api167 MCP Server")
    print(f"[VERSION] {__tag__}")
    print(f"[TRANSPORT] {TRANSPORT}")
    
    print()
    
    # 运行服务器
    
    mcp.run(transport="stdio")
    


if __name__ == "__main__":
    main()