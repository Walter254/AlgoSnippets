// Write a C++ function to check whether a given integer x is a power of two (e.g., 1, 2, 4, 8, 16, ...).

#include <iostream>
#include "powerOfTwo.h" // Include the header file

bool powerOfTwo(int x) {
    // Check if x is greater than 0 and if it has exactly one bit set
    return (x > 0) && ((x & (x - 1)) == 0);
}