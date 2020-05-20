import pandas as pd 
from matplotlib import pyplot as plt

df1 = pd.read_csv("/home/milton/github/REST_API_project/displaycommits.csv")

# Create our bar chart as before
plt.bar(x = 1, height = df1['Commits'])

# Give it a title
plt.title("Number of commits in learning_py")

# Give the x and y axes a title
plt.xlabel("learning_py")
plt.ylabel("Commits")

# Finally, show me our new plot
plt.show()

df2 = pd.read_csv("/home/milton/github/REST_API_project/displaycommitstwo.csv")

# Create our bar chart as before
plt.bar(x = 1, height = df2['Commits'])

# Give it a title
plt.title("Number of commits in Runescape")

# Give the x and y axes a title
plt.xlabel("Runescape")
plt.ylabel("Commits")

# Finally, show me our new plot
plt.show()

df3 = pd.read_csv("/home/milton/github/REST_API_project/displaycommitsthree.csv")

# Create our bar chart as before
plt.bar(x = 1, height = df3['Commits'])

# Give it a title
plt.title("Number of commits in REST_API_project")

# Give the x and y axes a title
plt.xlabel("REST_API_project")
plt.ylabel("Commits")

# Finally, show me our new plot
plt.show()