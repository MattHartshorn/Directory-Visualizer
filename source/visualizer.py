#******************************************************************************
#   Author: Matt Hartsorn
#   Description: Main program implementation
#******************************************************************************

import os, sys;
import Tree;


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
        path = Tree.getCurrentDirectory();
    
    
    if (Tree.containsSubDirectories(path)):
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
        Tree.traverseDirectories(path)
    else:    
        print("Directory does not contain any sub-directories.");



# Run the program with input arguments
if (__name__ == "__main__"):
    main(sys.argv);
