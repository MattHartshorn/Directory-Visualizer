import os, sys;

class LineChars:
    Vertical = "│";
    Horizontal = "─";
    TopLeftCorner = "┌";
    BottomLeftCorner = "└";
    DownRight = "├";
    
    
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
  

  
def getCurrentDirectory():
    return os.path.dirname(os.path.realpath(__file__));
        

def containsSubDirectories(dir):
    try:
        return len(os.listdir(dir)) > 0;
    except:
        return False;
   
   
def getSubDirectoryQueue(dir):
    res = Queue();
    
    try:
        for name in os.listdir(dir):
            if os.path.isdir(os.path.join(dir, name)):
                res.enqueue(name);
    except:
        pass;
    
    return res;
        
       
def traverseDirectories(path):
    
    # Detect invalid input
    if (path == None):
        raise ValueError("Path value cannot be None.");
    elif (not os.path.isdir(path)):
        raise ValueError("The provided directory, '" + path + "' does not exist.");

    # Get a queue of all of the sub directories
    sub_dirs = getSubDirectoryQueue(path);
    
    # Determine if there are any subdirectories
    if (sub_dirs.isEmpty()):
        return;
    
    # Declare the stack, and add the first set of sub directories
    dir_structures = Stack();
    dir_structures.push(("", sub_dirs));
    
    while (not dir_structures.isEmpty()):
        # Peak at the top element on the stack
        current_tree, current_sub_dirs = dir_structures.peak();
        
        while (not current_sub_dirs.isEmpty()):        
            # Get and print the current directory
            dir = current_sub_dirs.dequeue();
            next_tree = printDirectory(dir, not current_sub_dirs.isEmpty(), current_tree);
            
            # Get the new directory path and sub directories
            path = os.path.join(path, dir);
            sub_dirs = getSubDirectoryQueue(path);
            
            if (not sub_dirs.isEmpty()):
                # Add any subdirectories to the stack
                dir_structures.push((next_tree, sub_dirs));
                current_sub_dirs = sub_dirs;
                break;
            else:
                #navigate the path back one dir 
                path, _ = os.path.split(path);
            
                
        # Remove top item from the stack when all directories are visited
        if (current_sub_dirs.isEmpty()):
            dir_structures.pop();
            path, _ = os.path.split(path); #navigate the path back one dir 
   

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
    print(output + LineChars.Horizontal + LineChars.Horizontal + LineChars.Horizontal + dir_name);
    
    return result_tree;   
        
        

def main(argv):

    path = "";

    # Get the first argument as a path name
    if (len(argv) > 1):
        path = argv[1];
        
        try:
            if (not os.path.isabs(path)):
                path = os.path.abspath(path);
                
            if (not os.path.exists(path)):
                print("The provided directory does not exist.");
                return;
                
        except:
            print("Invalid directory value.");
            return;
    else:
        path = getCurrentDirectory();
    
    
    if (containsSubDirectories(path)):
        # Print out the description of the traversal
        msg = "Folder path visualization for ";
        if (len(argv) > 1):
            print(msg + "the specified directory:");
            print(path);
        else:
            drive, _ = os.path.splitdrive(path)
            print(msg + "the current directory:");
            print(drive + "\\.");
        
        
        # Perform the traversal
        traverseDirectories(path)
    else:    
        print("Directory does not contain any sub directories.");



# Run the program with input arguments
if (__name__ == "__main__"):
    main(sys.argv);
