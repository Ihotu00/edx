#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentence(string text);


int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int word = count_words(text);
    int sentence = count_sentence(text);
    printf("%i\n%i\n%i\n", letters, word, sentence);
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
            if isalpha(text[i + 1])
            {
                word++;
            }
        }
    }
    return word;
}


int count_sentence(string text)
{
    int sentence = 0;
    int l = strlen(text);
    for (int i = 0; i < l; i++)
    {
        if ispunct(text[i])
        {
            if isspace(text[i + 1])
            {
                sentence++;
            }
        }
    }
    return sentence;
}