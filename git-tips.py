git add ...
git commit -m "..."

git log
git log --pretty=oneline

git reset --hard HEAD^
git reset --hard HEAD^^

git reset --hard 3628164

git reflog

#git checkout -- file可以丢弃工作区的修改：
git checkout -- readme.txt

#用命令git reset HEAD file可以把暂存区的修改撤销掉（unstage），重新放回工作区：
git reset HEAD readme.txt

#从版本库中删除该文件，git rm
git rm test.txt
git commit -m "remove test.txt"

#删错了，因为版本库里还有，所以可以很轻松地把误删的文件恢复到最新版本：
#git checkout 用版本库里的版本替换工作区的版本
git checkout -- test.txt

