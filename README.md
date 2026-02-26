# KungFuTrader 🥋
基于截拳道哲学的轻量级量化交易回测框架

## 核心理念
- **以无法为有法**：灵活适配多种策略
- **以无限为有限**：极简架构，易于扩展
- **如水无形**：适配不同市场与品种

## 快速开始
```bash
pip install -r requirements.txt
python examples/jkd_trend_following.py

kungfutrader/
├── core/          # 回测引擎与策略基类
├── data/          # 数据获取与预处理
├── risk/          # 风险管理模块
└── visualization/ # 结果可视化
