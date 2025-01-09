#include <iostream>
using namespace std;

int main(){
    //Variables for the calculations
    int x;
    int y;
    char operation;
    //Used to check to break the loop
    char rst;
    //I'm sure this could be handled better, but I used these to hold the two different kinds of answers
    int ans1;
    float ans2;
    while (true){
        cout << "Input the first number: \n";
        cin >> x;
        cout << "Input the operation (+,-,*,/): \n";
        cin >> operation;
        cout << "Input the second number: \n";
        cin >> y;
        cout << "The variables are: " << x << " " << operation << " " << y << "\n";
        switch (operation) {
            case '+' :
                ans1 = x + y;
                cout << "The answer is: " << ans1 << "\n";
                break;
            case '-' :
                ans1 = x - y;
                cout << "The answer is: " << ans1 << "\n";
                break;
            case '*' :
                ans1 = x * y;
                cout << "The answer is: " << ans1 << "\n";
                break;
            case '/' :
                if (y != 0){
                    ans2 = float(x) / float(y);
                    cout << "The answer is: " << ans2 << "\n";
                }else{
                        cout << "Cannot divide by zero. \n";
                }
                break;
            default:
                cout << "Invalid input.";
        }
        cout << "Would you like to restart? (y/n)\n";
        cin >> rst;
        if (rst != 'y')
            break;
    }
    return 0;
}
