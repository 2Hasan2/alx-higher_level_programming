#include <Python.h>

/**
 * print_python_list - prints some basic info about Python lists
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
    if (!PyList_Check(p))
    {
        PyErr_Print();
        return;
    }

    Py_ssize_t size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; ++i)
    {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}


/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        PyErr_Print();
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_Size(p));
    printf("  trying string: %s\n", PyBytes_AS_STRING(p));

    printf("  first 10 bytes: ");
    Py_ssize_t size = PyBytes_Size(p);
    for (Py_ssize_t i = 0; i < 10 && i < size; ++i)
    {
        printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
    }
    printf("\n");
}
