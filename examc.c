#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main()
{
int i,j;
int Data[15];


for(i=0;i<15;i++){
	Data[i]=i*i;
	printf("%d\n",Data[i]);
}

printf("\n\n");

for(i=14;i>=0;i--){
	printf("%d\n",Data[i]);
}

printf("\n\n");

srand(time(NULL));
for(i=0;i<15;i++){
	Data[i]=rand() % 99;
	printf("%d ",Data[i]);
}

printf("\n\n");

j=0;
while ( j < 15 ) { // While x is less than 15 
    printf("%d ",Data[j]);
    j++;             // Update x so the condition can be met eventually
}


int *data = malloc(j*sizeof(int));
printf("Array length \n");
scanf("%d",&j);

for(i=0;i<j;i++){
	data[i]=i*i;
	printf("%d\n",data[i]);
}


return 0;

}

