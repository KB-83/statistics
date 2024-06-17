import pandas as pd

# Load the dataset
df = pd.read_csv('resources/project/Titanic-Dataset.csv')


column_name = 'Name'


# Find duplicated rows
duplicates = df[df.duplicated(subset=['Name','Sex'])]

# Display the first few rows of the dataframe
print(duplicates)
