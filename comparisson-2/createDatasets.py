import pandas as pd

test_df =  pd.read_csv("comparisson-2\\dataset\\CEAS_08.csv")


#for old methods
df_old = pd.DataFrame()
df_old["text"] = test_df["body"]
df_old["label_num"] = test_df["label"]
df_old['label'] = test_df['label'].map({1: 'spam', 0: 'ham'})

#new method

df_new = pd.DataFrame()
df_new["text"] = test_df["body"]
df_new['label'] = test_df['label'].map({1: 'spam', 0: 'ham'})

df_old.to_csv("comparisson-2\\dataset\\old.csv")
df_new.to_csv("comparisson-2\\dataset\\new.csv")
