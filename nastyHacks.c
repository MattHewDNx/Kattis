#include <stdio.h>

int main(){

int a,b,c,i,j;

scanf("%d",&a);

for ( i = 0; i <a; i++)
{
    scanf("%d %d %d",&b,&c,&j);

    if (b< c-j )
    {
        printf("advertise");
    }
    else if(b> c-j){

        printf("do not advertise");
    }
    else if(b == c-j){
        printf("does not matter");
    }
    printf("\n");
}

return 0;
}
