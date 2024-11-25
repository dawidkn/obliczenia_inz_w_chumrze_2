#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <chrono>

bool is_prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= std::sqrt(n); ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    std::vector<int> primes;
    auto start = std::chrono::high_resolution_clock::now();
    int num = 2;

    while (true) {
        auto now = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> elapsed = now - start;
        if (elapsed.count() >= 30.0) break;

        if (is_prime(num)) {
            primes.push_back(num);
        }
        num++;
    }

    std::ofstream outfile("cpp_output.txt");
    outfile << "Found " << primes.size() << " primes in 30 seconds.\n";
    outfile.close();

    return 0;
}
