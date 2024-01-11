#include<stdio.h>
int main()
{
    int a, s,i, j;
    scanf("%d", &s);
    for(i =1; i<=s ;++i)
    {
        for(j=1;j<=i;++j)
        {
            printf("*");
        }
        printf("\n");
    }  
    return 0;
}