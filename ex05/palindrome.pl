#!/usr/bin/perl

print "Enter a string: ";
my $input = <STDIN>;
chomp $input;
$input =~ s/[^a-zA-Z0-9]//g;
$input = lc($input);
if ($input eq reverse($input)) {
	print "$input is a palindrome.\n";
} else {
	print "$input is not a palindrome.\n";
}