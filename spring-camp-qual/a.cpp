#include <iostream>
using namespace std;

int main() {

    long long r;
    long long l;
    long long res=0;

    cin >> r >> l;

    for (int i=r; i<=l; i++) {
        if (i%2!=0 && i%3!=0 && i%5!=0 && i%7!=0) {
            res+=1;
        }
    }
    cout << res;


    return 0;
}