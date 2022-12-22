import pandas as pd
import numpy as np

# creating dataframe
df = pd.read_csv('pokemon.csv')

# print 10 first rows:
# print(df.head(10))

# print 10 last rows:
# print(df.tail(10))

# print random rows:
# print(df.sample(10))

# print information about the dataframe:
# print(df.info())

# print statistic information about the dataframe:
# print(df.describe())

# print quantity of rows and columns:
# rows, columns = df.shape
# print(f'Rows: {rows}\nColumns: {columns}')

# print a specific column:
# specificColumn = df['primary_type']
# print(specificColumn)

# print specifics columns:
# specificColumn = df[['english_name', 'primary_type']]
# print(specificColumn)

# print rows with specific values
# specificRows = df[df['primary_type'] == 'ghost']
# print(specificRows)

# print columns and rows in a condition (SELECT column1, column2, column3 FROM df
#                                        WHERE column3 = 'value'
# specificCondition = df[df['against_ghost'] > 1]
# specificCondition = specificColumnsRows[['english_name', 'primary_type', 'against_ghost']]
# print(specificCondition)

# print columns and rows in multiple conditions (SELECT column1, column2, column3 FROM df
#                                                WHERE column3 > valueA
#                                                AND column3 > valueB
# specificCondition = df[(df['against_ghost'] > 1) & (df['against_dark'] > 1)]
# specificCondition = specificCondition[['english_name', 'primary_type', 'against_ghost', 'against_dark']]
# print(specificCondition)

# print columns and rows in multiple conditions (SELECT column1, column2, column3 FROM df
#                                                WHERE column3 > valueA
#                                                OR column3 < valueB
# specificCondition = df[(df['against_ghost'] > 1) | (df['against_dark'] < 1)]
# specificCondition = specificCondition[['english_name', 'primary_type', 'against_ghost', 'against_dark']]
# print(specificCondition)


# print rows with not null values:
# notNullRows = df[df['mega_evolution'].notna()]
# print(notNullRows[['english_name', 'mega_evolution']])

# method iloc select fields by their index:
# print(df.iloc[0]) # first row
# print(df.iloc[0:10]) # first ten rows
# print(df.iloc[0].english_name) # first row + column specified
# print(df.iloc[0:10, 0:3]) # first ten rows and first three columns
# print(df.iloc[0:10:2]) # first ten rows skipping rows

# method loc select fields by their name:
# print(df.loc[0, 'english_name']) # select specific column and specific rows
# print(df.loc[:, 'english_name']) # select specific column and all rows
