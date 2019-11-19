import pandas as pd

df = pd.read_csv("sample_submission.csv")
print(df.head())
df['id'] = [name+".jpg" for name in df['id']]
df.to_csv("sample_submission_real.csv",index=False)


df = pd.read_csv("labels.csv")
print(df.head())
df['id'] = [name+".jpg" for name in df['id']]
df.to_csv("labels_real.csv",index=False)

