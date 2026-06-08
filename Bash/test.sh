echo $0
touch ansfile
echo $(./$1 $2) > ansfile
cat ansfile