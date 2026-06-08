all: test

test: functions.o test.c 

	g++ test.c functions.o -o test
	
functions.o: functions.c
	g++ -c functions.c
