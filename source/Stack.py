#******************************************************************************
#   Author: Matt Hartsorn
#   Description: Implementation for the Stack collection class
#******************************************************************************

class Stack:
    def __init__(self):
        self.__items = [];

    def isEmpty(self):
        return self.__items == [];

    def push(self,p):
        self.__items.append(p);

    def pop(self):
        return self.__items.pop();
        
    def size(self):
        return len(self.__items);
        
    def peak(self):
        return self.__items[len(self.__items) - 1];
        
    def __str__(self):
        return str(self.__items);