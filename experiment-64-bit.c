

#include<stdio.h>
#include<stdlib.h>

void target(long long p1, long long p2)	{
	FILE* fp;
	char* buf = malloc(100);
	if(p1 == 0x1234567890abcdef)
		fp = fopen("flag.txt", "r");
	if(p2 == 0xfedcba0987654321)	{
		fgets(buf, 100, fp);
		puts(buf);
	}
}

void vuln()	{
	char buf[8];
	gets(buf);
}

int main(int argc, char const *argv[])
{
	setvbuf(stdout, NULL, _IONBF, 0);

	

	target(0x1234567890abcdef, 0xfedcba0987654321);
	return 0;
}