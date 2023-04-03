#include <stdio.h>

int main(int argc, char** argv) {
	int points = 0;
	int aces = 0;

	for (int i = 0; argv[1][i] != '\0'; i++)
	{
		char card = argv[1][i];
		if (card == 'A') {
			aces++;
			points += 11;
		}
		else if (card == 'T' || card == 'J' || card == 'Q' || card == 'K')
			points += 10;
		else
			points += card - '0';
	}

	while (points > 21 && aces > 0)
	{
		points -= 10;
		aces--;
	}

	if (points == 21)
		printf("Blackjack!\n");
	else
		printf("%d\n", points);
	return 0;
}



