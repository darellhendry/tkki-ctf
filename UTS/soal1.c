#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int check_password(char *input) {
	int auth_flag = 0;
	char password_buffer[9];
	char password[9];
	FILE *fp;

	fp = fopen("./password.txt", "r");
	fgets(password, 9, (FILE*)fp);
	
	strcpy(password_buffer, input);
	
	if(strcmp(password_buffer, password) == 0)
		auth_flag = 0x42424141;

	return auth_flag;
}

int main(int argc, char *argv[])
{
    setvbuf(stdout, NULL, _IONBF, 0);
    char buf[10]; 
    puts("Masukkan password: ");
    gets(buf);
	
    if(check_password(buf) == 0x42424141)
        system("cat flag.txt");
    else
        puts("Wrong password!");
    return 0;
}
