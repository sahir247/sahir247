#include <stdio.h>

int main() {
    float a, b;  // Declaring variables as float for more accurate results

    // Taking input from the user
    printf("Enter the first number (a): ");
    scanf("%f", &a);
    printf("Enter the second number (b): ");
    scanf("%f", &b);

    // Performing arithmetic operations
    printf("Addition: %.2f\n", a + b);
    printf("Subtraction: %.2f\n", a - b);
    printf("Multiplication: %.2f\n", a * b);
    printf("Division: %.2f\n", a / b);  // Ensuring division uses float
    return 0;
}