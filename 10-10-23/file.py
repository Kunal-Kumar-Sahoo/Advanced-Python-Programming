import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('./train.csv')

# Select numerical columns from the data dataframe
numerical_cols = data.select_dtypes(include=[np.number]).columns.tolist()

# Plot a histogram for each numerical column

plt.hist(data['Age'])
plt.title(f'Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# # Plot a bar graph for each numerical column

plt.bar(data.index, data['Age'])
plt.title(f'Bar Graph of Age')
plt.xlabel('Index')
plt.ylabel('Age')
plt.show()

# Create a scatter plot for age
plt.scatter(data.index, data['Age'])
plt.title(f'Scatter Plot of Age')
plt.xlabel('Index')
plt.ylabel('Age')
plt.show()


# Count the number of VIP and non-VIP passengers
vip_counts = data['VIP'].value_counts()
plt.bar(vip_counts.index.astype(str), vip_counts.values)
plt.title('Bar Graph of VIP and Non-VIP Counts')
plt.xlabel('VIP')
plt.ylabel('Count')
plt.show()

# Create a new column 'age_group' based on age
data['age_group'] = pd.cut(data['Age'], bins=[0, 30, 50, np.inf], labels=['1-30', '30-50', 'above 50'])

age_group_counts = data['age_group'].value_counts()
plt.pie(age_group_counts, labels=age_group_counts.index)
plt.title('Pie Chart of Age Group Counts')
plt.show()