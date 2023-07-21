#include "helpers.h"
#include <math.h>
#include <stdlib.h>

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

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE img[height][width];
    RGBTRIPLE block[3][3];

    // make copy of image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            img[i][j] = image[i][j];
        }
    }

    // initialize the surrounding pixels array as 0
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            block[i][j].rgbtRed = 0;
            block[i][j].rgbtBlue = 0;
            block[i][j].rgbtGreen = 0;
        }
    }



    float GxR, GxB, GxG, GyR, GyB, GyG;

    float x[3][3] =
    {
        {-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}
    };

    float y[3][3] =
    {
        {-1, -2, -1}, {0, 0, 0}, {1, 2, 1}
    };

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            GxR = GxB = GxG = GyR = GyB = GyG = 0;
            int a, b;
            a = 0;

            // get the surrounding pixels
            for (int k = i - 1; k <= i + 1; k++)
            {
                b = 0;
                for (int l = j - 1; l <= j + 1; l++)
                {
                    // ignore out of bounds pixels
                    if (k >= 0 && k < height && l >= 0 && l < width)
                    {
                        // store the surrounding pixels in an array
                        block[a][b] = img[k][l];
                    }
                    b++;
                }
                a++;
            }

            // get the gx and gy for each red, blue and green pixel
            for (int c = 0; c < 3; c++)
            {
                for (int d = 0; d < 3; d++)
                {
                    GxR += x[c][d] * block[c][d].rgbtRed;
                    GxB += x[c][d] * block[c][d].rgbtBlue;
                    GxG += x[c][d] * block[c][d].rgbtGreen;

                    GyR += y[c][d] * block[c][d].rgbtRed;
                    GyB += y[c][d] * block[c][d].rgbtBlue;
                    GyG += y[c][d] * block[c][d].rgbtGreen;
                }
            }

            // convert the pixels
            image[i][j].rgbtRed = size(round(sqrt((GxR * GxR) + (GyR * GyR))));
            image[i][j].rgbtBlue = size(round(sqrt((GxB * GxB) + (GyB * GyB))));
            image[i][j].rgbtGreen = size(round(sqrt((GxG * GxG) + (GyG * GyG))));
        }
    }

    return;
}

// function the size of value and return appropriate value
int size(int a)
{
    if (a > 255)
    {
        return 255;
    }
    else if (a < 0)
    {
        return 0;
    }
    else
    {
        return a;
    }
}
