echo $0
if [ $# -ne 3 ]
then 
echo "Неверное количество аргументов!"
exit
fi
if [ ! -e $1 ]
then
echo "Неверный тип первого аргумента или такого файла не существует!"
exit
fi
if [ ! -d $2 ]
then
echo "Неверный тип второго аргумента или такого каталога не существует!"
exit
fi
if [ ! -d $3 ]
then
echo "Неверный тип третьего аргумента или такого каталога не существует!"
fi

rm fullfile
rm ansfile
touch ansfile
touch fullfile
cor=0
inc=0

Testdir=$(ls $2)
Ansdir=$(ls $3)

for name in $Testdir:
do
    echo Result of $name is >> fullfile
    echo $(./$1 $2/$name) >> fullfile
    echo $(./$1 $2/$name) > ansfile
    echo Ans of $name is >> fullfile
    cat $3/$name >> fullfile
    differ=$(cmp -b ansfile $3/$name)
    echo $differ >> fullfile
    if [ -z "differ" ]
    then
        echo "$name прошёл тест успешно" >> fullfile
        cor=$((cor+1))
    else
        echo "$name не прошёл тест" >> fullfile
        inc=$((inc+1))
    fi
done

echo "correct $cor" >> fullfile
echo "incorrect $inc" >> fullfile
