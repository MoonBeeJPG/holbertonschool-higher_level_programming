#include "listobject.h"
#include "object.h"
#include "Python.h"
/**
* print_python_list_info - A C function that prints some basic info about Python lists
*
* @p: PyObject, is the CPython implementation of the Python Object, implemented using a C struct
*
* 
*/
void print_python_list_info(PyObject *p)
{
	PyGILState_STATE state = PyGILState_Ensure();

	if (!PyCallable_Check(func))
	{
		goto fail;
	}
}
