#!/usr/bin/python3
'''This module has a class node that defines a node of a singly linked list
'''


class Node:
    '''This Node class defines an object which data and next_node pointer

    Attributes:
        data (int): This is data in a node
        next_node (Node): This is a pointer to the next node
    '''
    def __init__(self, data, next_node=None):
        '''This function Initializes an object with data and next_node pointer

        Args:
            data (int): node data as integer
            next_node (Node): The pointer to the next node
        '''
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data

        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        '''This function gets or sets the data of a Node objet'''
        return self.__data

    @data.setter
    def data(self, value):
        '''This function sets a new value for the data in the Node object

        Args:
            value (int): node data as integer
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        '''This function gets or sets the next_node pointer'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''This function sets a new next_node for the Node object

        Args:
            value (Node): This is a parameter value that holds a node
        '''
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    '''This class defines a singly-linked list

        Attributes:
            head (Node): The firs Node in a singly-linked list
    '''
    def __init__(self):
        '''Initializes a new singly-linked list'''
        self.__head = None

    def sorted_insert(self, value):
        '''This function adds a new Node

        Args:
            value (int): node data as integer
        '''
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        '''stringify a singly-linked list

        Returns:
            The singly-linked list as a string
        '''
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
