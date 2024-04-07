# assignment04-github.py
# By Joanne Feeney
# In this assignment I will write a program in python that will read a file from a repository, 
# The program should then replace all the instances of the text "Andrew" with your name. 
# The program should then commit those changes and push the file back to the repository.

from config import config as cfg 
import requests
import json
from github import Github

# Defining function to replace Andrew with Joanne
def replace_andrew(file_content, old_text, new_text):
    return file_content.replace(old_text, new_text)

# GitHub api key & path to the .txt file
apikey = cfg["githubkey"] 
repo_name = 'joannefeeney/wsaa-private-repo'
# Path to the file
file_path = 'wsaa-assignment04/andrew_scott.txt' 

# Installed PyGithub on cmd line and using it to get apikey
g = Github(apikey) 

# Defining variables
old_text = 'Andrew'
new_text = 'Joanne'

# Getting my private repo & file andrew_scott.txt
repo = g.get_repo(repo_name)
file = repo.get_contents(file_path)
# Need to decode the .txt file as utf-8 so there are no foreign characters causing issues
# https://stackoverflow.com/questions/13110629/decoding-utf-8-strings-in-python
# https://stackoverflow.com/questions/61930537/what-does-decodeutf-8-mean-when-scraping-csv-from-website
file_content = file.decoded_content.decode('utf-8')

# Defining main function for replacing text
def main():
    # Replace text
    new_file_content = replace_andrew(file_content, old_text, new_text)
    # Commit and push changes - some of this was done with help from lecture code in week 05
    repo.update_file(file_path, f"Replace {old_text} with {new_text}", new_file_content, file.sha)
    print("Text replaced and file pushed to repo")

# Check if script being run as main 
if __name__ == "__main__":
    main()