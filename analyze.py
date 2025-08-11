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

crime = pd.read_csv('Crime_Data_from_2020_to_Present.csv')

print(crime)

crime_description = crime['Crm Cd Desc'].value_counts()

top_n = 10
top = crime_description.head(top_n)


plt.figure(figsize=(12, 8))
colors = ['purple', 'blue', 'green', 'red']

top.plot(kind='bar', color=colors)

plt.title(f'Top {top_n} Crime Types', fontsize=16)
plt.xlabel('Types', fontsize=12)
plt.ylabel('Number of Crime Entries', fontsize=12)
plt.xticks(rotation=45, ha='right') 

plt.tight_layout()
plt.show()


area_name = crime['AREA NAME'].value_counts()

top_n = 15
top = area_name.head(top_n)


plt.figure(figsize=(12, 8))
colors = ['pink', 'blue']

top.plot(kind='bar', color=colors)

plt.title(f'Top {top_n} Areas of Crime', fontsize=16)
plt.xlabel('Location', fontsize=12)
plt.ylabel('Number of Crime Entries', fontsize=12)
plt.xticks(rotation=45, ha='right') 

plt.tight_layout()
plt.show()


crime['DATE OCC CONV'] = pd.to_datetime(crime['DATE OCC'], format='%m/%d/%Y %I:%M:%S %p')


crime_s = crime.sort_values(by='DATE OCC CONV')
print(crime_s)

entries_per_month = crime_s.groupby(crime_s['DATE OCC CONV'].dt.to_period('M')).size()

plt.figure(figsize=(12, 6))
entries_per_month.plot(kind='line', marker='o')

plt.title('Number of Entries per Month', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Entries', fontsize=12)
plt.grid(True)

plt.tight_layout()
plt.show()