#include <bits/stdc++.h>
#include <math.h>
#define print(a) cout << a << endl;
using namespace std;
int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        int diff = (abs(a - b) + 1) / 2;
        print(((diff + c - 1) / c));
    }
}