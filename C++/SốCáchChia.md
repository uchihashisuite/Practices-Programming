![image](https://user-images.githubusercontent.com/93731698/183993257-5b308c14-7c26-4e9e-9432-24231d79d8fd.png)

![image](https://user-images.githubusercontent.com/93731698/183993309-a4c0a35f-1a75-471a-9cf0-befed2f6b0eb.png)

```js
#include<bits/stdc++.h>
#define maxn 500010
using namespace std;
int n,a[maxn];
long long s[maxn],ans,dem;
int main()
{
    cin>>n;
    for(int i=1; i<=n; i++)
    {
        cin>>a[i];
        s[i]=s[i-1]+a[i];
    }
    if(s[n]%3!=0)return cout<<0,0;
    long long t=s[n]/3;
 
    for(int i=n-1;i>=1;i--)
    {
        if(s[i]==t)ans+=dem;
        if(s[i]==t*2)dem++;
    }
    cout<<ans;
}
```
