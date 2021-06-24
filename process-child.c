#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


int main() {
    int x = 0;
    printf("PID = %d\n", getpid());
    while (1) {
        printf("Inicio %d\n", x);

        int pid = 0, status = 0;
        if ((pid=fork()) == -1) {
            printf("Error al crear proceso hijo\n");
            //exit(1);
        }

        if (pid==0) { // Proceso hijo
            printf("El PID de mi proceso padre es %d\n", getpid());
            //exit(1);
        } else {
            printf("Mi PID es el %d y he creado un proceso hijo cuyo pid es %d\n", getpid(), pid);
            wait(&status);
            printf("\nEl proceso hijo finalizo con el estado %d\n", status);
            //exit(0);
        }

        x = x+1;
        sleep(2);
    }
    return 0;
}


