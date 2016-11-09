#******************************************************************************
#   Author: Matt Hartsorn
#   Description: Implementation for the Queue collection class
#******************************************************************************

class Queue:
    def __init__(self):
        self.__items = [];

    def isEmpty(self):
        return self.__items == [];

    def enqueue(self, item):
        self.__items.insert(0,item);

    def dequeue(self):
        return self.__items.pop();

    def size(self):
        return len(self.__items);
        
    def __str__(self):
        return str(self.__items);