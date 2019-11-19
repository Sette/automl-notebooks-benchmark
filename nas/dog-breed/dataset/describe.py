import pandas as pd


df = pd.read_csv("labels_real.csv")

print(df.head())
print(df.info())
print(df.describe())
print(len(df['breed'].unique()))

print("TEST DATASET DESCRIBE -----------------------------------------------------")

df = pd.read_csv("sample_submission_real.csv")

print(df.head())
print(df.info())
print(df.describe())

