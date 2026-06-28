#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];

  modified = 0;
  gets(buffer);

  if(modified != 0) {
      printf("BreakALLCTF{4U49uY7OJCrJL0vtbXjd}\n");
  } else {
      printf("Try again?\n");
  }
}

