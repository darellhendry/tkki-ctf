

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

	puts("ROP hampir selesai, kali ini belajar 64 bit");
	puts("Ingat bahwa di 64-bit, parameter tidak disimpan di stack, melainkan di register");
	puts("Urutan register adalah rdi, rsi, rdx, rcx, r8, dan r9");
	puts("Pada soal ini, kalian hanya perlu mengubah dua parameter, dan memanggil fungsi target");
	puts("Good luck!");

	vuln();
	return 0;
}