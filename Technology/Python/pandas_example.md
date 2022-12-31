# Pandas Example

-  Create dataframe reading excel file `df = pd.read_excel('Files\share.xlsx', sheet_name="BuySell")`
-  Create new dataframe from existing one with selected columns only `df1 = df[["Date"]].copy()`
-  To get static summary of dataframe `df.describe()`
-  To get correlation of columns `df.corr()`
-  To get duplicate in a dataframe `df.duplicated()` it will return Series with index and boolean value True or False for duplicate or not.
-  To remove duplicate rows `df.drop_duplicates(subset=None, keep='first', inplace=False)`
-  Groupby `df.groupby(["Share Id","Invenment","Profit"]).mean()`
