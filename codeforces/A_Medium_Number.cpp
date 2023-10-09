#include <bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    for (int j = 0; j < n; j++)
    {
        vector<int> nums;
        int m, k, l;
        cin >> m >> k >> l;
        nums.push_back(m);
        nums.push_back(k);
        nums.push_back(l);
        sort(nums.begin(), nums.end());
        cout << nums[1] << "\n";
    }
    return 0;
}
