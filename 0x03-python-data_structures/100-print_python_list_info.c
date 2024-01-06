#include <Python.h>
#include <listobject.h>
#include <object.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, i;
    PyListObject *list;
    PyObject *item;
    size = Py_SIZE(p);
    printf("[*] Size of the Python List = %ld\n", size);
    list = (PyListObject *)p;
    printf("[*] Allocated = %ld\n", list->allocated);
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
