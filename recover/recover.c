#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef uint8_t BYTE;
const int size = 512;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // declare variables
    BYTE buffer[size];
    int n = 0;
    char *name = malloc(8);
    FILE *output = NULL;

    while (fread(&buffer, 1, size, input))
    {
        // chceck for jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            // close files
            if (n != 0)
            {
                fclose(output);
            }

            // create new files
            sprintf(name, "%03i.jpg", n);
            output = fopen(name, "w");

            n++;
        }

        // write into file
        if (output != NULL)
        {
            fwrite(&buffer, 1, size, output);
        }
    }
    free(name);
    fclose(input);
    fclose(output);
}