#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

// int strlength(string text);


int main(void)
{
    string text = get_string("Text: ");
    int len = strlen(text);
    printf("%i\n", len);
}

int strlength(string text)
{
    
}