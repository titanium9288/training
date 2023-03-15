#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(int n, vector<string> words) { 
    vector<int> answer;
    int fail = 0;
    
    for(int i = 0; i < words.size(); i++)
    {
        auto result = find(words.begin(), words.end(), words.at(i));
        if ( i != distance(words.begin(), result))
        {
            fail = i;
            break;
        }
        if ( i != 0)
        {
            if (words.at(i).front() != words.at(i-1).back())
            {
                fail = i;
                break;
            }
        }
    }
    
    answer.push_back(fail == 0 ? 0 : fail%n + 1);
    answer.push_back(fail == 0 ? 0 : fail/n + 1);

    return answer;
}