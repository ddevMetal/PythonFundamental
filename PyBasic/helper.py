import os

def br(qty):
    """
    this function will produce a line break
    """
    return print("-"*qty)

def ctitle(title_name):
    """
    Prints a formatted comment title with underline
    """
    print(f"# {title_name}")
    print("#" + "-" * 60)

def getFullPath(path, subPath, filename):
    """
    Joins path components and returns full file path
    
    Args:
        path: Base directory path (e.g., './NewFolder/')
        subPath: Subdirectory name (e.g., 'Folder_A')
        filename: File name (e.g., 'items.txt')
    
    Returns:
        str: Complete file path
    """
    if path == "" and subPath == "":
        fullpath = os.path.join("./NewFolder", "Folder_Re_A", filename)
    elif path == "":
        fullpath = os.path.join("./NewFolder", subPath, filename)
    else:
        fullpath = os.path.join(path, subPath, filename)
    return fullpath