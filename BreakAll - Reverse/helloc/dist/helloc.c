#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int hello1()
{
    return 76;
}

int hello2(int a)
{
    return a + hello1();
}

int main(void)
{
    char flag[19] = { 0 };
    int secret[5] = {8502, 13431, 10165, 6767, 11495};
    int key[5] = {109, 121, 107, 101, 121};

    flag[0] = 70;
    flag[1] = hello1();

    for (int i = 0; i < 2; ++i) {
        flag[2+i] = flag[0+i] - 5;
    }

    flag[4] = 66 ^ 57;
    
    for (int i = 0; i < 5; ++i) {
        flag[5 + i] = secret[i] / key[i];
    }

    flag[10] = hello2(2);
    flag[11] = hello2(1) - 29;

    if (flag[11] & 0x80) {
        flag[12] = flag[11];
    } else {
        flag[12] = flag[7];
    }

    flag[13] = hello2(0);
    flag[14] = ((hello1() * hello2(8)) & 0xff) - 191;
    flag[15] = 'E';
    flag[16] = 'v';
    flag[15] = flag[15] ^ flag[16];
    flag[16] = flag[15] ^ flag[16];
    flag[15] = flag[15] ^ flag[16];
    flag[17] = '}';

    // TODO: write some C code to output flag

    return 0;
}
