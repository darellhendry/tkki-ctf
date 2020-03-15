

#include<stdio.h>
#include<stdlib.h>

FILE* fp;
char* buf;

void target(int p1, int p2)	{
	if(p1 == 0x12345678 && p2 == 0x87654321)	{
		puts("Flag.txt opened!");
		fp = fopen("flag.txt", "r");
	}
	else if(p1 == 0xaabbccdd && p2 == 0x11223344)	{
		puts("Flag read!");
		fgets(buf, 200, fp);
	}
	else if(p1 == 0x03030808 && p2 == 0x31310404)	{
		puts("Here you go!");
		printf("%s\n", buf);
	}
}

void vuln()	{
	puts("Good luck~");
	char buf[8];
	gets(buf);
}

void init()	{
	// Jangan panggil fungsi ini lebih dari sekali!
	setvbuf(stdout, NULL, _IONBF, 0);
	buf = malloc(200);
}

int main(int argc, char const *argv[])
{

	init();
	puts("Kali ini tujuannya mengubah return address beberapa kali untuk panggil fungsi target beberapa kali dengan parameter berbeda2");

	vuln();
	return 0;
}