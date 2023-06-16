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


    // print out # 2 adjacent pyramids
    for (int i = 1; i < height + 1; i++)
    {
        // print out spaces
        for (int k = height; k > i; k--)
        {
            printf(" ");
        }

        // print out first pyramid
        for (int j = 0; j < i; j++)
        {
            printf("#");
        }


        // print out gap betwee the pyramids
        for (int k = 0; k < 1; k++)
        {
            printf("  ");
        }

        // print out the second pyramid
        for (int n = 0; n < i; n++)
        {
            printf("#");
        }

        printf("\n");


    }
}