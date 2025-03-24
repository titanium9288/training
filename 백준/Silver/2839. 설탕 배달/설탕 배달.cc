#include <iostream>

int main()
{
	int n;
	std::cin >> n;
	int q0 = n / 5, q1 = q0 + 1, q2 = q0 + 2;
	int result[5] = { q0, q1, q2, q1, q2 };

	if (n == 4 || n == 7)
		std::cout << -1;
	else
		std::cout << result[n % 5];
}