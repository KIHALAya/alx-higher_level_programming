#include <Python.h>

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: Python object (bytes) to print information about
 */
void print_python_bytes(PyObject *p)
{
	int i, size;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = (int)PyBytes_GET_SIZE(p);
	str = PyBytes_AsString(p);

	printf("  size: %d\n", size);
	printf("  trying string: %s\n", str);
	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
		printf("%02x ", str[i] & 0xff);

	printf("\n");
}

/**
 * print_python_list - Print information about a Python list object
 * @p: Python object (list) to print information about
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size, allocated;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *elem = PyList_GetItem(p, i);
		const char *elem_type = Py_TYPE(elem)->tp_name;

		printf("Element %zd: %s\n", i, elem_type);

		if (PyBytes_Check(elem))
			print_python_bytes(elem);

	}
}


