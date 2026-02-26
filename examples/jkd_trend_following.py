import yfinance as yf
 import matplotlib.pyplot as plt
 from kungfutrader.core.engine import BacktestEngine
 from kungfutrader.core.strategy import JKDTrendFollowing
 def main():
     # 1. 获取历史数据（以苹果股票为例）
     data = yf.download("AAPL", start="2020-01-01", end="2023-01-01")
     data = data[["Close"]].rename(columns={"Close": "close"})
     # 2. 初始化策略和回测引擎
     strategy = JKDTrendFollowing(short_window=20, long_window=50)
     engine = BacktestEngine(data, initial_capital=10000.0)
     # 3. 运行回测
     performance = engine.run(strategy)
     # 4. 打印结果
     print("=== 回测结果 ===")
     print(f"总收益率: {performance['total_return']:.2%}")
     print(f"夏普比率: {performance['sharpe_ratio']:.2f}")
     print(f"最大回撤: {performance['max_drawdown']:.2%}")
     print(f"最终资金: ${performance['final_capital']:.2f}")
     print(f"交易次数: {len(performance['trades'])}")
     # 5. 绘制资金曲线
     plt.figure(figsize=(12, 6))
     plt.plot(data.index, performance['equity_curve'], label='Equity Curve')
     plt.title('KungFuTrader - JKD Trend Following Strategy')
     plt.xlabel('Date')
     plt.ylabel('Equity')
     plt.legend()
     plt.grid(True)
     plt.show()
 if __name__ == "__main__":
     main()
