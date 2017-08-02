#include <stdio.h>
int main(void)
{
    int num = 12345;
    int new_num = 0;
    while(num > 0)
    {
            new_num = new_num*10 + (num % 10);
            num = num/10;
    }
    printf("%d\n",new_num);
}

