# Project number 3 

import pandas as pd 
from github import Github 
# import boto3
import os

# Protecting the connection information  
auth_token = os.environ.get('gh_token')

g = Github(auth_token)

repos_obj = g.get_repo('miltonjdaz/learning_py')  

newobj = repos_obj.get_commits()

for i in newobj: 
    print(i)

# next level of pulling data is looping over paginated list newobj
numofcommits = []
for i, value in enumerate(newobj, 1):
    iv = i, value
    numofcommits.append(iv)
    print(numofcommits)

# import ipdb; ipdb.set_trace()

# Saving the dataframe into a CSV file 
df1 = pd.DataFrame(numofcommits)

# df1 = pd.DataFrame.set_value(i, 'commits', value)
df1.to_csv('/home/milton/github/REST_API_project/displaycommits.csv')


#     # only if you have multiple elements for each 

#     newobj[i][elem]. i is rows. elem is column.
#     # if you have only one, then only extract one.
#     

# TODO deliverable
# feel free to use functions or multiple API objects to pull different kinds of data
# one or multiple dataframes that have data from whatever you want. 
# If you can join between dfs, that's awesome.

# This is on hold as I try to fix the github pull request 
"""
s3 = boto3.resource('s3')
s3.meta.client.upload_file(displaycommits.csv, 'YOUR_S3_BUCKET_NAME', 'DESIRED_S3_OBJECT_NAME')
"""