# Weather Api167 MCP Server

[English](./README_EN.md) | 简体中文 | [繁體中文](./README_ZH-TW.md)

## 🚀 使用 EMCP 平台快速体验

**[EMCP](https://sit-emcp.kaleido.guru)** 是一个强大的 MCP 服务器管理平台，让您无需手动配置即可快速使用各种 MCP 服务器！

### 快速开始：

1. 🌐 访问 **[EMCP 平台](https://sit-emcp.kaleido.guru)**
2. 📝 注册并登录账号
3. 🎯 进入 **MCP 广场**，浏览所有可用的 MCP 服务器
4. 🔍 搜索或找到本服务器（`bach-weather_api167`）
5. 🎉 点击 **"安装 MCP"** 按钮
6. ✅ 完成！即可在您的应用中使用

### EMCP 平台优势：

- ✨ **零配置**：无需手动编辑配置文件
- 🎨 **可视化管理**：图形界面轻松管理所有 MCP 服务器
- 🔐 **安全可靠**：统一管理 API 密钥和认证信息
- 🚀 **一键安装**：MCP 广场提供丰富的服务器选择
- 📊 **使用统计**：实时查看服务调用情况

立即访问 **[EMCP 平台](https://sit-emcp.kaleido.guru)** 开始您的 MCP 之旅！


---

## 简介

这是一个 MCP 服务器，用于访问 Weather Api167 API。

- **PyPI 包名**: `bach-weather_api167`
- **版本**: 2.0.0
- **传输协议**: stdio


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

## 配置

### API 认证

此 API 需要认证。请设置环境变量:

```bash
export API_KEY="your_api_key_here"
```

### 环境变量

| 变量名 | 说明 | 必需 |
|--------|------|------|
| `API_KEY` | API 密钥 | 是 |
| `PORT` | 不适用 | 否 |
| `HOST` | 不适用 | 否 |



### 在 Claude Desktop 中使用

编辑 Claude Desktop 配置文件 `claude_desktop_config.json`:


```json
{
  "mcpServers": {
    "weather_api167": {
      "command": "uvx",
      "args": ["--from", "bach-weather_api167", "bach_weather_api167"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**注意**: 请将 `E:\path\to\weather_api167\server.py` 替换为实际的服务器文件路径。


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

- **传输协议**: stdio
- **HTTP 客户端**: httpx

## 开发

此服务器由 [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) 工具自动生成。

版本: 2.0.0
