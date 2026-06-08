#include "prim.h"

DataTime setCurrentTime() {
	long int a;
	a = time(NULL);
	DataTime * mtime;
	mtime = localtime(&a);
	return *mtime;
}

void printWeekDay(DataTime a) {
    if (a.tm_wday == 1) {
        printf("понедельник\n");
    }
    else if (a.tm_wday == 2) {
        printf("вторник\n");
    }
    else if (a.tm_wday == 3) {
        printf("среда\n");
    }
    else if (a.tm_wday == 4) {
        printf("четверг\n");
    }
    else if (a.tm_wday == 5) {
        printf("пятница\n");
    }
    else if (a.tm_wday == 6) {
        printf("суббота\n");
    }
    else if (a.tm_wday == 7) {
        printf("воскресенье\n");
    }
}

DataTime getTime(char* a){
    int dig[7];
    DataTime res;
    char s[3] = "";
    s[0] = a[0];
    s[1] = a[1];
    time_t tt = atoi(s);
    res.tm_year = tt;
    s[0] = a[3];
    s[1] = a[4];
    res.tm_mon = atoi(s);
    s[0] = a[6];
    s[1] = a[7];
    res.tm_mday = atoi(s);
    s[0] = a[9];
    s[1] = a[10];
    res.tm_hour = atoi(s);
    s[0] = a[12];
    s[1] = a[13];
    res.tm_min = atoi(s);
    s[0] = a[15];
    s[1] = a[16];
    res.tm_sec = atoi(s);
    return res;
}

DataTime after(char* s) {
    DataTime * res;
    char k[3];
    time_t t = time(NULL);
    k[0] = s[9];
    k[1] = s[10];
    t += atoi(k); //sec

    k[0] = s[6];
    k[1] = s[7];
    t += atoi(k) * 60; //min

    k[0] = s[3];
    k[1] = s[4];
    t += atoi(k) * 3600;//hour

    k[0] = s[0];
    k[1] = s[1];
    t += atoi(k) * 3600 * 24;//day

    res = localtime(&t);

    return *res;
}

DataTime before(char * s) {
    DataTime *res;
    time_t t = time(NULL);
    char k[3];

    k[0] = s[9];
    k[1] = s[10];
    t -= atoi(k); //sec

    k[0] = s[6];
    k[1] = s[7];
    t -= atoi(k) * 60; //min

    k[0] = s[3];
    k[1] = s[4];
    t -= atoi(k) * 3600;//hour

    k[0] = s[0];
    k[1] = s[1];
    t -= atoi(k) * 3600 * 24;//day

    res = localtime(&t);

    return *res;
}

void addTm(Timer * a, const Timer * b) {
    a->dd += b->dd;
    a->hh += b->hh;
    a->min += b->min;
    a->nano += b ->nano;
    a->sec += b->sec;

    if (a->nano > 999) {
        a->sec += 1;
        a->nano -= 1000;
    }
    if (a->sec > 59) {
        a->min += 1;
        a->nano -= 60;
    }
    if (a->min > 59) {
        a->hh += 1;
        a->min -= 60;
    }
    if (a->hh > 23) {
        a->dd += 1;
        a->hh -= 24;
    }
}

void minusTm(Timer * a, const Timer * b) {
    a->dd -= b->dd;
    a->hh -= b->hh;
    a->min -= b->min;
    a->nano -= b ->nano;
    a->sec -= b->sec;

    if (a->nano < 0) {
        a->min -= 1;
        a->nano += 1000;
    }
    if (a->sec < 0) {
        a->min -= 1;
        a->sec += 60;
    }
    if (a->min < 0) {
        a->hh -= 1;
        a->min += 60;
    }
    if (a->hh < 0) {
        a->dd -= 1;
        a->hh += 24;
    }
}

DataTime plusTimer(DataTime a, const Timer* b) {
    a.tm_sec += b->sec;
    a.tm_min += b->min;
    a.tm_hour += b->hh;
    a.tm_mday += b->dd;
    if (a.tm_sec > 59) {
        a.tm_min += 1;
        a.tm_sec -= 60;
    }
    if (a.tm_min > 59) {
        a.tm_hour += 1;
        a.tm_min -= 60;
    }
    if (a.tm_hour > 23) {
        a.tm_mday += 1;
        a.tm_hour -= 24;
    }
    return a;
}

void showTimer(const Timer* a) {
    printf("%0.2lld %0.2d:%0.2d:%0.2d", a->dd, a->hh, a->min, a->sec);
}

Timer startTime(){
    struct timespec mt1;
    clock_gettime(CLOCK_REALTIME, &mt1);
    time_t tt = mt1.tv_sec;
    DataTime * a = localtime(&tt);
    Timer b;
    b.dd = a->tm_mday + 365 * a->tm_year;
    b.hh = a->tm_hour;
    b.min = a->tm_min;
    b.sec = a->tm_sec;
    b.nano = mt1.tv_nsec;
    return b;
}

Timer* stopTime(Timer* b) {
    struct timespec mt1;
    clock_gettime(CLOCK_REALTIME, &mt1);
    time_t tt = mt1.tv_sec;
    DataTime * a = localtime(&tt);
    b->dd = a->tm_mday + 365 * a->tm_year;
    b->hh = a->tm_hour;
    b->min = a->tm_min;
    b->sec = a->tm_sec;
    b->nano = mt1.tv_nsec;
    return b;
}

Timer getTimer(long long dd, int hh, int min, int sec, int nano){
    Timer a = {dd, hh, min, sec, nano};
    return a;
}

