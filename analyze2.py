import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

df = pd.read_csv('Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System.csv')

#StratificationCategory1 has 6 categories so it is useful to seperate by category 
income = df.loc[df['StratificationCategory1'] == 'Income']
age = df.loc[df['StratificationCategory1'] == 'Age (years)']
ethnicity = df.loc[df['StratificationCategory1'] == 'Race\Ethnicity']
education = df.loc[df['StratificationCategory1'] == 'Education']
sex = df.loc[df['StratificationCategory1'] == 'Sex']
total = df.loc[df['StratificationCategory1'] == 'Total']

#Error: \\wsl.localhost\Ubuntu\home\joonha\CrimeInLA\analyze2.py:36: SyntaxWarning: invalid escape sequence '\E'
#Need to rename Race\Ethnicity

#print(df['StratificationCategory1'].unique())
print(df['Age(years)'].unique())

print(income)
income1 = income.loc[income['Stratification1'] == '$15,000 - $24,999']
income2 = income.loc[income['Stratification1'] == '$25,000 - $34,999']
income3 = income.loc[income['Stratification1'] == '$35,000 - $49,999']
income4 = income.loc[income['Stratification1'] == '$50,000 - $74,999']
income5 = income.loc[income['Stratification1'] == '$75,000 or greater']
income6 = income.loc[income['Stratification1'] == 'Data not reported']
income7 = income.loc[income['Stratification1'] == 'Less than $15,000']


age1 = age.loc[age['Stratification1'] == '18 - 24']
age2 = age.loc[age['Stratification1'] == '25 - 34']
age3 = age.loc[age['Stratification1'] == '35 - 44']
age4 = age.loc[age['Stratification1'] == '45 - 54']
age5 = age.loc[age['Stratification1'] == '55 - 64']
age6 = age.loc[age['Stratification1'] == '65 or older']


incomes = [income1, income2, income3, income4, income5, income6, income7]
for i, income in enumerate(incomes):
    print(f"Dataset {i + 1}")
    mean = np.mean(income['Low_Confidence_Limit'])
    variance = np.var(income['Low_Confidence_Limit'])
    std_deviation = np.std(income['Low_Confidence_Limit'])

    print(f"Mean: {mean}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_deviation}")

for i, income in enumerate(incomes):
    print(f"Dataset {i + 1} High")
    mean = np.mean(income['High_Confidence_Limit '])
    variance = np.var(income['High_Confidence_Limit '])
    std_deviation = np.std(income['High_Confidence_Limit '])

    print(f"Mean: {mean}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_deviation}")


grouped_stats = income1.groupby('Stratification1')['Low_Confidence_Limit'].agg(['mean', 'var'])

print(grouped_stats)

grouped_stats = income1.groupby('Stratification1')['High_Confidence_Limit '].agg(['mean', 'var'])

print(grouped_stats)

grouped_stats = income2.groupby('Stratification1')['Low_Confidence_Limit'].agg(['mean', 'var'])

print(grouped_stats)

grouped_stats = income2.groupby('Stratification1')['High_Confidence_Limit '].agg(['mean', 'var'])

print(grouped_stats)
grouped_stats = income3.groupby('Stratification1')['Low_Confidence_Limit'].agg(['mean', 'var'])

print(grouped_stats)

grouped_stats = income3.groupby('Stratification1')['High_Confidence_Limit '].agg(['mean', 'var'])

print(grouped_stats)
grouped_stats = income4.groupby('Stratification1')['Low_Confidence_Limit'].agg(['mean', 'var'])

print(grouped_stats)
grouped_stats = income4.groupby('Stratification1')['High_Confidence_Limit '].agg(['mean', 'var'])

print(grouped_stats)
grouped_stats = income5.groupby('Stratification1')['Low_Confidence_Limit'].agg(['mean', 'var'])

print(grouped_stats)
grouped_stats = income5.groupby('Stratification1')['High_Confidence_Limit '].agg(['mean', 'var'])

print(grouped_stats)
grouped_stats = income6.groupby('Stratification1')['Low_Confidence_Limit'].agg(['mean', 'var'])

print(grouped_stats)
grouped_stats = income6.groupby('Stratification1')['High_Confidence_Limit '].agg(['mean', 'var'])

print(grouped_stats)
grouped_stats = income7.groupby('Stratification1')['Low_Confidence_Limit'].agg(['mean', 'var'])

print(grouped_stats)

grouped_stats = income7.groupby('Stratification1')['High_Confidence_Limit '].agg(['mean', 'var'])

print(grouped_stats)


data_wide = pd.DataFrame({
    '$15,000 - $24,999': income1['Low_Confidence_Limit'],
    '$25,000 - $34,999': income2['Low_Confidence_Limit'],
    '$35,000 - $49,999': income3['Low_Confidence_Limit'],
    '$50,000 - $74,999': income4['Low_Confidence_Limit'],
    '$75,000 or greater': income5['Low_Confidence_Limit'],
    'Data not reported': income6['Low_Confidence_Limit'],
    'Less than $15,000': income7['Low_Confidence_Limit'],

})

income_long = pd.melt(data_wide, var_name='Category', value_name='Value')

print(income['Low_Confidence_Limit'])
plt.figure(figsize=(8, 6))
sns.boxplot(x='Category', y='Value', data=income_long)
plt.xticks(rotation=45, ha='right')
plt.title('BMI (Low) by Income Range')
plt.xlabel('Income')
plt.ylabel('BMI (Low end of confidence range)')
plt.tight_layout()
plt.show()


data_wide = pd.DataFrame({
    '18 - 24': age1['Low_Confidence_Limit'],
    '25 - 34': age2['Low_Confidence_Limit'],
    '35 - 44': age3['Low_Confidence_Limit'],
    '45 - 54': age4['Low_Confidence_Limit'],
    '55 - 64': age5['Low_Confidence_Limit'],
    '65 or older': age6['Low_Confidence_Limit'],

})

income_long = pd.melt(data_wide, var_name='Category', value_name='Value')

print(income['Low_Confidence_Limit'])
plt.figure(figsize=(8, 6))
sns.boxplot(x='Category', y='Value', data=income_long)
plt.xticks(rotation=45, ha='right')
plt.title('BMI (Low) by Age Range')
plt.xlabel('Age')
plt.ylabel('BMI (Low end of confidence range)')
plt.tight_layout()
plt.show()