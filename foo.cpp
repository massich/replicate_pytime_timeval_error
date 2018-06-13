#include "bar.h"
#include "foo.h"

std::string foo_hello()
{
    return "Hello from foo";
}

std::string link_bar_hello()
{
    return bar_hello();
}
