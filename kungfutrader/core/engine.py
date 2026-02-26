import pandas as pd
 import numpy as np
 class BacktestEngine:
     def __init__(self, data: pd.DataFrame, initial_capital: float = 10000.0):
         self.data = data
         self.initial_capital = initial_capital
         self.current_capital = initial_capital
         self.positions = 0
         self.trades = []
         self.equity_curve = []
     def run(self, strategy):
         for index, row in self.data.iterrows():
             signal = strategy.next_signal(row)
             if signal == "buy" and self.positions == 0:
                 self.positions = self.current_capital / row["close"]
                 self.current_capital = 0
                 self.trades.append({"type": "buy", "price": row["close"], "time": index})
             elif signal == "sell" and self.positions > 0:
                 self.current_capital = self.positions * row["close"]
                 self.positions = 0
                 self.trades.append({"type": "sell", "price": row["close"], "time": index})
             self.equity_curve.append(self.current_capital + self.positions * row["close"])
         return self._calculate_performance()
     def _calculate_performance(self):
         final_capital = self.current_capital + self.positions * self.data.iloc[-1]["close"]
         total_return = (final_capital - self.initial_capital) / self.initial_capital
         equity_array = np.array(self.equity_curve)
         daily_returns = np.diff(equity_array) / equity_array[:-1]
         sharpe_ratio = np.sqrt(252) * np.mean(daily_returns) / np.std(daily_returns)
         max_drawdown = np.max(np.maximum.accumulate(equity_array) - equity_array) / np.max(equity_array)
         return {
             "total_return": total_return,
             "sharpe_ratio": sharpe_ratio,
             "max_drawdown": max_drawdown,
             "final_capital": final_capital,
             "trades": self.trades,
             "equity_curve": self.equity_curve
