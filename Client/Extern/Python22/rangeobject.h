
/* Range object interface */

#ifndef Py_RANGEOBJECT_H
#define Py_RANGEOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

/*
A range object represents an integer range.  This is an immutable object;
a range cannot change its value after creation.

Range objects behave like the corresponding tuple objects except that
they are represented by a start, stop, and step datamembers.
*/

extern DL_IMPORT(PyTypeObject) PyRange_Type;

#define PyRange_Check(op) ((op)->ob_type == &PyRange_Type)

extern DL_IMPORT(PyObject *) PyRange_New(long, long, long, int);

#ifdef __cplusplus
}
#endif
#endif /* !Py_RANGEOBJECT_H */
