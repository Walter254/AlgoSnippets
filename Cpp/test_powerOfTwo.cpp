// test_powerOfTwo.cpp
#include <iostream>
#include "powerOfTwo.h" // Include the file containing the function

// Test cases for the powerOfTwo function
void testPowerOfTwo() {
    // Test cases
    std::cout << "Testing powerOfTwo function:\n";

    // Test with powers of two
    std::cout << "1: " << (powerOfTwo(1) ? "Pass" : "Fail") << "\n"; // 2^0
    std::cout << "2: " << (powerOfTwo(2) ? "Pass" : "Fail") << "\n"; // 2^1
    std::cout << "4: " << (powerOfTwo(4) ? "Pass" : "Fail") << "\n"; // 2^2
    std::cout << "8: " << (powerOfTwo(8) ? "Pass" : "Fail") << "\n"; // 2^3
    std::cout << "16: " << (powerOfTwo(16) ? "Pass" : "Fail") << "\n"; // 2^4

    // Test with non-powers of two
    std::cout << "3: " << (powerOfTwo(3) ? "Pass" : "Fail") << "\n"; // Not a power of two
    std::cout << "5: " << (powerOfTwo(5) ? "Pass" : "Fail") << "\n"; // Not a power of two
    std::cout << "6: " << (powerOfTwo(6) ? "Pass" : "Fail") << "\n"; // Not a power of two
    std::cout << "7: " << (powerOfTwo(7) ? "Pass" : "Fail") << "\n"; // Not a power of two

    // Test with edge cases
    std::cout << "0: " << (powerOfTwo(0) ? "Pass" : "Fail") << "\n"; // Not a power of two
    std::cout << "-1: " << (powerOfTwo(-1) ? "Pass" : "Fail") << "\n"; // Not a power of two
}

int main() {
    testPowerOfTwo();
    return 0;
}