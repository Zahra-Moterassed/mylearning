import pandas as pd
from ydata_profiling import ProfileReport

user_path = input("enter path: ")
data = pd.read_csv(user_path)

# Generate the profile report
profile = ProfileReport(data, title='Data Dashboard')

# Display the profile report
profile.to_notebook_iframe()
