#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> //Header file for sleep(). man 3 sleep for details.
#include <pthread.h>


// A normal C function that is executed as a thread
// when its name is specified in pthread_create()
void *myThreadFun(void *vargp)
{
    sleep(1);
    printf("Printing from myThreadFun\n");
    //sleep(1);
    return NULL;
}

void *myThreadCalc(void *vargp)
{
    int i = 0;
    for (i = 1; i <= 10; ++i) {
        printf("%d ", i);
    }
    printf("Printing from myThreadCalc %d\n", i);
    return NULL;
}


int main()
{
    pthread_t thread_fun_id;
    pthread_t thread_calc_id;

    printf("Before Threads\n");

    pthread_create(&thread_fun_id, NULL, myThreadFun, NULL);
    pthread_create(&thread_calc_id, NULL, myThreadCalc, NULL);

    pthread_join(thread_fun_id, NULL);
    pthread_join(thread_calc_id, NULL);

    printf("After Threads\n");

    exit(0);
}

