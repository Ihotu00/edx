#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int length(string text);


int main(void)
{
    string text = get_string("Text: ");
    int len = length(text);
    printf("%i\n", len);
}

int length(string text)
{
   int l = strlen(text);
   for(int i = 0; i < l; i++)
   {
        if isalnum(text[i])
            int len++;
   }
   return len;

}