from ucimlrepo import fetch_ucirepo 
  
# fetching dataset 
adult = fetch_ucirepo(id=2) 
  
X = adult.data.features 
y = adult.data.targets 
  
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = X.copy()  
data['income'] = y 
print("First few rows of the dataset:")
print(data.head())

# 1. Bar Plot: Visualizing the frequency of education levels
plt.figure(figsize=(10, 6))
sns.countplot(x='education', data=data, palette='Set2')
plt.title('Frequency of Education Levels')
plt.xlabel('Education Level')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# 2. Pie Chart: Proportion of marital status
plt.figure(figsize=(8, 8))
data['marital-status'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette('Set3'))
plt.title('Proportion of Marital Status')
plt.ylabel('')  # Hides the y-label
plt.show()

# 3. Dot Plot: Visualizing the relationship between hours-per-week and income level
plt.figure(figsize=(10, 6))
sns.stripplot(x='income', y='hours-per-week', data=data, jitter=True, palette='Set1', dodge=True)
plt.title('Dot Plot of Hours per Week by Income Level')
plt.xlabel('Income Level')
plt.ylabel('Hours per Week')
plt.show()

plt.savefig('education_barplot.png')
plt.savefig('marital_status_piechart.png')
plt.savefig('hours_income_dotplot.png')
