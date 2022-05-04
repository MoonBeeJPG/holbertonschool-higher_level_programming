#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
#include <assert.h>
#include <stdlib.h>
/**
* print_python_list_info - A C function that prints some basic info about Python lists
*
* @p: PyObject, is the CPython implementation of the Python Object, implemented using a C struct
*
* 
*/
void print_python_list_info(PyObject *p)
{
	int idx = 0;
	PyObject *iter;

	Py_ssize_t out = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", (int)out);
	printf("[*] Allocated = %d\n", (int)((PyListObjec *)p)->allocated);
	
	while (idx < out)
	{
		iter = PyList_GetItem(p, idx);
		printf("Element %d: %s\n", idx, Py_TYPE(iter)->tp_name);
		idx++;
	}
}
