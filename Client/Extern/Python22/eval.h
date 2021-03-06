
/* Interface to execute compiled code */

#ifndef Py_EVAL_H
#define Py_EVAL_H
#ifdef __cplusplus
extern "C" {
#endif

DL_IMPORT(PyObject *) PyEval_EvalCode(PyCodeObject *, PyObject *, PyObject *);

DL_IMPORT(PyObject *) PyEval_EvalCodeEx(PyCodeObject *co,
					PyObject *globals,
					PyObject *locals,
					PyObject **args, int argc,
					PyObject **kwds, int kwdc,
					PyObject **defs, int defc,
					PyObject *closure);

#ifdef __cplusplus
}
#endif
#endif /* !Py_EVAL_H */
