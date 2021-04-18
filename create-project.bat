@echo off
your directory with projects
create.py %1
cd %1
echo > README.md
git init
git remote add origin https://github.com/username/%1.git
git add .
git commit -m "init"
git push -u origin main
code .