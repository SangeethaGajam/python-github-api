import requests
import json

class GithubRepoCreator:

    #token = ''
    #github_url = ''

    def __init__(self,  login_token, the_github_url):
        self.token = login_token
        self.github_url = the_github_url

    def create_repo(self, org, repo_name):
        repodetails = {"name": repo_name}
        url = self.github_url + "/" + org + "/repos"
        headers_details = {'Authorization': 'token ' +
                           self.token, "Accept": "application/vnd.github.v3+json"}
        print('Creating Repo for url :: ' + url)
        print(repodetails)
        print(headers_details)
        response = requests.post(url=url, data=json.dumps(repodetails), headers=headers_details, verify=False)
        print(response.status_code)
        print(response.content);
