#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentence(string text);


int main(void)
{
    string text = get_string("Text: ");
    float letters = count_letters(text);
    float word = count_words(text);
    float sentence = count_sentence(text);
    // apply the Coleman-Liau index
    float grade = (0.0588 * (letters / word) * 100) - (0.296 * (sentence / word) * 100) - 15.8;
    // round grade
    grade = round(grade);
    if (grade >= 1 && grade <= 16)
    {
        printf("Grade %.f\n", grade);
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

// function to count the letters in a string
int count_letters(string text)
{
    int letters = 0;
    int l = strlen(text);
    for (int i = 0; i < l; i++)
    {
        // only count alphabtes
        if isalpha(text[i])
        {
            letters++;
        }
    }
    return letters;

}

// function to count the words in a string
int count_words(string text)
{
    int word = 1;
    int l = strlen(text);
    for (int i = 0; i < l; i++)
    {
        // count after every space
        if isspace(text[i])
        {
            word++;
        }
    }
    return word;
}


// function to count sentences in a string
int count_sentence(string text)
{
    int sentence = 0;
    int l = strlen(text);
    for (int i = 0; i < l; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentence++;
        }
    return sentence;
}