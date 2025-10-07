article1_tags = {"python", "data science", "pandas", "machine learning"}
article2_tags = {"python", "web development", "django", "data science"}

# 1. Find common tags using intersection (&)
common_tags = article1_tags & article2_tags
print(f"Common Tags: {common_tags}")

# 2. Find tags unique to the first article using difference (-)
unique_to_article1 = article1_tags - article2_tags
print(f"Tags unique to Article 1: {unique_to_article1}")
