# assignment04-github.py
# By Joanne Feeney
# In this assignment I will write a program in python that will read a file from a repository, 
# The program should then replace all the instances of the text "Andrew" with your name. 
# The program should then commit those changes and push the file back to the repository.

pip install PyGithub

from github import Github 
from config import config as cfg 

apikey = ht6Vnk["githubkey"] 
# use your own key 
g = Github(apikey) 

for repo in g.get_user().get_repos(): 
    print(repo.name) 