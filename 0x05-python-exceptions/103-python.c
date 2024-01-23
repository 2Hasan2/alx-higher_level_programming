#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - prints information about a PyFloatObject
 * @object: the PyObject
 */
void print_python_float(PyObject *object)
{
	double val = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(object))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	val = ((PyFloatObject *)object)->ob_fval;
	str = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

/**
 * print_python_bytes - prints information about a PyBytesObject
 * @object: the PyObject
 */
void print_python_bytes(PyObject *object)
{
	Py_ssize_t size = 0, i = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(object))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(object);
	printf("  size: %zd\n", size);

	str = (assert(PyBytes_Check(object)), (((PyBytesObject *)(object))->ob_sval));
	printf("  trying string: %s\n", str);

	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", str[i]);
		i++;
	}
	printf("\n");
}

/**
 * print_python_list - prints information about a PyListObject
 * @object: the PyObject
 */
void print_python_list(PyObject *object)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");

	if (PyList_CheckExact(object))
	{
		size = PyList_GET_SIZE(object);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)object)->allocated);

		while (i < size)
		{
			item = PyList_GET_ITEM(object, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);

			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);

			i++;
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
}
