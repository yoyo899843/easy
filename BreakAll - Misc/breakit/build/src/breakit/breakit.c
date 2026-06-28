#include"stdio.h"
#include"stdlib.h"

int main(){
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  
  char buffer[8];
  int secret = 8;
  
  gets(buffer);

  if(secret != 8){
    puts("Something wrong.");
    system("/bin/sh");
  } else {
    puts(buffer);
  }

  return 0;
}
