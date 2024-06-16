import pandas as pd
from ydata_profiling import ProfileReport
from wordcloud import WordCloud
import matplotlib.pyplot as plt

user_path = input("enter path: ")
data = pd.read_csv(user_path)

# Generate the profile report
profile = ProfileReport(data, title='Data Dashboard')

# Display the profile report
profile.to_notebook_iframe()

# Get the column list
print("Column List:")
print(data.columns)

# Create a word cloud
text = ' '.join(data.astype(str).values.flatten())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(12,8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud')
plt.show()

# Display the correlation matrix
plt.figure(figsize=(12,8))
data.corr().plot(cmap='RdBu_r')
plt.title('Correlation Matrix')
plt.show()

duplicates = data[data.duplicated()]
print(duplicates)