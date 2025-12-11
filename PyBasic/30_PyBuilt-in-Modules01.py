"""
Python OS Module Examples
=========================
Demonstrates common file system operations using Python's os module.

Topics covered:
1. Check if folder exists and create it
2. Join paths and create multiple folders
3. Rename files (two methods)
4. Traverse directory tree with os.walk()
"""

import os


# ==============================================================================
# EXAMPLE 1: Check if Folder Exists and Create It
# ==============================================================================
def create_folder_if_not_exists():
    """
    Check if a folder exists at the specified path.
    If it doesn't exist, create it using os.makedirs().
    
    Note: os.makedirs() creates all intermediate directories if needed.
    """
    # Use relative path from current directory (more portable)
    folder_path = os.path.join(os.getcwd(), 'NewFolder')
    
    if os.path.exists(folder_path):
        print("✓ Path already exists.")
    else:
        print("✗ Path doesn't exist. Creating folder...")
        os.makedirs(folder_path)  # Creates parent directories if needed
        print(f'📁 Folder created successfully at: {folder_path}')
    
    return folder_path


# ==============================================================================
# EXAMPLE 2: Join Paths and Create Multiple Subfolders
# ==============================================================================
def create_multiple_folders(base_path):
    """
    Create multiple subfolders inside a base directory.
    
    Args:
        base_path: The parent directory where subfolders will be created
        
    Logic:
        - Uses os.path.join() for cross-platform path compatibility
        - Checks existence before creating to avoid errors
        - Creates each folder only if it doesn't exist
    """
    folder_names = ['Folder_A', 'Folder_B', 'Folder_C']
    
    for folder_name in folder_names:
        # Join paths (handles \ or / depending on OS)
        new_folder_path = os.path.join(base_path, folder_name)
        
        # Only create if doesn't exist
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            print(f'✓ Created folder: {folder_name}')
        else:
            print(f'⊙ Folder already exists: {folder_name}')


# ==============================================================================
# EXAMPLE 3: Rename Files (Method 1 - Simple Replace)
# ==============================================================================
def rename_files_method1():
    """
    Rename files in a directory by replacing part of the filename.
    
    Process:
        1. List all items in directory with os.listdir()
        2. Search for files matching a pattern
        3. Replace old name with new name
        4. Use os.rename() with absolute paths
    """
    target_folder = os.path.join(os.getcwd(), 'NewFolder', 'Folder_A')
    
    # Ensure folder exists before attempting to list/rename
    if not os.path.exists(target_folder):
        print(f"✗ Folder not found: {target_folder}")
        return
    
    # Iterate through all files in the directory
    for filename in os.listdir(target_folder):
        print(f"Checking: {filename}")
        
        # Check if target filename pattern exists
        if 'file_1.txt' in filename:
            new_filename = filename.replace('file_1.txt', 'newFile1.txt')
            
            # Build absolute paths (required for os.rename)
            old_path = os.path.join(target_folder, filename)
            new_path = os.path.join(target_folder, new_filename)
            
            os.rename(old_path, new_path)
            print(f'✓ Renamed: {filename} → {new_filename}')


# ==============================================================================
# EXAMPLE 4: Rename Files (Method 2 - Using Absolute Paths)
# ==============================================================================
def rename_files_method2():
    """
    Alternative method for renaming files using explicit absolute paths.
    
    Difference from Method 1:
        - More verbose with separate variables for old/new paths
        - Same functionality, different coding style
    """
    target_folder = os.path.join(os.getcwd(), 'NewFolder', 'Folder_A')
    
    if not os.path.exists(target_folder):
        print(f"✗ Folder not found: {target_folder}")
        return
    
    for filename in os.listdir(target_folder):
        print(f'Checking file: {filename}')
        
        if 'newFile1.txt' in filename:
            new_filename = filename.replace('newFile1.txt', 'newFile2.txt')
            
            # Store absolute paths in separate variables
            abs_old_filepath = os.path.join(target_folder, filename)
            abs_new_filepath = os.path.join(target_folder, new_filename)
            
            os.rename(abs_old_filepath, abs_new_filepath)
            print(f'✓ Renamed: {filename} → {new_filename}')


