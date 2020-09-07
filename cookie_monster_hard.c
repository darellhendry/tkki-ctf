

#include<stdio.h>
#include<stdlib.h>

int global_cookie;

void init_global_cookie()	{
	FILE *fp;
	fp = fopen("/dev/urandom", "r");
	fread((char *)(&global_cookie), 1, 4, fp);
	fclose(fp);
}

void init()	{
	setvbuf(stdout, NULL, _IONBF, 0);
}

void vuln()	{
	int local_cookie;
	char buf[100];
	char choice[5];
	while(1)	{
		init_global_cookie();
		local_cookie = global_cookie;
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
	puts("Ini cookie monster yang hard, ada tambahan PIE dan cookie berubah selalu.");
	puts("Vulnnya sama, bof dan format string, good luck!");
	puts("Sebenarnya kalo udah dapat soal ini, bisa reuse-exploit untuk soal yang easy version");
	vuln();
	return 0;
}