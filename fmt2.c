#include <stdio.h>

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);

    char flag[64];
    FILE *f = fopen("flag.txt","r");
    fgets(flag,64,f);

    char name[64];
    printf("What's your name?\n");
    fgets(name, sizeof(name), stdin);
    printf("Hello, ");
    printf(name);
    printf("\n");

    return 0;
}

