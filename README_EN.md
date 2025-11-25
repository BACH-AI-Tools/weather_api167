# Weather Api167 MCP Server

English | [简体中文](./README.md) | [繁體中文](./README_ZH-TW.md)

## 🚀 Quick Start with EMCP Platform

**[EMCP](https://sit-emcp.kaleido.guru)** is a powerful MCP server management platform that allows you to quickly use various MCP servers without manual configuration!

### Quick Start:

1. 🌐 Visit **[EMCP Platform](https://sit-emcp.kaleido.guru)**
2. 📝 Register and login
3. 🎯 Go to **MCP Marketplace** to browse all available MCP servers
4. 🔍 Search or find this server (`bach-weather_api167`)
5. 🎉 Click the **"Install MCP"** button
6. ✅ Done! You can now use it in your applications

### EMCP Platform Advantages:

- ✨ **Zero Configuration**: No need to manually edit config files
- 🎨 **Visual Management**: Easy-to-use GUI for managing all MCP servers
- 🔐 **Secure & Reliable**: Centralized API key and authentication management
- 🚀 **One-Click Install**: Rich selection of servers in MCP Marketplace
- 📊 **Usage Statistics**: Real-time service call monitoring

Visit **[EMCP Platform](https://sit-emcp.kaleido.guru)** now to start your MCP journey!


---

## Introduction

This is an automatically generated MCP server using [FastMCP](https://fastmcp.wiki) for accessing the Weather Api167 API.

- **PyPI Package**: `bach-weather_api167`
- **Version**: 1.0.0
- **Transport Protocol**: stdio


## 安装

### 从 PyPI 安装:

```bash
pip install bach-weather_api167
```

### 从源码安装:

```bash
pip install -e .
```

## 运行

### 方式 1: 使用 uvx（推荐，无需安装）

```bash
# 运行（uvx 会自动安装并运行）
uvx --from bach-weather_api167 bach_weather_api167

# 或指定版本
uvx --from bach-weather_api167@latest bach_weather_api167
```

### 方式 2: 直接运行（开发模式）

```bash
python server.py
```

### 方式 3: 安装后作为命令运行

```bash
# 安装
pip install bach-weather_api167

# 运行（命令名使用下划线）
bach_weather_api167
```

## Configuration

### API Authentication

This API requires authentication. Please set environment variable:

```bash
export API_KEY="your_api_key_here"
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_KEY` | API Key | Yes |
| `PORT` | N/A | No |
| `HOST` | N/A | No |



### 在 Claude Desktop 中使用

编辑 Claude Desktop 配置文件 `claude_desktop_config.json`:


```json
{
  "mcpServers": {
    "weather_api167": {
      "command": "python",
      "args": ["E:\path\to\weather_api167\server.py"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Note**: Replace `E:\path\to\weather_api167\server.py` with the actual server file path.


## 可用工具

此服务器提供以下工具:


### `forecast_weather`

Fetch forecast weather data using  coordinate value, place name or zip code

**端点**: `GET /api/weather/forecast`


**参数**:

- `lon` (string): Longitude coordinate(Note. lat and lon value has priority over both place and zip value). use the lat and lon for more accurate and reliable weather data

- `lat` (string): Latitude coordinate(Note. lat and lon value has priority over both place and zip value). use the lat and lon for more accurate and reliable weather data

- `place` (string): City name, state code (only for the US) and country code divided by comma like Zion,VA,US . Please use ISO 3166 country codes. Note. place value has priority over zip value

- `zip` (string): Zip code with optional country code(Note. Zip value will only be used if both lat,lon and place name not provided)

- `cnt` (string): Number of timestamps to retrieve (up to a maximum allowed by the API)

- `units` (string): Unit type (standard, metric, and imperial)

- `type` (string): Forcast Type

- `mode` (string): Mode type

- `lang` (string): Language type



---


### `country_info`

Return detail for given country

**端点**: `GET /api/weather/country/detail`


**参数**:

- `country` (string): Example value: United Kingdom



---


### `us_weather_alert_data`

US weather alert daily information for given region or area and other filtering parameter

**端点**: `GET /api/weather/us/alert`


**参数**:

- `status` (string): use comm(,) to separate multiple value

- `message_type` (string): Example value: alert,update,cancel

- `area` (string): example AM,AN

- `region` (string): Example value: AL,AT

- `zone` (string): Example>> OKZ929

- `region_type` (string): Example>> marine,land This value can't be used in combination with area or region

- `urgency` (string): Example value: Immediate,Expected

- `severity` (string): Example value: Extreme,Severe,Moderate

- `certainty` (string): Example value: Observed,Likely,Possible,Unlikely,Unknown

- `limit` (string): Example value: 500



---


### `us_zone_list`

Zone list for US given state or All Zone list if state not given

**端点**: `GET /api/weather/us/zone`


**参数**:

- `state` (string): Example value: WY



---


### `earthquake_data`

Near real time earthquake for given country

**端点**: `GET /api/weather/earthquake`


**参数**:

- `country` (string): Example value: US

- `startDate` (string): Example value: 

- `endDate` (string): Example value: 



---


### `current_weather`

Fetch current weather data using  coordinate value, place name or zip code

**端点**: `GET /api/weather/current`


**参数**:

- `lon` (string): Longitude coordinate(Note. lat and lon value has priority over both place and zip value). use the lat and lon for more accurate and reliable weather data

- `lat` (string): Latitude coordinate(Note. lat and lon value has priority over both place and zip value). use the lat and lon for more accurate and reliable weather data

- `place` (string): City name, state code (only for the US) and country code divided by comma use like Zion,VA,US . Please use ISO 3166 country codes. Note. place value has priority over zip value

- `zip` (string): Zip code with optional country code(Note. Zip value will only be used if both lat,lon and place name not provided)

- `units` (string): Unit type (standard, metric, and imperial)

- `lang` (string): Language type

- `mode` (string): Mode type



---


### `air_pollution_data`

Fetch air pollution data using  coordinate value, place name or zip code

**端点**: `GET /api/weather/air_pollution`


**参数**:

- `lat` (string): Latitude coordinate(Note. lat and lon value has priority over both place and zip value). use the lat and lon for more accurate and reliable weather data

- `lon` (string): Longitude coordinate(Note. lat and lon value has priority over both place and zip value). use the lat and lon for more accurate and reliable weather data

- `place` (string): City name, state code (only for the US) and country code divided by comma like Zion,VA,US . Please use ISO 3166 country codes Note. place value has priority over zip value

- `zip` (string): Zip code with optional country code(Note. Zip value will only be used if both lat,lon and place name not provided)

- `type` (string): Data for air pulltion type



---



## 技术栈

- **FastMCP**: 快速、Pythonic 的 MCP 服务器框架
- **传输协议**: stdio
- **HTTP 客户端**: httpx

## 开发

This server is automatically generated by [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) tool.

Version: 1.0.0
