import os;

class LineChars:
    Vertical = "│";
    Horizontal = "─";
    TopLeftCorner = "┌";
    BottomLeftCorner = "└";
    DownRight = "├";
    
    
class Stack:
    def __init__(self):
        self.__items = []

    def isEmpty(self):
        return len(self.__items) == 0

    def push(self,p):
        self.__items.append(p)

    def pop(self):
        return self.__items.pop()
        
    def size(self):
        return len(self.__items);
        
    def peak(self):
        return self.__items[len(self.__items) - 1];
    
class Queue:
    def __init__(self):
        self.__items = []

    def isEmpty(self):
        return self.__items == []

    def enqueue(self, item):
        self.__items.insert(0,item)

    def dequeue(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)
  

  
def getCurrentDirectory():
    return os.path.dirname(os.path.realpath(__file__));

def containsSubDirectories(dir):
    return len(os.listdir(dir)) > 0;
    
def getSubDirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]
            
def getSubDirectoryQueue(dir):
    res = Queue();
    
    for name in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, name)):
            res.enqueue(name);
    
    return res;

def printDirectory(dir_name, has_sibling = False, tree_structure = None):
    
    # Detect invalid tree input, must be a string
    if (tree_structure != None and not isinstance(tree_structure, str)):
        raise ValueError("'tree_structure' must be a string");
    
    # Create the resulting tree structure that is returned
    result_tree = "    ";
    
    # Add vertical line if the current dir has a 
    if (has_sibling):
        result_tree = LineChars.Vertical + "   ";
        
    output = "";
    
    # Update the resulting tree structure and the line that will be printed
    if (tree_structure != None):
        result_tree = tree_structure + result_tree;
        output = tree_structure;
        
    # Change the starting character of the output based on if there is a sibling or it is the first dir in the tree
    if (tree_structure != None and has_sibling):
        output += LineChars.DownRight;
    elif (tree_structure == None and has_sibling):
        output += LineChars.TopLeftCorner;
    else:
        output += LineChars.BottomLeftCorner;
        
    # Print the current directory tree structure
    print(line + LineChars.Horizontal + LineChars.Horizontal + LineChars.Horizontal + dir_name);
    
    return result_tree;
        
       
def traverseDirectories(path = None):

    if (not os.path.isdir(None)):
        raise ValueError("The provided directory, '" + path + "' does not exist.");

    # Get a queue of all of the sub directories
    sub_dirs = getSubDirectoryQueue();
    
    # Determine if there are any subdirectories
    if (sub_dirs.isEmpty()):
        return False;
    
    
    dir_structures = Stack();
    dir_structures.push(("", sub_dirs));
    
    
    # Depth First Search
    # Stack containing current Tree Structure as well as a Queue of sub directories
    # - while stack isnt empty 
    #   - Add all sub-directories of current dir to new queue
    #   - Push the current tree and queue onto the stack
    #   - while current queue isnt empty
    #       - print top directory
    #       - if current dir has sub-dirs
    #           - set current dir equal to the current dir
    #           - break
    #   - if queue is empty
    #       - go back one directory
    
    
    while (dir_structures.isEmpty()):
        
        current_tree = dir_structures.peak();
        
        
    
    return True;
    
        
# tree = printDirectory("dir1", True);
# tree = printDirectory("dir2", False, tree);
# tree1 = printDirectory("dir3", True, tree);
# tree1 = printDirectory("dir4", False, tree1);
# tree1 = printDirectory("dir4-1", False, tree1);
# tree = printDirectory("dir5", False, tree);

