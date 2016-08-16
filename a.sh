git checkout aaa
echo "." >> a.txt
git commit -am "woot"
git checkout master
git merge aaa
