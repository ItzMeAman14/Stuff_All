#include<stdio.h>

int main(){
    int n1,n2,n3;
    printf("Enter size of 1st set:");
    scanf("%d",&n1);
    
    int set1[n1];
    
    for(int i=0;i<n1;i++){
        printf("Enter %d element:",i+1);
        scanf("%d",&set1[i]);
    }
    
    printf("Enter size of 2nd set:");
    scanf("%d",&n2);
    
    n3 = n1 * n2 * 2;
    int set2[n2],set3[n3];
    
    for(int i=0;i<n2;i++){
    printf("Enter %d element:",i+1);
    scanf("%d",&set2[i]);
    }

    int k = 0,l = 0;
    while(k!=0){
        for(int i=0;i<n1;i++){
            for(int j=0;j<n2;j++){
            set3[l] = set1[i];
            l++;
            if(l == n1*n2*2){
            k = 1;
        }
    }
    }
    }

    for(int i=0;i<n3;i++){
        printf("%d\n",set3[i]);
    }
    



    return 0;
}