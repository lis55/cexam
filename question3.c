#include <stdio.h>
#include <math.h>

/////question 3e)
struct Point {
    double x, y, z;
};

///////Question 3c)

///non recursive factorial
int factorial(int n){
	int fac,i;
	fac=1;
	for (i=1;i<=n;i++)
		{
			
		fac *= i;
		}	
	return fac;
};

//recursive factorial
int factorial2(int n)
{
  if (n == 0)
    return 1;
  else
    return(n * factorial2(n-1));
}


// question 3 d)
int invernum(int num){
int new_num;
new_num=0;

    while(num > 0)
    {
            new_num = new_num*10 + (num % 10);
            num = num/10;
    }

}



int main()
{

///Question 3e) 
    struct Point a, b;
    printf("Enter coordinate of point a: ");
    scanf("%lf %lf %lf", &a.x, &a.y, &a.z);
    printf("Enter coordinate of point b: ");
    scanf("%lf %lf %lf", &b.x, &b.y, &b.z);

    double distance;
    distance = sqrt((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y) + (a.z-b.z)*(a.z-b.z));
    printf("Distance between a and b: %lf\n", distance);
///

int n;
    printf("Enter integer number to compute factorial\n");
    scanf("%d", &n);
    printf("Factorial of %d=%d \n",n,factorial(n));
    printf("Factorial of %d=%d \n",n,factorial2(n));    

    return 0;
}


