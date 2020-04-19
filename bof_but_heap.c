

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct data
{	
	char *str;
	int length;
};

long long target = 0x1234;

int read_int()	{
	// Fungsi untuk membaca integer
	char buf[5];
	fgets(buf, 5, stdin);
	return atoi(buf);
}

int main(int argc, char const *argv[])
{
	setvbuf(stdout, NULL, _IONBF, 0);
	puts("Pada soal kali ini, kalian harus mengubah nilai dari target menjadi 0x00001a2b3c4d5e6f");
	printf("Target terletak di %lp\n", &target);
	puts("Gunakan heap overflow untuk menyelesaikan soal ini");
	printf("Mau berapa data? ");

	int arr_length = read_int();
	if(arr_length < 1 || arr_length > 7)	{
		puts("Invalid length. Aborting");
		exit(-1);
	}
	struct data *arr[arr_length];
	for(int i = 0; i < arr_length; i++)	{
		arr[i] = malloc(sizeof(struct data));
		arr[i]->str = malloc(32);
	}

	for(int i = 0; i < arr_length; i++)	{
		printf("Enter data at data %d (max 32 characters):\n", i);
		gets(arr[i]->str);
		arr[i]->length = strlen(arr[i]->str);
	}

	if(target == 0x00001a2b3c4d5e6f)	{
		puts("Nice job, here's your shell");
		system("/bin/sh");
	}

	return 0;
}