#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int l, r;
        cin >> l >> r;
        int maxLuck = 0, ans = r;
        for (int i = l; i < r + 1; i++)
        {
            string num = to_string(i);
            sort(num.begin(), num.end());
            int curr = num[num.length() - 1] - num[0];
            if (curr >= maxLuck)
            {
                maxLuck = curr;
                ans = i;
            }
            if (maxLuck == 9)
            {
                break;
            }
        }
        cout << ans << "\n";
    }
}