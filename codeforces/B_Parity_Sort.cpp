#include <bits/stdc++.h>
#define print(a) cout << a << endl;
using namespace std;
bool validate(vector<long long> a, vector<long long> b)
{

    for (int i = 0; i < a.size(); i++)
    {
        if (a[i] % 2 != b[i] % 2)
        {
            return false;
        }
    }
    return true;
}
int main()
{
    long long n;
    cin >> n;
    while (n--)
    {
        long long m;
        cin >> m;
        vector<long long> a, b;
        for (int i = 0; i < m; i++)
        {
            int j;
            cin >> j;
            a.push_back(j);
            b.push_back(j);
        }
        sort(b.begin(), b.end());
        bool valid = validate(a, b);
        if (valid)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
}