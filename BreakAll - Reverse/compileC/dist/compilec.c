#include <stdio.h>

typedef unsigned char uint8_t;

int main(void)
{
    uint8_t c[] = {193, 203, 198, 192, 252, 207, 194, 203, 203, 200, 216, 208, 200, 213, 203, 195, 216, 200, 193, 216, 196, 166, 250};

    for (int i = 0; i < sizeof(c); ++i) {
        c[i] ^= 0x87;
    }

    printf("%s\n", c);
}