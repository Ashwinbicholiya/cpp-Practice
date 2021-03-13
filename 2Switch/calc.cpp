//By using Switch
#include <iostream>
using namespace std;
int main()
{
    int n1,n2;
    cout << "Enter Two numbers" << endl;
    cin >> n1 >> n2;
    char op;
    cout << "Input an operator" << endl;
    cin >> op;
    switch (op)
    {
    case '+':
        cout << n1 + n2 << endl;
        break;
    case '-':
        cout << n1 - n2 << endl;
        break;
    case '/':
        cout << n1 / n2 << endl;
        break;
    case '%':
        cout << n1 % n2 << endl;
        break;
    default:
        break;
    }
    return 0;
}