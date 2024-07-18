#include <stdio.h>
#include  "Python.h"

int fib(int n){
    if (n == 0) return (0);
    else if (n==1) return (1);
    else  return fib(n-1) + fib(n-2);
}

int test(){
    printf("fib(4)==%d\n", fib(4));
    printf("fib(8)==%d\n", fib(8));
    return 0;
}

static PyObject * exttest_fib(PyObject * self, PyObject * args){
    int num;
    if (!PyArg_ParseTuple(args, "i", &num))
       return NULL;
    return (PyObject *) Py_BuildValue("i", fib(num));
}

static PyObject * exttest_test(PyObject * self, PyObject * args){
    test();
    return (PyObject *) Py_BuildValue("");
}


static PyMethodDef exttestMethods[] = {
    {"fib", exttest_fib, METH_VARARGS, "fib function"},
    {"test", exttest_test, METH_VARARGS, "test function"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef exttest = 
{
    PyModuleDef_HEAD_INIT,
    "exttest", 
    "",
    -1,
    exttestMethods
};

PyMODINIT_FUNC PyInit_exttest(void){
    return PyModule_Create(&exttest);
}
