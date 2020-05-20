# Project number 3 

import pandas as pd 
from github import Github 
import os

# Protecting the connection information  
auth_token = os.environ.get('gh_token')

g = Github(auth_token)

# Using the first repo
repos_obj = g.get_repo('miltonjdaz/learning_py')  

newobj = repos_obj.get_commits()

# next level of pulling data is looping over paginated list newobj
for value in enumerate(newobj, 1):
    iv = value
    print(iv)

# Saving the dataframe into a CSV file 
df1 = pd.DataFrame(iv)

# df1 = pd.DataFrame.set_value(i, 'commits', value)
df1.to_csv('/home/milton/github/REST_API_project/displaycommits.csv')

# Using the second repo
repos_objtwo = g.get_repo('miltonjdaz/Runescape')  

newobjtwo = repos_objtwo.get_commits()

# Find the number of commits
for value in enumerate(newobjtwo, 1):
    print(value)

# Saving the dataframe into a CSV file 
df2 = pd.DataFrame(value)

# df1 = pd.DataFrame.set_value(i, 'commits', value)
df2.to_csv('/home/milton/github/REST_API_project/displaycommitstwo.csv')

# Using the third repo
repos_objthree = g.get_repo('miltonjdaz/REST_API_project')  

newobjthree = repos_objthree.get_commits()

# Find the number of commits
for value in enumerate(newobjthree, 1):
    print(value)

# Saving the dataframe into a CSV file 
df3 = pd.DataFrame(value)

# df1 = pd.DataFrame.set_value(i, 'commits', value)
df3.to_csv('/home/milton/github/REST_API_project/displaycommitsthree.csv')