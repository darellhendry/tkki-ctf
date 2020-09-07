

#include<stdio.h>
#include<stdlib.h>

char* containers[5];

void init()	{
	setvbuf(stdout, NULL, _IONBF, 0);
}

void print_menu()	{
	puts("==================================================");
	puts("                 Shellcode Maker                  ");
	puts("==================================================");
	puts(" 1. Create Shellcode");
	puts(" 2. Delete Shellcode");
	puts(" 3. Exit");
	puts("==================================================");
	printf("Your Choice: ");
}

int read_int()	{
	char buf[5];
	fgets(buf, 5, stdin);
	return atoi(buf);
}

void create_shellcode()	{
	int index, size;

	printf("Index: ");
	index = read_int();
	if(index > 4)	{
		puts("Out of bounds!");
		return;
	}

	printf("Size: ");
	size = read_int();
	containers[index] = malloc(size);
	printf("Data: ");
	fgets(containers[index], size, stdin);
	puts("Done!");

	return;
}

void delete_shellcode()	{
	int index;

	printf("Index: ");
	index = read_int();
	if(index > 4)	{
		puts("Out of bounds!");
		return;
	}

	free(containers[index]);
	containers[index] = 0;
	puts("Done!");
	return;
}

int main(int argc, char const *argv[])
{
	init();
	while(1)	{
		print_menu();
		unsigned int choice = read_int();
		switch(choice)	{
			case 1:
				create_shellcode();
				break;
			case 2:
				delete_shellcode();
				break;
			case 3:
				exit(0);
		}
	}
	return 0;
}