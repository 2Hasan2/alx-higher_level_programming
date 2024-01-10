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
    char *byte_string;
    long int size, i, limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(py_obj))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)(py_obj))->ob_size;
    byte_string = ((PyBytesObject *)py_obj)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", byte_string);

    if (size >= 10)
        limit = 10;
    else
        limit = size + 1;

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++)
        if (byte_string[i] >= 0)
            printf(" %02x", byte_string[i]);
        else
            printf(" %02x", 256 + byte_string[i]);

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
    long int size, i;
    PyListObject *list;
    PyObject *obj;

    size = ((PyVarObject *)(py_obj))->ob_size;
    list = (PyListObject *)py_obj;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        obj = ((PyListObject *)py_obj)->ob_item[i];
        printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
    }
}

/**
 * print_python_dict - Prints dictionary information
 *
 * @py_obj: Python Object
 * Return: no return
 */
void print_python_dict(PyObject *py_obj)
{
    long int size, i;
    PyDictObject *dict;
    PyObject *key, *value;

    size = ((PyVarObject *)(py_obj))->ob_size;
    dict = (PyDictObject *)py_obj;

    printf("[*] Python dictionary info\n");
    printf("[*] Size of the Python Dictionary = %ld\n", size);

    for (i = 0; i < size; i++)
    {
        key = PyDict_GetItem(dict, dict->ma_keys[i]);
        value = PyDict_GetItem(dict, dict->ma_values[i]);

        printf("Key: %s, Value: %s\n", ((PyUnicodeObject *)key)->ob_sval, ((PyUnicodeObject *)value)->ob_sval);
    }
}

