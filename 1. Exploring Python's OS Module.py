
import os 

def list_directory_contents(path): 
    try: 
###### Check if the given path exists ######
        if not os.path.exists(path):
         raise FileNotFoundError(f"The path '{path}' does not exist.")
    

        if not os.path.isdir(path): 
          raise NotADirectoryError(f"The path '{path}' is not a directory.")
    
##### List all files and subdirectories in the specified directory  #####
        contents = os.listdir(path) 

        if contents: 
           print(f"Contents of '{path}':") 
        for item in contents: 
           print(item) 
        else: 
           print(f"The directory '{path}' is empty.") 
 
    except FileNotFoundError as e: 
        print(e) 
    except NotADirectoryError as e: 
        print(e) 
    except PermissionError: 
        print(f"Permission denied: Unable to access '{path}'.") 
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
if __name__ == "__main__":
    path = input("Enter the directory path: ") 

    list_directory_contents(path)

    