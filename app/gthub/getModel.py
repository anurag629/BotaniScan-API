from github import Github

from github import Auth

auth = Auth.Token('access_token')

g = Github(auth=auth)

repo = g.get_repo("anurag629/BotaniScan-API")

print(repo.stargazers_count)