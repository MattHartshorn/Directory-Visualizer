#******************************************************************************
#   Author: Matt Hartsorn
#   Description: Implementation of the traversal and printing of the 
#                directories
#******************************************************************************

import os;
from Stack import Stack;
from Queue import Queue;



class LineChars:
    """
    Contains all the required characters used to draw the directories.
    """
    
    Vertical = "│";
    Horizontal = "─";
    TopLeftCorner = "┌";
    BottomLeftCorner = "└";
    DownRight = "├";
    
    

def getCurrentDirectory():
    """
    Returns the current working directory.
    
    @return: The full path of the current working directory.
    """
    return os.path.dirname(os.path.realpath(__file__));
        

def containsSubDirectories(path):
    """
    Returns whether or not the provided directory contains any sub-directories.

    @param path: Full path of the desired directory to search
    @return: True if the provided path contains sub directories, otherwise false.
    """
    
    try:
        for name in os.listdir(path):
            if os.path.isdir(os.path.join(path, name)):
                return True;
    except:
        pass;
        
    return False;

def getSubDirectoryQueue(path):
    """
    Returns a queue containing all the sub-directories of the provided path.
    
    @param path: Full path of the desired directory to search
    @return: A queue that contains all the sub-directories of the provided path.
    @notes: An empty queue is returned if permission to the provided path is denied.
    """
    res = Queue();
    
    try:
        for name in os.listdir(path):
            if os.path.isdir(os.path.join(path, name)):
                res.enqueue(name);
    except:
        pass;
    
    return res;
        

       
def traverseDirectories(path):
    """
    Traverses all the sub-directories of the provided directory. All the 
    directories are printed out as they are visited.
    
    @param path: Full path of the desired directory to traverse
    """ 
    
    
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
    """
    Prints out the provided directory name following the supplied tree structure.
    
    @param dir_name: Name of the directory that will be printed
    @param has_sibling: True if the provided directory has one or more siblings
    @param tree_structure: String representing the current tree structure of the visited nodes
    
    @return: The modified tree structure based on if the provided directory has any siblings.
    """
    
    
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