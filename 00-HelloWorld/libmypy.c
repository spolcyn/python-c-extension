#include <Python.h>
#include "libmypy.h"
#include <stdio.h>

PyObject * hello(PyObject * self) {
    // Py_BEGIN_ALLOW_THREADS
    sleep(500);
    // Py_END_ALLOW_THREADS
	return PyUnicode_FromFormat("Hello C extension!");
}
