#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(llist):
    # Prev를 None으로 두고  nxt는 리스트 current의 다음 숫자를 두고 그 전의 숫자를 current의
    #next넘버 바꾸면서 화살표를 바꾸게 된다 그다음에 prev를 현 숫자로 옮겨서 while loop를 돌게한다.
    prev = None  
    while llist != None:
        nxt = llist.next
        llist.next = prev
        prev = llist
        llist = nxt
    return prev
