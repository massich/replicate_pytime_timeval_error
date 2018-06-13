# replicate_pytime_timeval_error
This is a MWE to replicate this issue https://github.com/openmeeg/openmeeg/issues/312

## Requirments
* cmake >= 3.2

## How to run it
```sh
mkdir build
cd build
cmake .. && cmake --build . && ctest -v .
```
