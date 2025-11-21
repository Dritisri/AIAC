import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Example: Load your financial dataset
#df = pd.read_csv('financial_data.csv')

# For demonstration, create a mock financial dataset
data = {
    'date': pd.date_range("2023-01-01", periods=60),
    'company_name': ['AlphaTech']*20 + ['BetaBank']*20 + ['GammaEnergy']*20,
    'sector': ['Technology']*20 + ['Finance']*20 + ['Energy']*20,
    'stock_price': np.random.normal(100, 15, 60),
    'volume': np.random.normal(10000, 2000, 60)
}
df = pd.DataFrame(data)

# Randomly set some stock_price and volume as missing
np.random.seed(42)
missing_idx = np.random.choice(df.index, size=8, replace=False)
df.loc[missing_idx[:4], 'stock_price'] = np.nan
df.loc[missing_idx[4:], 'volume'] = np.nan

# 1. Handle missing values in stock_price and volume
df['stock_price'] = df['stock_price'].fillna(df['stock_price'].mean())
df['volume'] = df['volume'].fillna(df['volume'].median())

# 2. Create new features: moving averages (7-day, 30-day) by company
df.sort_values(['company_name', 'date'], inplace=True)
df['ma_7'] = df.groupby('company_name')['stock_price'].transform(lambda x: x.rolling(window=7, min_periods=1).mean())
df['ma_30'] = df.groupby('company_name')['stock_price'].transform(lambda x: x.rolling(window=30, min_periods=1).mean())

# 3. Normalize continuous variables using StandardScaler
continuous_columns = ['stock_price', 'volume', 'ma_7', 'ma_30']
scaler = StandardScaler()
df[continuous_columns] = scaler.fit_transform(df[continuous_columns])

# 4. Encode categorical columns
categorical_cols = ['sector', 'company_name']
encoder = OneHotEncoder(sparse_output=False, drop='first')
encoded = encoder.fit_transform(df[categorical_cols])
encoded_cols = encoder.get_feature_names_out(categorical_cols)
df_encoded = pd.DataFrame(encoded, columns=encoded_cols, index=df.index)

# Merge encoded columns and drop originals
df = df.drop(columns=categorical_cols).join(df_encoded)

# Final feature-engineered DataFrame ready for ML tasks
print(df.head())

# Optionally save to new CSV
df.to_csv('financial_data_feature_engineered.csv', index=False)
