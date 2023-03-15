#include <iostream>
#include <string>
#include <ctime>

int main()
{
	int n, cnt = 0;

	std::cin >> n;
	// time_t start = clock();

	for (int i = 0; cnt < n; i++)
	{
		if (std::to_string(i).find("666") != std::string::npos)
		{
			cnt++;
			if (cnt == n)
			{
				std::cout << i << std::endl;
				break;
			}
		}
	}
	// time_t end = clock();
	// std::cout << "응답 시간 : " << end - start / (CLOCKS_PER_SEC) << "ms" << std::endl;

}