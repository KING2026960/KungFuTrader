from abc import ABC, abstractmethod
 import pandas as pd
 class StrategyBase(ABC):
     @abstractmethod
     def next_signal(self, data_row: pd.Series) -> str:
         """
         根据当前数据行返回交易信号
         :param data_row: 包含当前价格、指标等数据的Series
         :return: 'buy', 'sell' 或 'hold'
         """
         pass
 class JKDTrendFollowing(StrategyBase):
     """截拳道风格的趋势跟随策略：如水无形，适应市场"""
     def __init__(self, short_window: int = 20, long_window: int = 50):
         self.short_window = short_window
         self.long_window = long_window
         self.price_history = []
     def next_signal(self, data_row: pd.Series) -> str:
         close_price = data_row["close"]
         self.price_history.append(close_price)
         
         if len(self.price_history) < self.long_window:
             return "hold"
         
         short_ma = pd.Series(self.price_history[-self.short_window:]).mean()
         long_ma = pd.Series(self.price_history[-self.long_window:]).mean()
         
         if short_ma > long_ma:
             return "buy"
         elif short_ma < long_ma:
             return "sell"
         else:
             return "hold"
