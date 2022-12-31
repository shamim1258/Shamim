# Pandas
-  Very powerful library for data cleaning, analysis and manipulation.
-  A fast and efficient DataFrame object for data manipulation.
-  It is built on the top of the NumPy library
-  Pandas Data Structure
   -  Series
   -  Dataframe

### Series
-  It is like a column in a table or one-dimensional array.

### Dataframe
-  It represents multi-dimentional array or table with multiple columns.
-  Heterogeneous tabular data structure with labeled axes (rows and columns).
-  Methods Used
   -  Data Correlations
      -  `corr()`
         -  This will give output in tabular format with value range from -1 to 1 showing the relationship of columns.
   -  Graph
      -  `plot()`
         -  Pandas uses the plot() method to create diagrams. We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
         

### Data Cleaning
-  Empty Cell
   -  If any cell in dataframe does not have any value i.e. nan it is termed as empty cell.
   -  Method-1 : remove these records as usually dataframe is very hugh removing few records will not impact much.
   -  Method-2 : replace null value with any default value `df.fillna(130, inplace = True)` and only replacing null in a column `df["column name"].fillna(130, inplace = True)`
   -  Method-3 : replace null with mean() median() and mode() `df["Col Name"].fillna(df["Col Name"].mean(), inplace = True)`.
-  Wrong Format
   -  This can be date format is different in few records.
   -  To Fix only 2 option either remove those records or convert all column values of same format, pandas has `to_datetime` method for this.
   -  Syntax `df['Date'] = pd.to_datetime(df['Date'])`
   -  For removing row - `df.dropna(subset=['Date'], inplace = True)`
-  Wrong Date
   -  This occur when data only is given wrong and hard to detech.
   -  Loop through all values in the "Duration" column. If the value is higher than 120, set it to 120:
^
    for x in df.index:
        if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120
^
-  Removing Duplicates
   -  Duplicate is said to occur when whole record is same any other record.
   -  For comparing duplicate records we can use method `duplicated()` it will return True or False.
   -  For removing duplicate use method `df.drop_duplicates(inplace = True)`
