#include <bits/stdc++.h>
#define p(a) cout << a << endl
#define ll long long
using namespace std;
int main()
{
    ll t, i;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        s += '#';
        vector<char> v;
        for (i = 0; i < s.size();)
        {
            if (s[i] == s[i + 1])
                i += 2;
            else
                v.push_back(s[i]), i++;
        }
        sort(v.begin(), v.end());
        set<char> st;
        for (ll i = 0; i < v.size() - 1; i++)
        {
            st.insert(v[i]);
        }
        for (auto it : st)
            cout << it;
        cout << endl;
    }
}