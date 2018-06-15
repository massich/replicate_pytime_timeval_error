%module swig_mwe

%include <exception.i>
%exception {
  try {
    $action
      } catch (const std::exception& e) {
    SWIG_exception(SWIG_RuntimeError, e.what());
  }
 }

%include <std_string.i>
%include <std_vector.i>

// Add necessary symbols to generated header
%{
#include "foo.h"
%}

// Process symbols in header
%include "foo.h"
