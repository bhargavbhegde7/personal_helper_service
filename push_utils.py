from git import Repo

repo_dir = '/home/pi/bhargavbhegde7.github.io'
repo = Repo(repo_dir)
file_list = ['utils.html']
commit_message = 'Change ip address of pi'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()
