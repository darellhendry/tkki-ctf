

#include<stdio.h>
#include<stdlib.h>

void vuln()	{
	char buf[8];
	gets(buf);
}

int main(int argc, char const *argv[])
{

	setvbuf(stdout, NULL, _IONBF, 0);
	puts("Tujuan kalian adalah mencari 3 digit terakhir (dalam hex) dari address fungsi puts, setvbuf, dan gets");
	puts("Libc yang digunakan aku rahasiakan");
	puts("Silakan menggunkan fungsi puts untuk mencetak address-addressnya o_O");
	puts("Good luck all!");

	vuln();
	return 0;
}