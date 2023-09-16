import pandas as pd

# Sample stock price data
data = {
    'Date': ['2023-06-01', '2023-06-02', '2023-06-03', '2023-06-04', '2023-06-05'],
    'StockName': ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB'],
    'OpenPrice': [130.50, 2700.00, 250.00, 3500.00, 320.00],
    'HighPrice': [135.00, 2720.00, 255.00, 3550.00, 330.00],
    'LowPrice': [128.00, 2680.00, 245.00, 3400.00, 315.00],
    'ClosePrice': [132.50, 2690.00, 252.00, 3520.00, 325.00],
    'Volume': [1000000, 2000000, 1500000, 1800000, 1200000]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to an XLSX file
df.to_excel('stock_prices.xlsx', index=False)