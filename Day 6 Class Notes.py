# Class Notes
# Thursday, July 5, 2018


# Homework Examples
import pandas as pd
df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8], 'c': [9, 10, 11, 12]}
    ,index=['i', 'ii', 'iii', 'iv'])
df
df.describe()
df.describe().loc['mean']
df.describe().iloc[1]
df.describe().loc[['mean','min']]


# Pandas and SQL
    # SQLite3 is included initially with Panda
    # Can store the database name/value as a variable to call
        VARIABLE = sqlite3.connect('DATABASE NAME')
    # Can return a sql into a Pandas DataFrame
    # Can read sql from a single Pandas expression
        pd.read_sql("SQL Query", CONNECTION VARIABLE)
    # To list all table names in a database
        res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for name in res:
            print(name[0])
        "OR"
        conn.execute("SELECT name FROM sqlist_master WHERE type='table';)
