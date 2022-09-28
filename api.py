import requests

class GithubAPI():

    url = 'https://api.github.com/users/nicholasshort/repos'

    def __init__(self, token):
        self.session = requests.Session()
        self.session.headers['Accept'] = 'application/vnd.github+json' 
        self.session.headers['Authorization'] = 'Bearer ' + token
        print(self.session.headers)
        
    
    def get_repo_names(self):
        return self.session.get(self.url)
    


print(GithubAPI('token').get_projects().json())
