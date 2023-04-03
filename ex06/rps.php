<?php
// user to select either rock, paper, or scissors (repeat until valid choice is made)
do {
	$user_choice = strtolower(readline("Enter your choice (rock, paper, or scissors): "));
} while ($user_choice != 'rock' && $user_choice != 'paper' && $user_choice != 'scissors');

// random choice for computer
$choices = ['rock', 'paper', 'scissors'];
$computer_choice = $choices[rand(0, 2)];

// who win
if ($user_choice == $computer_choice) {
	echo "It's a tie!\n";
} elseif (($user_choice == 'rock' && $computer_choice == 'scissors') ||
	($user_choice == 'paper' && $computer_choice == 'rock') ||
	($user_choice == 'scissors' && $computer_choice == 'paper')) {
	echo "You win! $user_choice beats $computer_choice\n";
} else {
	echo "Computer wins! $computer_choice beats $user_choice\n";
}
?>