# Project number 3 

import pandas as pd 
from github import Github 
"import boto3"
import os

# Protecting my username and password 

gh_us = os.environ.get('gh_user')
gh_pw = os.environ.get('gh_pass')

# For some reason, this is not working

github = Github(gh_us, gh_pw)
transfer = github.PullRequest.PullRequest.get_commits() 

# Code to make have transfer become a dataframe

df1 = pd.DataFrame(transfer) 
  
# Saving the dataframe into a CSV file 
df1.to_csv('/home/milton/github/REST_API_project/displaycommits.csv')


# This is on hold as I try to fix the github pull request 
"""
s3 = boto3.resource('s3')
s3.meta.client.upload_file(displaycommits.csv, 'YOUR_S3_BUCKET_NAME', 'DESIRED_S3_OBJECT_NAME')
"""

import ipdb; ipdb.set_trace()