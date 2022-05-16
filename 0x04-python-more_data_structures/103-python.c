#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
#include <assert.h>
#include <stdlib.h>
/**
* print_python_list - A function that print some basic info about Python lists
*
* @p: PyObject, is the CPython implementation of the Python Object, implemented using a C struct
*/
void print_python_list(PyObject *p)
{
	int idx = 0;
	PyObject *iter;

	Py_ssize_t out = PyList_Size(p);
	printf("[*] Python list info");
	printf("[*] Size of the Python List = %d\n", (int)out);
	printf("[*] Allocated = %d\n",(int)((PyListObject *)p)->allocated);

	while (idx < out)
	{
		iter = PyList_GET_ITEM(p, idx);
		printf("Element %d: %s\n", idx, PyType_Type);
		idx++;
	}
}
/**
* print_python_bytes - A function that print some basic information about Python bytes objects
*
* @p: PyObject, is the CPython implementation of the Python Object, implemented using a C struct
*/
void print_python_bytes(PyObject *p)
{

}
