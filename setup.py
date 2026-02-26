from setuptools import setup, find_packages
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 setup(
     name="kungfutrader",
     version="0.1.0",
     author="KING2026960",
     author_email="your.email@example.com",
     description="基于截拳道哲学的轻量级量化交易回测框架",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/KING2026960/KungFuTrader",
     packages=find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     python_requires=">=3.8",
     install_requires=[
         "pandas>=1.5.0",
         "numpy>=1.21.0",
         "matplotlib>=3.5.0",
         "yfinance>=0.1.87",
         "scipy>=1.7.0",
     ],
 )
