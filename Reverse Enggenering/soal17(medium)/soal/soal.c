// file: find_flag.c
#include <stdio.h>
#include <string.h>

int main() {
    char input[100];
    printf("Enter the flag: ");
    scanf("%99s", input);

    if (strcmp(input, "FLAG{R3vRs9_ELF_22G}") == 0) {
        printf("Correct! You found the flag.\n");
    } else {
        printf("Wrong flag.\n");
    }
    return 0;
}
