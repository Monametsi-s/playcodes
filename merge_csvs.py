import pandas as pd

# Load the first CSV file (ISDN, Found in HSS, Status, Operation Result)
df1 = pd.read_csv("file1.csv")

# Load the second CSV file (ISDN, APNTPLID)
df2 = pd.read_csv("file2.csv")

# Merge the two dataframes on the ISDN column
merged_df = pd.merge(df1, df2, on="ISDN", how="left")

# Save the merged dataframe to a new CSV file
merged_df.to_csv("merged_output.csv", index=False)

print("Merged CSV file saved as 'merged_output.csv'")