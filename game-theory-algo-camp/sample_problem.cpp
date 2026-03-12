#include<iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    if (n%6 == 0 || n%6==1 || n%6==2) {
        cout << "Furkan" << endl;
    }
    else {
        cout << "Metin" << endl;
    }

    return 0;
}
