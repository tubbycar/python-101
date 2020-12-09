## **Modified Exercise from the Six Degrees of Kevin Bacon Algorithmic Puzzle**

**_(This exercise was authored by faculty members of the Singapore Management University)_**

**_(In this repository, I have put forth two naive solutions)_**

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

## **Polynomial Multiplication Script**

**_(This exercise was authored by faculty members of the Singapore Management University)_**

**_(In this repository, I have put forth a naive solution)_**

Implement a function called multiply(). This function takes 1 parameter:

● polynomials (type: list): This is a list of lists, where each list inside polynomials represents the coefficients of a single-variable polynomial such as −2𝑥^2+3𝑥+1 . (This means you will NOT see polynomials with more than one variable such as 2𝑥𝑦+3𝑥+5 .)

Each polynomial is represented as a list of the form [an, an-1, an-2, …, a2, a1, a0], where an is the coefficient of 𝑥^𝑛, an-1 is the coefficient 𝑥𝑛−1, and so on. You can assume that the list consists of all the coefficients of the polynomial (i.e., coefficients of all individual terms including the zero value coefficients as shown in the third illustration below). You can also assume that all coefficients are integers.

For example,

○ [2, 6] represents the polynomial 2𝑥+6.

○ [-2, 3, 1] represents the polynomial −2𝑥^2+3𝑥+1.

○ [5, 0, 3, 7] represents the polynomial 5𝑥^3+3𝑥+7.

Note: 

• The list representing a polynomial will NOT be empty. 

• The first element of the list will not be 0 (e.g., 2𝑥+6 will not be represented as [0, 2, 6]), except for the special case when we represent a zero polynomial; in the case of a zero polynomial, we use [0] (a list with a single element 0 inside) to represent it.

The parameter polynomials is a list of polynomials. E.g., if polynomials is [ [2, 6] , [-2, 3, 1], [5, 0, 3, 7] ], it represents the following list of polynomials: [ 2𝑥+6 , −2𝑥^2+3𝑥+1 , 5𝑥^3+3𝑥+7 ] .

This function returns a list that represents coefficients of the resultant polynomial after multiplying all the polynomials in the given list polynomials.

To multiply 2 polynomials, multiply each term in the first polynomial by each term in the second polynomial. 

For example,(x^2+2x+3)(5𝑥^2+6𝑥+7)=x^2(5x^2+6x+7)+2x(5x^2+6x+7)+3(5x^2+6x+7)=(5𝑥^4+6𝑥^3+7𝑥^2)+(10𝑥^3+12𝑥^2+14𝑥)+(15𝑥^2+18𝑥+21)=5x^4+16x^3+34x^2+32x+21

Note:

• You can assume that the list polynomials always contains at least one element.

• If the result is a zero polynomial, the function should return [0] (rather than [0, 0], [0, 0, 0], etc.).
