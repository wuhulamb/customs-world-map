# 世界贸易伙伴地图

将海关贸易数据（country-iso.csv）匹配到世界行政区划边界上，生成一个可通过浏览器直接打开的交互式世界地图。

## 文件说明

| 文件 | 说明 |
|------|------|
| `country-iso.csv` | 海关贸易数据，272 条记录，含 贸易伙伴名称 / 贸易伙伴编码 / ISO_A3 |
| [`World_Bank_Official_Boundaries_Admin_0.geojson`](https://datacatalog.worldbank.org/search/dataset/0038272/world-bank-official-boundaries) | 世界银行国界数据，164 MB，264 个国家（原始数据） |
| `world.topo.json` | 经 mapshaper 简化（10%）后转换为 TopoJSON 格式，3.4 MB |
| `world_data.js` | 生成的地理数据（`generate_map.py` 输出），3.4 MB |
| `index.html` | **最终成品**，浏览器可直接打开 |
| `generate_map.py` | 数据生成脚本：将 CSV 数据合并到 TopoJSON，输出 `world_data.js` |

## 数据匹配方式

通过 `ISO_A3` 字段关联：

- CSV 260 条记录（有 ISO_A3 的）
- TopoJSON 264 个几何体
- **263/264 匹配成功**（仅 Kosovo `XKX` 无 CSV 对应数据）

## 使用方法

无需任何服务器和网络，直接用浏览器打开：

```bash
open index.html   # macOS
start index.html  # Windows
xdg-open index.html  # Linux
```

### 交互方式

- **搜索框** — 输入中文名称、英文名称或贸易伙伴编码，下拉提示并定位高亮
- **鼠标悬停** — 显示国家名称英文、国家名称中文、中国海关贸易伙伴编码
- **鼠标点击** — 右侧面板固定显示该国家详情
- **滚轮缩放** — 世界地图流畅缩放拖拽

颜色说明：橙色 = 有贸易数据，灰色 = 无贸易数据

## 重新生成

```bash
pip install mapshaper  # 首次需安装
mapshaper World_Bank_Official_Boundaries_Admin_0.geojson \
  -simplify 10% keep-shapes \
  -o format=topojson world.topo.json

python3 generate_map.py
```

## 技术栈

- **Leaflet** — 地图渲染引擎（通过 CDN 加载，需要联网）
- **TopoJSON** — 经拓扑压缩的世界边界数据
- **topojson-client** — TopoJSON 转 GeoJSON
