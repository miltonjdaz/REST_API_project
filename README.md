Scripting a REST API Data Pipeline
Exporting GitHub commits using REST APIs and displaying which repository has the most commits

For my third project, I wanted to visualize the total number of commits for each of my repositories in my GitHub account by using REST APIs. I was especially excited about diving into what REST APIs have to offer using “import ipdb; ipd.set_trace()”. When I had this project in mind, I envisioned that I would need to connect to PostgreSQL, have multiple CSV files, and multiple graphs. However, as I worked on the project, I realized I needed to modify the project. 

In the first draft of the project, I thought I needed to connect to PostgreSQL. By connecting to PostgreSQL, I would write a SQL command to figure out the total number of commits in each repository by using COUNT(). However, I realized that I achieved the same result by using a for loop. Therefore, I realized there was no reason to connect to PostgreSQL. 

After successfully creating the for loop, I made a dataframe and connected the number of commits to a CSV file. I repeated the process two more times since I have three repositories. After each CSV file was created, I used a 2nd Python script in order to make graphs from the data. After making graphs for each of the three CSV files, I had this strange feeling of not being excited and happy with the results. I decided to table the results for now and created a 2nd draft in order to figure out if there was a better method in completing this project. 

The 2nd draft of the project is broken down into 3 parts: a function to get the total count of commits in each repository, creating a list with appending the number of commits, and making the bar graph. The following lines of code replaces about 30 lines of code that completes the same thing: 

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
Since I needed the total number of commits for each of the three repositories, it is better to create a function to complete the task. The REST APIs that I used were get_repo which gets the repository from GitHub, get_commits() which retrieves the number of commits in the repository, and totalCount which returns the total number of commits in the repository. Since I had the total number of commits for each repository in one location, I did not need a for loop nor the CSV files. 

The 2nd part of the Python script, I created a list and appended the number of commits for each repository: 

repos_list = ['learning_py', 'Runescape', 'REST_API_project']
total_count = []

for i in repos_list:
   total_count.append(get_data(i))

print(total_count) 
Just 5 lines of code replaces about 25 lines of code in the first draft. Again, I want to emphasize that if you are working on a project, the end result can be different from what was envisioned at the beginning.

For the 3rd part, I made a bar graph from the data that is located in total_count: 

objects = ('Runescape', 'learning_py', 'REST_API_project')
y_pos = np.arange(len(objects))
performance = [total_count[0], total_count[1], total_count[2]]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)

plt.ylabel('Number of Commits')
plt.xlabel('The Repositories')
plt.title('Total Number of Commits in Each Repository')
plt.show()
The final result is one graph showing the number of commits for each repository. 


As you can see, there are significantly more commits in my learning_py repository compared to the other two. I am happy that the results are all in one graph so it is easier to compare the total number of commits for each repository. Once I saw this graph, I felt the same feeling of accomplishment that I felt when I completed the Runescape project. I am happy that I decided to modify my project as time went on. Less than 40 lines of code brings a better result than 2 Python scripts and 3 CSV files. It is important to be flexible with projects otherwise you will not find the best solution.

