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
    float grade = 0.0588 * (letters / word * 100) - 0.296 * (sentence / word * 100) - 15.8;
    if grade > 1 && grade < 16
    {
        printf("Grade\n", grade);
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade 16+\n");
    }
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
        if isalpha(text[i])
        {
            if isspace(text[i + 1])
            {
                word++;
            }
            else if (ispunct(text[i + 1]))
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
                sentence++;
        }
    }
    return sentence;
}