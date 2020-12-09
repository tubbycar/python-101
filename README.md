## **Modified Exercise from the Six Degrees of Kevin Bacon Algorithmic Puzzle**

**_(This exercise was authored by faculty members of the Singapore Management University)_**

You are given a file called “friends.txt” that stores people who are friends with each other. Each line of the file contains two people’s names separated by a tab. These two people are friends with each other.

###### Part (a)

Write a program that does the following. The program prompts the user for a person’s name. Call this person X. The program then prompts the user for an integer between 1 and 6. Call this number n. The program then displays all people who are within n-degrees of separation from X. You can assume that X has at least one friend, i.e., X has appeared in the file “friends.txt.”

For example, suppose the file contains the following data:
A	B
A	C
A	D
B	C
B	E
C	D
C	F
D	G
F	G

•	Example #1: If X is E and n is 1, then the program should display only B because 1-degree separation means direct friends. 

•	Example #2: If X is E and n is 2, then the program should display A, B and C. This is because B is 1-degree separated from E, while A and C are 2-degree separated from E.

•	Example #3: If X is E and n is 3, then the program should display A, B, C, D and F. This is because in addition to A, B and C, now D and F are 3-degree separated from E, and therefore should be added.

###### Part (b)

Change the program above so that when X and n are given, the program prints out those people who are exactly n-degree separated from X.
