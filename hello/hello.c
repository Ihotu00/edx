#include<stdio.h>
#include<cs50.h>

int main(void)
{
    // accept name and output greeting
    string name = get_string("Enter name: ");
    printf("hello, %s\n", name);
}