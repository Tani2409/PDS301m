import pandas as pd
import numpy as np

# 1. Create a sample dataset for the A/B test
data = {
    'user_id': range(1, 201),
    'group': ['A']*100 + ['B']*100,
    'converted': np.random.choice([0, 1], 200, p=[0.8, 0.2]) # Dummy data for Group A
}
# Make Group B slightly better
data['converted'][100:] = np.random.choice([0, 1], 100, p=[0.75, 0.25])
ab_test_df = pd.DataFrame(data)

# 2. Handle potential complex data issues (e.g., custom methods)
# Let's say we want a text label for conversion
def get_status(n):
    return 'Converted' if n == 1 else 'Not Converted'

# Apply a custom function to create a new column
ab_test_df['status'] = ab_test_df['converted'].apply(get_status)

# 3. Aggregate the data to calculate conversion rates
conversion_rates = ab_test_df.groupby('group')['converted'].mean()
print("\nConversion Rates by Group:\n", conversion_rates)

# 4. Analyze the result
if conversion_rates['B'] > conversion_rates['A']:
    print("\nConclusion: Group B performed better.")
else:
    print("\nConclusion: Group A performed better.")
