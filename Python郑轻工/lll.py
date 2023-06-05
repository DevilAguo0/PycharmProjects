#include<cstdio>
#include <cstring>
using namespace std;

int main()
{
    int l,m,cnt=0;
    scanf("%d %d",&l,&m);
    bool a[l];
    for(int i=0;i<=l;i++)
        a[i]=false;
    for(int i=0;i<=m;i++)
    {
        int ii,jj;
        scanf("%d %d",&ii,&jj);
        for(int j=ii;j<=jj;j++)
            if(a[j]==false)
                a[j]=true;
    }
    for(int i=0;i<=l;i++)
        if(a[i]==false)
            cnt++;
    printf("%d",cnt+1);

    return 0;
}