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

/* Explanation:
This program is similar to the previous one, but it also checks if the hand has a value of 21 and prints "Blackjack!" if it does.
The program loops through each character in the hand string until it reaches the null terminator '\0', and adds the point value of each card to a variable called points. It also keeps track of the number of Aces using a variable called aces.
If the card is an Ace, the program increments aces and adds 11 points to points.
If the card is a face card (10, J, Q, or K), the program adds 10 points to points.
If the card is a number card (2-9), the program subtracts the ASCII code of '0' (48) from the card character code to get the numerical value of the card, and adds that to points.
After the loop, the program checks if the hand has a sum greater than 21 and if there are any Aces worth 11 points. If both conditions are true, the program converts one Ace to 1 point and subtracts 10 from the points. It repeats this process until there are no Aces worth 11 points or the sum of points is less than or equal to 21.
Finally, the program checks if the value of points is 21 and prints "Blackjack!" if it is, or the sum of points otherwise.
 */



