import pandas as pd

# Load the dataset
df = pd.read_csv("netflix_titles_original.csv")

# Drop duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna({
    'director': 'Unknown',
    'cast': 'Unknown',
    'country': 'Unknown',
    'date_added': 'Unknown',
    'rating': 'Unknown',
    'duration': 'Unknown'
}, inplace=True)

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert date_added to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Standardize text fields
for col in ['type', 'country', 'rating']:
    df[col] = df[col].astype(str).str.title().str.strip()

# Save cleaned version
df.to_csv("cleaned_netflix_titles.csv", index=False)
