import pandas as pd
 import numpy as np
 class StrategyBase:
     def __init__(self):
         self.data = None
     
     def initialize(self, data: pd.DataFrame):
         self.data = data
     
     def next_signal(self, index: int) -> str:
         raise NotImplementedError("Subclasses must implement next_signal method")
 class JKDTrendFollowing(StrategyBase):
     def __init__(self, short_window: int = 20, long_window: int = 50):
         super().__init__()
         self.short_window = short_window
         self.long_window = long_window
     
     def initialize(self, data: pd.DataFrame):
         super().initialize(data)
         self.data["short_ma"] = self.data["close"].rolling(window=self.short_window).mean()
         self.data["long_ma"] = self.data["close"].rolling(window=self.long_window).mean()
     
     def next_signal(self, index: int) -> str:
         if index < self.long_window:
             return "hold"
         
         prev_short = self.data["short_ma"].iloc[index-1]
         prev_long = self.data["long_ma"].iloc[index-1]
         curr_short = self.data["short_ma"].iloc[index]
         curr_long = self.data["long_ma"].iloc[index]
         
         if prev_short < prev_long and curr_short > curr_long:
             return "buy"
         elif prev_short > prev_long and curr_short < curr_long:
             return "sell"
         else:
             return "hold"
