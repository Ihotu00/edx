#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // get the height from user
    int height = 0;
    while (height < 1 || height > 8)
    {
        height = get_int("Height: ");
         
    }


    // print out # pyramid
    for (int i = 1; i < height + 1; i++)
    {
        // print out spaces
        for (int k = height; k > i; k--)
        {
            printf(" ");
        }

        //print out #
        for (int j = 0; j < i; j++)
        {
            printf("#");
        }

        printf("\n");

    }
}