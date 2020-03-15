

#include<stdio.h>
#include<stdlib.h>

void vuln()	{
	char buf[8];
	gets(buf);
}

int main(int argc, char const *argv[])
{
	setvbuf(stdout, NULL, _IONBF, 0);

	puts("Lagi lagi, kalian harus panggil fungsi system untuk jalanin shell");
	puts("Nah kali ini aku jahat, gaada address yang aku beri >:D");
	puts("Berarti kalian harus cari \"address leak\"");
	puts("Semangat! :)");

	vuln();
	return 0;
}