#include <cs50.h>
#include <stdio.h>

int length(long card);
int check1(long card);
int check2(long card);
int initial_digits(long card);

int main(void)
{
    long card = get_long("Enter number: ");
    int chksm = (check1(card) + check2(card)) % 10;
    int len = length(card);
    int first = initial_digits(card);

    // print out the corresponding output
    if (len == 15 && (first == 34 || first == 37) && chksm == 0)
    {
        printf("AMEX\n");
    }
    else if (len == 16 && (first >= 51 && first <= 55) && chksm == 0)
    {
        printf("MASTERCARD\n");
    }
    else if ((len == 13 || len == 16) && (first / 10 == 4) && chksm == 0)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

// calculate the first half of the checksum
int check1(long card)
{
    int add = 0;
    // remove last digit
    card /= 10;
    while (card >= 1)
    {
        // assigns the last digit to variable
        int digit = card % 10;
        digit *= 2;
        // removes the last two digits
        card /= 100;
        // adds each digit of the variable
        while (digit >= 1)
        {
            int mini = digit % 10;
            add += mini;
            // removes last digit
            digit /= 10;
        }
    }
    return add;
}

// calculate the second half of the check sum
int check2(long card)
{
    int add = 0;
    int digit = 0;
    while (card >= 1)
    {
        digit = card % 10;
        add += digit ;
        card /= 100;
    }
    return add;
}

// calculate the length of the input
int length(long card)
{
    int count = 0;
    while (card != 0)
    {
        card /= 10;
        count++;
    }
    return count;

}

// calculates the first two digits
int initial_digits(long card)
{
    // int initial_digits;
    while (card > 99)
    {
        // initial_digits = card % 100;
        card /= 10;
    }
    return card;
}