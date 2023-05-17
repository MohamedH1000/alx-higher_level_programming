#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
void print_python_list_info(PyObject *t)
{
        int a, b;

        b = PyList_Size(t);
        for (a = 0; a < b; a++)
                printf("[*] the size of the python list = %d", b);
}
