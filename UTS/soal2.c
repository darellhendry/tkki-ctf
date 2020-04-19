

#include<stdio.h>
#include<stdlib.h>

int main(int argc, char const *argv[])
{
	setvbuf(stdout, NULL, _IONBF, 0);

	char buf[20];
	int* var = malloc(10);
	*var = 5;

	printf("My address: %lp\n", var);
	printf("Masukan password: ");

	fgets(buf, 20, stdin);
	printf(buf);

	if(*var == 0x100)
		system("cat flag.txt");
	else
		puts("Failed!");

	return 0;
}
