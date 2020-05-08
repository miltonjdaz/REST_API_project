# Project number 3 
import pandas as pd 
from github import Github 
"import boto3"
import os

gh_us = os.environ.get('gh_user')
gh_pw = os.environ.get('gh_pass')

github = Github(gh_us, gh_pw)
transfer = github.PullRequest.PullRequest.get_commits() 

df1 = pd.DataFrame(transfer) 
  
# saving the dataframe 
df1.to_csv('/home/milton/github/REST_API_project/displaycommits.csv')

"""
s3 = boto3.resource('s3')
s3.meta.client.upload_file(displaycommits.csv, 'YOUR_S3_BUCKET_NAME', 'DESIRED_S3_OBJECT_NAME')
"""

import ipdb; ipdb.set_trace()