#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);


int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int word = count_words(text);
    printf("%i, %i\n ", letters, word);
}

int count_letters(string text)
{
    int letters = 0;
   int l = strlen(text);
   for (int i = 0; i < l; i++)
   {
        if isalpha(text[i])
        {
            letters++;
        }

   }
   return letters;

}

int count_words(string text)
{
    int word = 0;
    int l = strlen(text);
    for (int i = 0; i < l; i++)
    {
        if isspace(text[i])
        {
            word++;
        }
    }
    return word;
}

