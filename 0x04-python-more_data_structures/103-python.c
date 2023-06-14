#include <Python.h>
#include <stdio.h>

/**
* print_python_bytes - Prints bytes info
* made By MEGATRON
* @p: Python Object
* Return: zero
*/

void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, a, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (a = 0; a < limit; a++)
		if (string[a] >= 0)
			printf(" %02x", string[a]);
		else
			printf(" %02x", 256 + string[a]);

	printf("\n");
}

/**
* print_python_list - Prints lst info
* Made by MEGATRON
* @p: Python Object
* Return: zero
*/

void print_python_list(PyObject *p)
{
	long int size, a;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (a = 0; a < size; a++)
	{
		obj = ((PyListObject *)p)->ob_item[a];
		printf("Element %ld: %s\n", a, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