# ==============================================================================
# EXAMPLE 5: Traverse Directory Tree with os.walk()
# ==============================================================================
def traverse_directory_tree():
    """
    Recursively walk through all directories and files starting from a path.
    
    os.walk() yields a tuple for each directory:
        - root: Current directory path (absolute)
        - dirs: List of subdirectory names in current directory
        - files: List of file names in current directory
    
    Behavior:
        - Starts at specified path
        - Only goes DOWN into subdirectories (never up to parent)
        - Recursively explores ALL nested folders (no depth limit)
        - Each iteration processes one directory level
    """
    # Start from current working directory
    start_path = os.getcwd()
    
    print(f"\n{'='*70}")
    print(f"Directory Tree Traversal Starting from: {start_path}")
    print(f"{'='*70}")
    
    # Walk through directory tree
    for root, dirs, files in os.walk(start_path):
        # Print current directory being examined
        print(f'\n📂 Directory: {root}')
        
        # Print all subdirectories in current directory
        if dirs:
            print(f'   ├─ Subfolders ({len(dirs)}):')
            for directory in dirs:
                print(f'   │  └─ {directory}')
        
        # Print all files in current directory
        if files:
            print(f'   ├─ Files ({len(files)}):')
            for file in files:
                print(f'   │  └─ {file}')
        
        # Visual separator if no subdirectories or files
        if not dirs and not files:
            print(f'   └─ (empty)')


# ==============================================================================
# EXAMPLE 6: Search for Files by Name Pattern
# ==============================================================================
def search_files_by_pattern(start_path, search_pattern):
    """
    Search for files containing a specific string in their filename.
    
    Args:
        start_path: Directory to start searching from
        search_pattern: String to search for in filenames (case-sensitive)
    
    Logic:
        - Uses os.walk() to traverse all subdirectories
        - Checks each filename for the search pattern
        - Builds absolute path when match is found
        - Returns all matching file paths
    
    Example:
        search_files_by_pattern(os.getcwd(), 'test')
        # Finds: test.txt, test_data.py, pytest.ini, etc.
    """
    found_files = []
    
    print(f"\n{'='*70}")
    print(f"Searching for files containing '{search_pattern}'...")
    print(f"Starting from: {start_path}")
    print(f"{'='*70}\n")
    
    # Traverse directory tree
    for root, dirs, files in os.walk(start_path):
        # Check each file in current directory
        for file in files:
            # Check if search pattern is in filename
            if search_pattern in file:
                # Build absolute path by joining root + filename
                abs_path = os.path.join(root, file)
                found_files.append(abs_path)
                print(f'✓ Found: {abs_path}')
    
    # Summary
    print(f"\n{'='*70}")
    if found_files:
        print(f"Total files found: {len(found_files)}")
    else:
        print(f"✗ No files containing '{search_pattern}' were found.")
    print(f"{'='*70}")
    
    return found_files


# ==============================================================================
# EXAMPLE 7: Search for Files by Extension
# ==============================================================================
def search_files_by_extension(start_path, extension):
    """
    Find all files with a specific file extension.
    
    Args:
        start_path: Directory to start searching
        extension: File extension to search for (e.g., '.txt', '.py', '.json')
    
    Note: Extension should include the dot (e.g., '.txt' not 'txt')
    """
    found_files = []
    
    print(f"\n{'='*70}")
    print(f"Searching for files with extension '{extension}'...")
    print(f"{'='*70}\n")
    
    for root, dirs, files in os.walk(start_path):
        for file in files:
            # Check if file ends with the specified extension
            if file.endswith(extension):
                abs_path = os.path.join(root, file)
                found_files.append(abs_path)
                print(f'✓ {abs_path}')
    
    print(f"\n{'='*70}")
    print(f"Total {extension} files found: {len(found_files)}")
    print(f"{'='*70}")
    
    return found_files


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("Python OS Module - File System Operations")
    print("=" * 70)
    
    # Example 1: Create base folder
    print("\n[1] Creating base folder...")
    base_folder = create_folder_if_not_exists()
    
    # Example 2: Create multiple subfolders
    print("\n[2] Creating multiple subfolders...")
    create_multiple_folders(base_folder)
    
    # Example 3 & 4: Uncomment to test file renaming
    # print("\n[3] Renaming files (Method 1)...")
    # rename_files_method1()
    # 
    # print("\n[4] Renaming files (Method 2)...")
    # rename_files_method2()
    
    # Example 5: Traverse directory tree
    print("\n[5] Traversing directory tree...")
    traverse_directory_tree()
    
    # Example 6: Search for files by pattern
    print("\n[6] Searching for files by pattern...")
    search_files_by_pattern(os.getcwd(), 'test')
    
    # Example 7: Search for files by extension
    print("\n[7] Searching for files by extension...")
    search_files_by_extension(os.getcwd(), '.txt')
    
    print("\n" + "=" * 70)
    print("Execution completed!")
    print("=" * 70)