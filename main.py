from GitHubRepo import GithubRepoCreator
github_task = GithubRepoCreator(
    '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', 'https://api.github.com/orgs')
github_task.create_repo('<your repo goes here>', 'test')

