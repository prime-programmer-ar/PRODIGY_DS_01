import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset directly from the web
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

print("Dataset loaded successfully! Here are the first 5 rows:")
print(df.head())
print("-" * 50)

# ==========================================
# Task A: Bar Chart for Categorical Variable
# Variable: 'Sex' (Gender)
# ==========================================
categorical_col = 'Sex' 

# Count the occurrences of each category
category_counts = df[categorical_col].value_counts()

plt.figure(figsize=(8, 5))
# Create the bar chart
plt.bar(category_counts.index, category_counts.values, color=['#4C72B0', '#DD8452'], edgecolor='black')

plt.title(f'Distribution of {categorical_col.capitalize()} on the Titanic')
plt.xlabel('Gender')
plt.ylabel('Count')

# Add data labels on top of the bars
for i, v in enumerate(category_counts.values):
    plt.text(i, v + 5, str(v), ha='center', fontweight='bold')
    
plt.show()
# saving the image
plt.savefig('titanic_gender_distribution.png')
# ==========================================
# Task B: Histogram for Continuous Variable
# Variable: 'Age'
# ==========================================
continuous_col = 'Age'

plt.figure(figsize=(8, 5))

# Create the histogram
# .dropna() removes missing age values so the plot renders correctly
plt.hist(df[continuous_col].dropna(), bins=20, color='#55A868', edgecolor='black')

plt.title(f'Distribution of {continuous_col} on the Titanic')
plt.xlabel('Age (Years)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.5)

plt.show()
# saving the image
plt.savefig('titanic_age_distribution.png')