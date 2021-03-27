#include <iostream>
using namespace std;

int main()
{
    int n, i;
    cin >> n;
    for (i = 2; i <n-1; i++)
    {
        if (n % i == 0)
        {
            cout << "Non Prime" << endl;
            break;
        }
    }
    if (i == n)
    {
        cout << "Prime";
    }
    return 0;
}