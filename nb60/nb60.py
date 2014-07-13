# coding: utf-8
from utils import ntos, ston

_NB60AB = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZ_abcdefghijkmnopqrstuvwxyz'

def ntonb60(n):
    return ntos(n, _NB60AB)

def nb60ton(s):
    return ston(s, _NB60AB)
