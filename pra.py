import os
import numpy as np
import matplotlib.pyplot as plt 

def get_data(repos):
    from github import Github
    # Protecting the connection information 
    auth_token = os.environ.get('gh_token')

    # github object
    g = Github(auth_token)
    # repos object
    repos_obj = g.get_repo('miltonjdaz/{reposname}'.format(reposname=repos))
    newobj = repos_obj.get_commits()
    tc = newobj.totalCount
    return tc

repos_list = ['learning_py', 'Runescape', 'REST_API_project']
total_count = []
for i in repos_list:
    total_count.append(get_data(i))
print(total_count)

# Making the bar graph
objects = ('learning_py', 'Runescape', 'REST_API_project')
y_pos = np.arange(len(objects))
performance = [total_count[0], total_count[1], total_count[2]]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)

plt.ylabel('Number of Commits')
plt.xlabel('The Repositories')
plt.title('Total Number of Commits in Each Repository')
plt.show()

# import ipdb; ipdb.set_trace()