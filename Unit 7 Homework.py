# Unit 7 Homework
# Retrieve Information from SQL Databases

# Lesson 1 - Database Structure

  # Question 1 - SQL Q1
  # The Shopper column in the orders table is a ______ key
      # Answer -- foreign

# Lesson 2 - Populating a Database

    # Question 1 - SQL Q2
    # Assume you used SQLite to connect to a new (populated) database
        # and want to see what tables it contains

         # What command should you enter at the prompt?

        # Answer -- .tables

    # Question 2 - SQL Q3
    # Visit the SQLite documentation and navigate to the section on Data Types
        # in SQLite Version 3 to answer the following question:

        # How does SQLite store boolean values?

        # Answer -- integers 0 and 1

    # Question 3 - SQL Q4
    # Download world.sql database. Create a file called world.db and connect to
        # it via SQLite. Run the SQL script to populate the world database

        # Enter the following query;
        SELECT COUNT(*) FROM country;

        # You should get a number back. This represents the number of rows
            # in the country table

        # What is the value?

        # Answer -- 239
