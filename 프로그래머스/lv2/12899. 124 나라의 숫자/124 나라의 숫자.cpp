#include <string>
#include <vector>

using namespace std;

string solution(int n) {
    string answer = "";
    
    while (n != 0)
    {
        switch (n % 3)
        {
            case 0:
                answer = '4' + answer;
                break;
            case 1:
                answer = '1' + answer;
                break;
            case 2:
                answer = '2' + answer;
                break;
        }
        if (n % 3 == 0)
        {
            n -= n%3;
            n /= 3;
            n -= 1;
        }
        else 
        {
            n -= n%3;
            n /= 3;
        }
    }
    
    return answer;
}