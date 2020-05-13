# Project number 3 

import pandas as pd 
from github import Github 
# import boto3
import os

# Protecting my username and password 

auth_token = os.environ.get('gh_token')

# For some reason, this is not working

g = Github(auth_token)



repos_obj = g.get_repo('miltonjdaz/learning_py') # explore methods attached to repos obj
import ipdb; ipdb.set_trace()
# TODO after you're done exploring, choose a method i.e. 
# newobj = repos_obj.get_newobj()
# explore the new object with for loops if they are paginated lists.
# i.e. for i in newobj: print(i)
# just to start




# Code to make have transfer become a dataframe

# TODO
# next level of pulling data is looping over paginated list newobj
# i.e.
# for i, elem in enumerate(newobj):
#     df.set_value(i, '1stcolname', newobj.elem)
#     # only if you have multiple elements for each 

#     newobj[i][elem]. i is rows. elem is column.
#     # if you have only one, then only extract one.
#     df.set_value(i, '2ndcolname', newobj.elem)

# TODO deliverable
# feel free to use functions or multiple API objects to pull different kinds of data
# one or multiple dataframes that have data from whatever you want. 
# If you can join between dfs, that's awesome.
  
# Saving the dataframe into a CSV file 
# df1.to_csv('/home/milton/github/REST_API_project/displaycommits.csv')


# This is on hold as I try to fix the github pull request 
"""
s3 = boto3.resource('s3')
s3.meta.client.upload_file(displaycommits.csv, 'YOUR_S3_BUCKET_NAME', 'DESIRED_S3_OBJECT_NAME')
"""


