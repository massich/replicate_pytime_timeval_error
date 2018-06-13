#include <iostream>
#include "foo.h"

int main(int argc, char* argv[])
{
  std::cout << "Hello from main" << std::endl;
  std::cout << foo_hello() << std::endl;
  std::cout << link_bar_hello() << std::endl;

  return 0;
}

