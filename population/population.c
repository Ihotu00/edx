#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start = 0;
    while (start < 9)
    {
        start = get_int("What is the population start size? ");
    }

    // TODO: Prompt for end size
    int stop = 0;
    while (stop < start)
    {
        stop = get_int("What is the population stop size? ");
    }

    // TODO: Calculate number of years until we reach threshold
    int year = 0;
    for (int y = 1; start < stop; y++)
    {
        start = start + start / 3 - start / 4;
        year = y;
    }


    // TODO: Print number of years
    printf("Years: %i\n", year);

}
