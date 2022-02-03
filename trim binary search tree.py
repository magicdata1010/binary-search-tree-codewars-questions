# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 01:54:27 2022

@author: 91838
""" # using multiple recursion ,different from deleting nodes
def trim(a,l,r):
    if a==None:
        return None
    if int(a.key)>r:
        return trim(a.leftChild,l,r)
    if int(a.key)<=l:
        return trim(a.rightChild,l,r)
    a.leftChild=trim(a.leftChild,l,r)
    a.rightChild=trim(a.rightChild,l,r)
    return a



