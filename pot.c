#include <stdio.h>
#include <math.h>

int main(){
int a,i,j;

scanf("%d",&a);

int b[a];
long int new=0;
for ( i = 0; i < a; i++)
{
    scanf("%d",&b[i]);

}

int lastDigit[a];
for ( i = 0; i < a; i++)
{
    lastDigit[i] =b[i] %10;
   
}
for(i = 0 ;i <a;i++){
    b[i]=b[i]/10;
}

for ( i = 0; i < a; i++)
{
    
    new += pow(b[i],lastDigit[i]);
}
printf("%ld",new);


}