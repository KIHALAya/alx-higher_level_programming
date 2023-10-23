#include <stdio.h>
#include "Python.h"
#include "floatobject.h"

/**
 * print_python_list - Prints basic info about a Python list.
 * @p: PyObject representing a list.
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_GET_SIZE(p);

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *element = PyList_GET_ITEM(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about a Python bytes object.
 * @p: PyObject representing a bytes object.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size = PyBytes_GET_SIZE(p);

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AS_STRING(p));

	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < 10 && i < size; i++)
	{
		printf("%02x ", (unsigned char)bytes->ob_sval[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic info about a Python float object.
 * @p: PyObject representing a float.
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

