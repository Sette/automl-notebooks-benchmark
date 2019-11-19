import pandas as pd


df = pd.read_csv("train.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df['target'].unique())

print("TEST DATASET DESCRIBE -----------------------------------------------------")

df = pd.read_csv("test.csv")

print(df.head())
print(df.info())
print(df.describe())

