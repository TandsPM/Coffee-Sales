import pandas as pd

# Load the CSV
df = pd.read_csv("data/coffee_data.csv")

pd.set_option('display.max_columns', None)

# Fill missing with "No Card"
df['card'] = df['card'].fillna('No Card')

# Remove duplicate rows, if any
df = df.drop_duplicates()

# Check and remove invalid or zero/negative 'money' values
df = df[df['money'] > 0]

# lowercase and strip whitespace
df['cash_type'] = df['cash_type'].str.lower().str.strip()
df['coffee_name'] = df['coffee_name'].str.lower().str.strip()

# Save to Excel
df.to_excel("cleaned_data.xlsx", index=False, engine='openpyxl')

print("Data exported to cleaned_data.xlsx ✅")
