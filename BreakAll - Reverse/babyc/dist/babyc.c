#include"stdio.h"
#include"string.h"

void enc(char* str, char* key){
  int str_len = strlen(str);
  int key_len = strlen(key);

  for(int i=0; i<str_len; i++){
    str[i] = str[i] ^ key[i % key_len];
  }
}

int main(){
  char flag[] = {0xd4, 0x91, 0x08, '&', 0xf6, 0xa3, 0xac, 'N', 0x1d, 0xf5, '1', 0xc2, 0xf0, 0x81, 'f', 0xc2, 0xf3, 0xb1, '%', 0x1c, 0x00};
  char key[] = {0x92, 0xdd, 0x49, 0x61, 0x8d, 0xf0, 0xc5, 0x23, 0x6d, 0x99, 0x54, 0x9d, 0xb3, 0xde, 0x25, 0xaa, 0x00};

  char input[30] = {0};

  printf("Hi, guess the flag: ");
  scanf("%s", input);

  enc(input, key);

  int found = 1;
  for(int i=0; i<strlen(flag); i++){
    if(flag[i] != input[i]){
      found = 0;
      break;
    }
  }

  if(found){
    printf("You got it!\n");
  }else{
    printf("Pfft Nope!\n");
  }
}
