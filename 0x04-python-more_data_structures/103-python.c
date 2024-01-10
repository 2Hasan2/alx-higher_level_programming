#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @py_obj: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *py_obj)
{
    PyBytesObject *byte_obj = (PyBytesObject *)py_obj;
    long int size = PyBytes_Size(py_obj);
    char *byte_string = PyBytes_AsString(py_obj);

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(py_obj))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", byte_string);

    long int limit = (size >= 10) ? 10 : size + 1;

    printf("  first %ld bytes:", limit);

    for (long int i = 0; i < limit; i++)
    {
        unsigned char byte = byte_string[i];
        printf(" %02x", byte);
    }

    printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @py_obj: Python Object
 * Return: no return
 */
void print_python_list(PyObject *py_obj)
{
    PyListObject *list = (PyListObject *)py_obj;
    long int size = PyList_Size(py_obj);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (long int i = 0; i < size; i++)
    {
        PyObject *obj = PyList_GetItem(py_obj, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
    }
}