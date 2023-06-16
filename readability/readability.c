#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int count_letters(string text);


int main(void)
{
    string text = get_string("Text: ");
    int len = count_letters(text);
    printf("%i\n", len);
}

int count_letters(string text)
{
    int len = 0;
   int l = strlen(text);
   for(int i = 0; i < l; i++)
   {
        if isalpha(text[i])
            len++;
   }
   return len;

}