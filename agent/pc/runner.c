#include <stdio.h>
#include <signal.h>
#include <unistd.h> 


#define RUN      1
#define STOP    -1

static volatile int keep_running = RUN;


void int_handler(int dummy)
{
    (void)dummy;
    keep_running = STOP;
}


int main()
{
    unsigned long counter = 0;

    signal(SIGINT, int_handler);

    while (keep_running != STOP)
    {
        counter++;
        printf("Counter %lu\n", counter);
        fflush(stdout);
        sleep(1);
    }
    
    return 0;
}
