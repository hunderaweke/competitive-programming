#include <iostream>
#include <vector>
#include <unordered_set>

int main()
{
    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        int m;
        std::cin >> m;

        std::vector<int> ls(m);
        for (int j = 0; j < m; j++)
        {
            std::cin >> ls[j];
        }

        std::unordered_set<int> uniqueElements;
        int count = 0;
        for (int j = m - 1; j >= 0; j--)
        {
            if (uniqueElements.find(ls[j]) == uniqueElements.end())
            {
                uniqueElements.insert(ls[j]);
                count++;
            }
            else
            {
                break;
            }
        }

        std::cout << m - count << std::endl;
    }

    return 0;
}