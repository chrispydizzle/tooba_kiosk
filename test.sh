source migrationcount
echo $GNUM
lent=${#GNUM}
echo $lent
if [ "$lent" == "1" ]; then
	MIGR="000$GNUM"
	echo $MIGR
fi
if [ "$lent" == "2" ]; then
	MIGR="00$GNUM"
	echo $MIGR
fi
if [ "$lent" == "3" ]; then
	MIGR="0$GNUM"
	echo $MIGR
fi
if [ "$lent" == "4" ]; then
	MIGR="$GNUM"
	echo $MIGR
fi

