import pandas as pd

# Load data from the CSV we created earlier
df = pd.read_csv('data.csv')

# Inspect the DataFrame
print("DataFrame Head:\n", df.head())
print("\nDataFrame Info:")
df.info()

# Working with data: selecting and filtering
scores = df['score']  # Select a single column (a Series)
high_scorers = df[df['score'] > 90] # Filter rows based on a condition
print("\nHigh Scorers:\n", high_scorers)

# Save the filtered data to a new file
high_scorers.to_csv('high_scorers.csv', index=False)
