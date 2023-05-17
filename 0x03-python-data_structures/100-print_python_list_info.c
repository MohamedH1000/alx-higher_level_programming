#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
void print_python_list_info(PyObject *t)
{
	int a;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(t));
	printf("[*] Allocated = %lu\n", ((PyListObject *)t)->allocated);
	for (a = 0; a < Py_SIZE(t); a++)
		printf("Element %d: %s\n", a, Py_TYPE(PyList_GetItem(t, a))->tp_name);
}
