#include <bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[])
{
    int t;
    cin >> t;
    while (t--)
    {
        int max = 0, min = 0, l, n;
        cin >> l >> n;
        while (n--)
        {
            int elem;
            cin >> elem;
            min = std::max(min, std::min(elem, l - elem));
            max = std::max(max, std::max(elem, l - elem));
        }
        cout << min << " " << max << endl;
    }

    return 0;
}
