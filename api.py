# Not currently used in main.py due to html formatting issues

import requests

class GithubAPI():

    url = 'https://api.github.com/'

    def __init__(self, token, owner):
        self.session = requests.Session()
        self.session.headers['Authorization'] = 'Bearer ' + token
        self.owner = owner

    def get_readme(self, repo_name):
        self.session.headers['Accept'] = 'application/vnd.github.html+json'
        return self.session.get(self.url + 'repos/' + self.owner + '/' + repo_name + '/readme')
        
    def get_starred_repo_names(self):
        self.session.headers['Accept'] = 'application/vnd.github+json' 

        repo_names = []
        for repo in self.session.get(self.url + 'users/' + self.owner + '/repos').json():
            if repo['stargazers_count'] > 0:
                repo_names.append(repo['name'])
        
        return repo_names[::-1] # Reverse list for now to show robot project first

