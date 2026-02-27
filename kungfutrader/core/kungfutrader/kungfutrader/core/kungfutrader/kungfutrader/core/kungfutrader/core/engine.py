import pandas as pd
 import numpy as np
 class BacktestEngine:
     def __init__(self, data: pd.DataFrame, initial_capital: float = 10000.0):
         self.data = data.copy()
         self.initial_capital = initial_capital
         self.current_capital = initial_capital
         self.position = 0.0
         self.equity_curve = []
         self.trades = []
     def run(self, strategy):
         strategy.initialize(self.data)
         for i in range(len(self.data)):
             current_price = self.data["close"].iloc[i]
             signal = strategy.next_signal(i)
             
             if signal == "buy" and self.position == 0:
                 self.position = self.current_capital / current_price
                 self.current_capital = 0.0
                 self.trades.append({
                     "type": "buy",
                     "price": current_price,
                     "date": self.data.index[i]
                 })
             elif signal == "sell" and self.position > 0:
                 self.current_capital = self.position * current_price
                 self.position = 0.0
                 self.trades.append({
                     "type": "sell",
                     "price": current_price,
                     "date": self.data.index[i]
                 })
             
             self.equity_curve.append(self.current_capital + self.position * current_price)
         
         final_capital = self.current_capital + self.position * self.data["close"].iloc[-1]
         total_return = (final_capital - self.initial_capital) / self.initial_capital
         equity_array = np.array(self.equity_curve)
         returns = np.diff(equity_array) / equity_array[:-1]
         sharpe_ratio = np.sqrt(252) * np.mean(returns) / np.std(returns) if len(returns) > 0 else 0.0
         peak = np.maximum.accumulate(equity_array)
         drawdown = (equity_array - peak) / peak
         max_drawdown = np.min(drawdown) if len(drawdown) > 0 else 0.0
         
         return {
             "final_capital": final_capital,
             "total_return": total_return,
             "sharpe_ratio": sharpe_ratio,
             "max_drawdown": max_drawdown,
             "equity_curve": self.equity_curve,
             "trades": self.trades
