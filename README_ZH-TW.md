# Weather Api167 MCP Server

[English](./README_EN.md) | [简体中文](./README.md) | 繁體中文

## 🚀 使用 EMCP 平台快速體驗

**[EMCP](https://sit-emcp.kaleido.guru)** 是一個強大的 MCP 伺服器管理平台，讓您無需手動配置即可快速使用各種 MCP 伺服器！

### 快速開始：

1. 🌐 造訪 **[EMCP 平台](https://sit-emcp.kaleido.guru)**
2. 📝 註冊並登入帳號
3. 🎯 進入 **MCP 廣場**，瀏覽所有可用的 MCP 伺服器
4. 🔍 搜尋或找到本伺服器（`bach-weather_api167`）
5. 🎉 點擊 **「安裝 MCP」** 按鈕
6. ✅ 完成！即可在您的應用中使用

### EMCP 平台優勢：

- ✨ **零配置**：無需手動編輯配置檔案
- 🎨 **視覺化管理**：圖形介面輕鬆管理所有 MCP 伺服器
- 🔐 **安全可靠**：統一管理 API 金鑰和認證資訊
- 🚀 **一鍵安裝**：MCP 廣場提供豐富的伺服器選擇
- 📊 **使用統計**：即時查看服務調用情況

立即造訪 **[EMCP 平台](https://sit-emcp.kaleido.guru)** 開始您的 MCP 之旅！


---

## 簡介

這是一個 MCP 伺服器，用於存取 Weather Api167 API。

- **PyPI 套件名**: `bach-weather_api167`
- **版本**: 1.0.0
- **傳輸協定**: stdio


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

### API 認證

此 API 需要認證。請設定環境變數:

```bash
export API_KEY="your_api_key_here"
```

### 環境變數

| 變數名 | 說明 | 必需 |
|--------|------|------|
| `API_KEY` | API 金鑰 | 是 |
| `PORT` | 不適用 | 否 |
| `HOST` | 不適用 | 否 |



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

**注意**: 請將 `E:\path\to\weather_api167\server.py` 替換為實際的伺服器檔案路徑。


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

此伺服器由 [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) 工具自動生成。

版本: 1.0.0
