#include "helpers.h"
#include <math.h>

int size(int a);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // get gray value for each pixel
            int avg = round((image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3.0);

            // convert to gray value
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // get sepia value for each pixel
            int s_red = size(round((0.393 * image[i][j].rgbtRed) + (0.769 * image[i][j].rgbtGreen) + (0.189 * image[i][j].rgbtBlue)));
            int s_green = size(round((0.349 * image[i][j].rgbtRed) + (0.686 * image[i][j].rgbtGreen) + (0.168 * image[i][j].rgbtBlue)));
            int s_blue = size(round((0.272 * image[i][j].rgbtRed) + (0.534 * image[i][j].rgbtGreen) + (0.131 * image[i][j].rgbtBlue)));

            // convert to sepia value for each pixel
            image[i][j].rgbtRed = s_red;
            image[i][j].rgbtBlue = s_blue;
            image[i][j].rgbtGreen = s_green;
        }
    }

    return;
}

// function to check the size of value and return 255 if value exceeds it
int size(int a)
{
    if (a > 255)
    {
        return 255;
    }
    else
    {
        return a;
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        int k = width - 1;
        for (int j = 0; j < width / 2 ; j++)
        {
            // swap pixel with pixel on opposite side
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][k];
            image[i][k] = temp;
            k--;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE img[height][width];
    // make copy of image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            img[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int s_red, s_Blue, s_Green;
            float n;
            s_red = s_Blue = s_Green = n = 0;

            // get the surrounding pixels
            for (int k = i - 1; k <= i + 1; k++)
            {
                for (int l = j - 1; l <= j + 1; l++)
                {
                    // ignore out of bounds pixels
                    if (k >= 0 && k < height && l >= 0 && l < width)
                    {
                        s_red += img[k][l].rgbtRed;
                        s_Blue += img[k][l].rgbtBlue;
                        s_Green += img[k][l].rgbtGreen;
                        n++;
                    }
                }
            }

            // convert to blurred pixels
            image[i][j].rgbtRed = round(s_red / n);
            image[i][j].rgbtBlue = round(s_Blue / n);
            image[i][j].rgbtGreen = round(s_Green / n);
        }
    }

    return;
}
