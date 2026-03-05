##how to push code
## git config --global user.email "youremail@gmail.com"
## git config --global user.name "YourName"

##now initialize the repo
## git init
## git remote add origin https://github.com/yourusername/your-repo-name.git

##if switching to another repo
## git remote set-url origin https://github.com/yourusername/new-repo-name.git

##Every time you want to push code, just run these 3 commands:
## git add .
## git commit -m "added tuple practice code"
## git push origin main

##if readme file add in repo then terminal might show error its bcz the file name is not matching so run this command after the above one

## git config pull.rebase false
## git pull origin main --allow-unrelated-histories
##press esc button then :wq
##git push origin main