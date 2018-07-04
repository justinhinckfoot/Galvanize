# Pandas Homework

# Part 1 -- The Basics of DataFrames
    # General workflow for moving data into DataFrames
        # import pandas
        # read data into dataframe
        # get a sense for the data
    # For this part you should
        # Import Pandas
        # Read the wine data into a DataFrame
        # Use the attribute and methods available on DataFrames to answer:
                # How many rows and columns are in the DataFrame?
                # What data type is in each column?
                # Are all of the variables continuous, or are any categorical?
                # How many non-null values are in each columns?
                # What are the min, mean, max, median for all numeric columns
    import pandas as pd
    df = read_csv('data/winequality-red.csv',delimiter=';')
    df.shape
    df.dtypes
    df.count()
    df.describe().mean()
    df.describe().min()
    df.describe().max()
    df.describe().median()
