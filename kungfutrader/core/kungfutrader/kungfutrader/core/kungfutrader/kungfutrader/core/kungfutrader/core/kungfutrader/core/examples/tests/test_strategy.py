import pandas as pd
 import numpy as np
 from kungfutrader.core.engine import BacktestEngine
 from kungfutrader.core.strategy import JKDTrendFollowing
 def test_strategy_import():
     """测试策略能否正常导入"""
     strategy = JKDTrendFollowing()
     assert strategy is not None
     print("✅ 策略导入成功")
 def test_engine_basic():
     """测试回测引擎基础功能"""
     data = pd.DataFrame({
         "close": np.linspace(100, 200, 100)
     })
     engine = BacktestEngine(data, initial_capital=10000)
     strategy = JKDTrendFollowing(short_window=5, long_window=10)
     perf = engine.run(strategy)
     assert "total_return" in perf
     assert "sharpe_ratio" in perf
     assert "max_drawdown" in perf
     assert perf["final_capital"] > 0
     print("✅ 回测运行正常，指标计算无误")
 def run_all_tests():
     print("🧪 开始运行 KungFuTrader 单元测试...\n")
     test_strategy_import()
     test_engine_basic()
     print("\n🎉 全部测试通过！")
 if __name__ == "__main__":
     run_all_tests()
