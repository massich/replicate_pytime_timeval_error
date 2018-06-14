from swig_mwe import foo_hello, link_bar_hello

assert foo_hello() == "hello from foo"
assert link_bar_hello() == "hello from bar"
