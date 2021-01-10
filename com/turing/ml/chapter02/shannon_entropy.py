
'''
cimport numpy as cnp
from libc.math cimport log as clog

cpdef shannon_entropy_v1(cnp.ndarray p_x):
    cdef double res = 0.0
    cdef int n = p_x.shape[0]
    cdef int i
    for i in range(n):
        res += p_x[i] * clog(p_x[i])
    return -res

cpdef shannon_entropy_v2(cnp.ndarray[double] p_x):
    cdef double res = 0.0
    cdef int n = p_x.shape[0]
    cdef int i
    for i in range(n):
        res += p_x[i] * clog(p_x[i])
    return -res
''''''














