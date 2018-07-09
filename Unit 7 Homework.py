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

# Lesson 3 - Writing Simple Queries

    # Question 1 - SQL Q5
    # Use the WHERE clause to show the appearance of rats.
    # You should return your query as a string assigned to the variable one_where, as follows:

    # Provided Code
    one_where = '''
    enter your query here
    '''

    # Submitted Code
    one_where = """
    SELECT apperance FROM animals
        WHERE species = 'rat'
    """

    # Question 2 -- SQL 06
    # Use IN to show the species for animals with vertebrae_class 'mammal' and
    # 'amphibian'
    # Return your query as:

    # Provided Code
    two_in = '''
    enter your query here
    '''

    # Submitted Code
    two_in = """
    SELECT species FROM animals
        WHERE vertebrate_class IN ('mammal','amphibian')
    """

    # Question 3 -- SQL 07
    # Use BETWEEN to show species that have at least 1 leg, but no more than 3 legs

    # Provided Code
    three_between = '''
    enter your query here
    '''

    # Submitted Code
    three_between = """
    SELECT species FROM animals
        WHERE num_legs BETWEEN 1 AND 3
    """

    # Question 4 -- SQL 08
    # Use LIKE to show species that have an appearance that starts with 'f'

    # Provided Code
    four_like = '''
    enter query here
    '''

    # Submitted Code
    four_like = """
    SELECT species FROM animals
        WHERE apperance LIKE 'f%'
    """

# Lesson 4 -- Writing Aggregate Queries

    # Question 1 -- SQL Q9
    # Use an aggregate function to return the number of countries that became independent
        # in the year 1918.

    # Provided Code
    agg_1918 = '''
    enter query here
    '''

    # Submitted Code
    agg_1918 = '''
    SELECT COUNT(DISTINCT name)
        FROM country
        WHERE indepyear = 1918;
    '''

    # Question 2 -- SQL10
    # Write a query that returns the average population of countries whose government is
        # a constitutional monarchy

    # Provided Code
    agg_constmon = '''
    enter query here
    '''

    # Submitted Code
    agg_constmon = '''
    SELECT AVG(population), name
        FROM country
        WHERE governmentform = 'Constitutional Monarchy';
    '''

    # Question 3 -- SQL11
    # Write a query that returns each continent and the area of the largest country
        # in that continent

    # Provided Code
    agg_areas = '''
    enter query here
    '''

    # Submitted Code
    agg_areas = '''
    SELECT continent, MAX(surfacearea)
        FROM country
        GROUP BY continent;
    '''
