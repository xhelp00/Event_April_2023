#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
	if (argc == 1) 
		return 1;
	int max_length = 0;
	for (int i = 1; i < argc; i++) {
		int len = strlen(argv[i]);
		if (len > max_length)
			max_length = len;
	}

	for (int i = 0; i < max_length + 4; i++) // 4 on top since all mid lines starts with "* " and ends with " *"
		printf("*");

	printf("\n");
	for (int i = 1; i < argc; i++)
	{
		printf("* ");
		printf("%-*s", max_length, argv[i]);  // - for left alingment, * for placeholder of width indicated as intiger before string
		printf(" *\n");
	}
	for (int i = 0; i < max_length + 4; i++)
		printf("*");
	printf("\n");
	return 0;
}




