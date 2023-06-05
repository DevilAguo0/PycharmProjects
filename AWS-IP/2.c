#include <iostream>
#include <math.h>
using namespace std;
int ss(int n)
{
    int a = 0, b = 0;
    for (int i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
            a++;
    }
    if (a == 0)
        return 1;
    else
        return 0;
}
int main()
{
    int n;
    cin >> n;
    if (n <= 3)
        cout << "empty" << endl;
    for (int i = 3; i + 2 <= n; i++)
    {
        if (ss(i) == 1 && ss(i + 2) == 1)
            cout << i << ' ' << i + 2 << endl;
    }
    return 0;
}