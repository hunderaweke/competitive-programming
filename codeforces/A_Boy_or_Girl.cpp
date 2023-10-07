#include <bits/stdc++.h>
using namespace std;
int main()
{
    unordered_set<char> s;
    string user_name;
    cin >> user_name;
    for (auto i : user_name)
    {
        s.insert(i);
    }
    if (s.size() % 2 == 0)
    {
        cout << "CHAT WITH HER!\n";
    }
    else
    {
        cout << "IGNORE HIM!\n";
    }
}