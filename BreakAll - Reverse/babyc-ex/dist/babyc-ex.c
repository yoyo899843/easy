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
  char flag[] = "\xb7\x12\xb8\x99\xde<_\xff\xed\t\xb4\x1a\x9f:1\x11\xea\x30\x30\xce B\xf9\xd0zu\xbbI\xf5\x37\xbdZ\x0ft\x97\xc0\xbd\x08\xe3\x83\x17~\x05\x19\x38@\x1dt\x9e\x39\x8b\xbf\xc8\x1b\x43\xe2\xfew\xa8\x00";
  char key1[] = "\x92\xdd\x49\x61\x8d\xf0\xc5\x23\x6d\x99\x54\x9d\xb3\xde\x25\xaa\x00";
  char key2[] = "\x36\x9c\x1e\x93\x0a\x92\xd7\xe7\x00";
  char key3[] = "\x55\x1f\xae\x2c\x22\x14\x38\x48\xc2\x53\x9f\x4b\x00";
  
  char input[70] = {0};

  printf("Hey hey, I've upgraded my system, no way you can guess it!\n");
  printf("guess the flag: ");
  scanf("%s", input);

  enc(input, key2);
  enc(input, key1);
  enc(flag, key3);

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
