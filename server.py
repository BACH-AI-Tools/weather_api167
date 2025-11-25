"""
Weather Api167 MCP Server

使用 FastMCP 的 from_openapi 方法自动生成

Version: 1.0.0
Transport: stdio
"""
import os
import json
import httpx
from fastmcp import FastMCP

# 服务器版本和配置
__version__ = "1.0.0"
__tag__ = "weather_api167/1.0.0"

# API 配置
API_KEY = os.getenv("API_KEY", "")

# 传输协议配置
TRANSPORT = "stdio"


# OpenAPI 规范
OPENAPI_SPEC = """{\n  \"openapi\": \"3.0.0\",\n  \"info\": {\n    \"title\": \"Weather Api167\",\n    \"version\": \"1.0.0\",\n    \"description\": \"RapidAPI: maruf111/weather-api167\"\n  },\n  \"servers\": [\n    {\n      \"url\": \"https://weather-api167.p.rapidapi.com\"\n    }\n  ],\n  \"paths\": {\n    \"/api/weather/forecast\": {\n      \"get\": {\n        \"summary\": \"forecast weather\",\n        \"description\": \"Fetch forecast weather data using  coordinate value, place name or zip code\",\n        \"operationId\": \"forecast_weather\",\n        \"parameters\": [\n          {\n            \"name\": \"lon\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Longitude coordinate(Note. lat and lon value has priority over both place and zip value). use the lat and lon for more accurate and reliable weather data\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"0\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"lat\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Latitude coordinate(Note. lat and lon value has priority over both place and zip value). use the lat and lon for more accurate and reliable weather data\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"0\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"place\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"City name, state code (only for the US) and country code divided by comma like Zion,VA,US . Please use ISO 3166 country codes. Note. place value has priority over zip value\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"zip\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Zip code with optional country code(Note. Zip value will only be used if both lat,lon and place name not provided)\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"cnt\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Number of timestamps to retrieve (up to a maximum allowed by the API)\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"units\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Unit type (standard, metric, and imperial)\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"type\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Forcast Type\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"mode\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Mode type\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"lang\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Language type\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/weather/country/detail\": {\n      \"get\": {\n        \"summary\": \"country info\",\n        \"description\": \"Return detail for given country\",\n        \"operationId\": \"country_info\",\n        \"parameters\": [\n          {\n            \"name\": \"country\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: United Kingdom\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/weather/us/alert\": {\n      \"get\": {\n        \"summary\": \"US weather alert data\",\n        \"description\": \"US weather alert daily information for given region or area and other filtering parameter\",\n        \"operationId\": \"us_weather_alert_data\",\n        \"parameters\": [\n          {\n            \"name\": \"status\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"use comm(,) to separate multiple value\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"message_type\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: alert,update,cancel\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"area\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"example AM,AN\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"region\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: AL,AT\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"zone\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example>> OKZ929\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"region_type\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example>> marine,land This value can't be used in combination with area or region\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"urgency\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: Immediate,Expected\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"severity\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: Extreme,Severe,Moderate\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"certainty\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: Observed,Likely,Possible,Unlikely,Unknown\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"limit\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: 500\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/weather/us/zone\": {\n      \"get\": {\n        \"summary\": \"US Zone List\",\n        \"description\": \"Zone list for US given state or All Zone list if state not given\",\n        \"operationId\": \"us_zone_list\",\n        \"parameters\": [\n          {\n            \"name\": \"state\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: WY\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/weather/earthquake\": {\n      \"get\": {\n        \"summary\": \"earthquake data\",\n        \"description\": \"Near real time earthquake for given country\",\n        \"operationId\": \"earthquake_data\",\n        \"parameters\": [\n          {\n            \"name\": \"country\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: US\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"startDate\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: \",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"endDate\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: \",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/weather/current\": {\n      \"get\": {\n        \"summary\": \"current weather\",\n        \"description\": \"Fetch current weather data using  coordinate value, place name or zip code\",\n        \"operationId\": \"current_weather\",\n        \"parameters\": [\n          {\n            \"name\": \"lon\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Longitude coordinate(Note. lat and lon value has priority over both place and zip value). use the lat and lon for more accurate and reliable weather data\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"0\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"lat\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Latitude coordinate(Note. lat and lon value has priority over both place and zip value). use the lat and lon for more accurate and reliable weather data\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"0\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"place\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"City name, state code (only for the US) and country code divided by comma use like Zion,VA,US . Please use ISO 3166 country codes. Note. place value has priority over zip value\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"zip\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Zip code with optional country code(Note. Zip value will only be used if both lat,lon and place name not provided)\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"units\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Unit type (standard, metric, and imperial)\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"lang\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Language type\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"mode\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Mode type\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/weather/air_pollution\": {\n      \"get\": {\n        \"summary\": \"air pollution data\",\n        \"description\": \"Fetch air pollution data using  coordinate value, place name or zip code\",\n        \"operationId\": \"air_pollution_data\",\n        \"parameters\": [\n          {\n            \"name\": \"lat\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Latitude coordinate(Note. lat and lon value has priority over both place and zip value). use the lat and lon for more accurate and reliable weather data\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"0\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"lon\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Longitude coordinate(Note. lat and lon value has priority over both place and zip value). use the lat and lon for more accurate and reliable weather data\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"0\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"place\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"City name, state code (only for the US) and country code divided by comma like Zion,VA,US . Please use ISO 3166 country codes Note. place value has priority over zip value\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"zip\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Zip code with optional country code(Note. Zip value will only be used if both lat,lon and place name not provided)\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"type\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Data for air pulltion type\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    }\n  },\n  \"components\": {\n    \"securitySchemes\": {\n      \"ApiAuth\": {\n        \"type\": \"apiKey\",\n        \"in\": \"header\",\n        \"name\": \"X-RapidAPI-Key\"\n      }\n    }\n  },\n  \"security\": [\n    {\n      \"ApiAuth\": []\n    }\n  ]\n}"""

# 创建 HTTP 客户端
# 设置默认 headers
default_headers = {}


# RapidAPI 必需的 headers
if API_KEY:
    default_headers["X-RapidAPI-Key"] = API_KEY
    default_headers["X-RapidAPI-Host"] = "weather-api167.p.rapidapi.com"
else:
    print("⚠️  警告: 未设置 API_KEY 环境变量")
    print("   RapidAPI 需要 API Key 才能正常工作")
    print("   请设置: export API_KEY=你的RapidAPI-Key")

# 对于 POST/PUT/PATCH 请求，自动添加 Content-Type
default_headers["Content-Type"] = "application/json"




client = httpx.AsyncClient(
    base_url="https://weather-api167.p.rapidapi.com", 
    timeout=30.0
)


# 从 OpenAPI 规范创建 FastMCP 服务器
openapi_dict = json.loads(OPENAPI_SPEC)
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
        print("⚠️  警告: API_KEY 未设置，请求可能失败")
    
    # 对于 POST/PUT/PATCH，添加 Content-Type
    if method.upper() in ['POST', 'PUT', 'PATCH']:
        if 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'
    
    return await _original_request(method, url, **kwargs)

# 替换 request 方法
client.request = _add_rapidapi_headers


def main():
    """主入口点"""
    print(f"🚀 启动 Weather Api167 MCP 服务器")
    print(f"📦 版本: {__tag__}")
    print(f"🔧 传输协议: {TRANSPORT}")
    
    print()
    
    # 运行服务器
    
    mcp.run(transport="stdio")
    


if __name__ == "__main__":
    main()