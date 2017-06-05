#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a node class use for singlelist
# author Yongjun Chen

class Node(object):
    def __init__(self,val,p=0):
        self.data = val
        self.next = p