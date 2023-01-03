# Pandas
-  Very powerful library for data cleaning, analysis and manipulation.
-  A fast and efficient DataFrame object for data manipulation.
-  It is built on the top of the NumPy library
-  Pandas Data Structure
   -  Series
   -  Dataframe
      -  axis: {0 or 'index', 1 or 'columns'}, default value 0
-  **Links :**
   -  [Syntax with Examples](pandas_example.md)

### Series
-  It is like a column in a table or one-dimensional array.

### Dataframe
-  It represents multi-dimentional array or table with multiple columns.
-  Heterogeneous tabular data structure with labeled axes (rows and columns).
-  Methods Used
   -  General
      -  `shape` - to number of row and column count in a dataframe.
      -  `columns` - to all column names and index.
      -  `df.index.values`
      -  `df.set_index('client',inplace=True)`
      -  `transpose()` - To transponse the dataframe i.e. convert rows into columns and vice verse.
      -  `describe()` - It returns the statistical summary of the Series and DataFrame i.e. count, mean, max, min aggregated over column with numeric values only.
      -  `head(n)` - It will return the first n rows from top, default value is 5.
   -  Aggregation
      -  `groupby()`
         -  A groupby operation involves some combination of splitting the object, applying a function, and combining the results. This can be used to group large amounts of data and compute operations on these groups.
         -  It will return the groupby object and we can you other aggregated function over the groupby object.
         -  Example `df.groupby(["Share Id","Invenment","Profit"]).mean()`
         -  `get_group()` to find the entries contained in any of the groups.
   -  Iteration
      -  Pandas use three functions for iterating over the rows of the DataFrame - iterrows(), iteritems() and itertuples()
      -  `iterrows()`
         -  If you want to loop over the DataFrame for performing some operations on each of the rows.
         -  It is used for iterating over the rows as (index, series) pairs.
         -  It returns an iterator that contains index and data of each row as a Series.
      -  `iteritems()` - used for iterating over the (key, value) pairs.
      -  `itertuples()` - used for iterating over the rows as namedtuples.
   -  Data Correlations
      -  `corr()`
         -  This will give output in tabular format with value range from -1 to 1 showing the relationship of columns.
   -  Relationship
      -  `join()`
         -  The method of combining the DataFrame using common fields is called "joining". The method that we use for combining the DataFrame is a join() method. The columns that contain common values are called "join key".
         -  Join Types
            -  Inner Join
            -  Left Join
   -  Graph
      -  `hist()`
         -  It is a quick way to understand the distribution of certain numerical variables from the dataset. It divides the values within a numerical variable into "bins". It counts the number of examinations that fall into each of the bin. These bins are responsible for a rapid and intuitive sense of the distribution of the values within a variable by visualizing bins.
         -  We can create a histogram by using the DataFrame.hist() method, which is a wrapper for the matplotlib pyplot API.
         -  It returns the matplotlib.AxesSubplot or numpy.ndarray
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
   -  We can use method `drop_duplicates()`
