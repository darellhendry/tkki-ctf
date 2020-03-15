


#define _GNU_SOURCE     /* for RTLD_NEXT */
#include<dlfcn.h>
#include<stdio.h>
#include<stdlib.h>

char *str = "/bin/sh";

void vuln()	{
	char buf[8];
	gets(buf);
}

int main(int argc, char const *argv[])
{
	setvbuf(stdout, NULL, _IONBF, 0);

	puts("Kali ini, kalian harus panggil fungsi system dengan parameter /bin/sh");
	puts("Contoh: system(\"/bin/sh\");");
	printf("Karena aku baik, maka aku telah sediakan string /bin/sh di address %p\n", str);
	printf("Ini masih permulaan ret2libc, maka aku juga sediakan address dari fungsi puts: %p, ingat bahwa ini bukan address system\n", dlsym(RTLD_NEXT, "puts"));
	puts("Ok sekarang laksanakan ret2libcnya :)");

	vuln();
	return 0;
}