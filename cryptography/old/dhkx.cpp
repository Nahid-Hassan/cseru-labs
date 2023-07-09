#include<bits/stdc++.h>
#define ll long long
using namespace std;

ll bigmod(ll n, ll r, ll m){
    if(r == 0) return 1;
    if(r == 1) return n%m;
    ll x;
    if(r%2==1) x = bigmod(n, r-1, m)*n;
    else{
        x = bigmod(n, r/(ll)2, m);
        x = x*x;
    }
    return x%m;
}



int main(){

    ll p = 97;
    ll r = 27;

    ll a = 18; // alice private key
    ll b = 21; // bobs private key

    ll x = bigmod(r, a, p);
    ll y = bigmod(r, b, p);

    ll ka = bigmod(y, a, p);
    ll kb = bigmod(x, b, p);

    cout<<"Alices key: "<<ka<<endl;
    cout<<"Bobs key: "<<kb<<endl;

    return 0;
}