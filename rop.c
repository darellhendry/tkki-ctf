

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

void print_flag(int p1)
{
	FILE *fd = fopen("flag.txt", "r");
	if(p1 == 0x31030408)	{
		char flag[100];
		fgets(flag, 100, fd);
		printf("%s\n", flag);
		exit(0);
	}

	puts("<3");
}

void vuln()	{
	char buf[8];
	gets(buf);
}

int main(int argc, char const *argv[])
{
	
	setvbuf(stdout, NULL, _IONBF, 0);

	puts("Call the print_flag function with the required arguments");
	puts("Param1: 0x31030408");

	vuln();
	
	return 0;
}
