#include"stdio.h"
#include"stdlib.h"

void printTheKey(){
  char key[40] = {0};
  for(int i=0; i<20; i++){
    key[i*2] = (('a'+i)*i + 5)%26 + 'a';
    key[i*2+1] = (('k'*i)+i+7)%26 + 'a';
  }
  for(int i=0; i<40; i++){
    int j = i*32%40;
    char tmp = key[i];
    key[i] = key[j];
    key[j] = tmp;
  }
  key[39] = 0;
  printf("MyFirstCTF{%s}\n", key);
}

int main(){
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  int token = 1234;
  char key[16];

  printf("Billy left his key in the locked room.\n");
  printf("However, he forgot the token of the room.\n");
  printf("Do you know what's the key?");

  read(0, key, 40);

  if((int)token == 0xdeadbeef){
    printf("Door open. OwO\n");
    printTheKey();
    system("cat /home/ctf/flag");
  }else{
    printf("Cannot open door. QwQ\n");
  }

  return 0;
}
