import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('exams.csv')

# Calculate average scores
df['Average Score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

# Top 5 performers
top_students = df.sort_values(by='Average Score', ascending=False).head(5)

print("Top 5 Students Based on Average Score:")
print(top_students[['math score', 'reading score', 'writing score', 'Average Score']])

# Visualization
plt.figure(figsize=(8,5))
sns.boxplot(data=df[['math score', 'reading score', 'writing score']])
plt.title("Score Distribution in Subjects")
plt.show()
