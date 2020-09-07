

#include<stdio.h>
#include<stdlib.h>

int global_cookie;

void init()	{
	setvbuf(stdout, NULL, _IONBF, 0);
	FILE *fp;
	fp = fopen("/dev/urandom", "r");
	fread((char *)(&global_cookie), 1, 4, fp);
	fclose(fp);
}

void vuln()	{
	int local_cookie = global_cookie;
	char buf[100];
	char choice[5];
	while(1)	{
		printf("Enter a testimony (max 100 characters): ");
		gets(buf);
		printf("Your testimony: ");
		printf(buf);
		printf("Would you like to enter another testimony (y/n)? ");
		fgets(choice, 5, stdin);
		if(choice[0] != 'y')
			break;
	}
	if(global_cookie != local_cookie)	{
		printf("You bad-bad try buffer overflow! >:(");
		exit(-1);
	}
	printf("Thank you!");
	return;
}

int main(int argc, char const *argv[])
{
	init();
	puts("Karena materi binex udah selesai, ini aku kasih soal yang competition-like");
	puts("Vuln yang ada di soal ini adalah bof dan format string, good luck!");
	vuln();
	return 0;
}