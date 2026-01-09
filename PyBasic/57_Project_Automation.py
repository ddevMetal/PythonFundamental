"""
Project Title: Let's sort your Messy Download Folder!

"""

# Library Imports
import os
import shutil   
from pathlib import Path

# Global Variables 
#---------------------------------------------------
current_dir = Path(__file__).parent
PATH_DOWNLOADS = os.path.join(current_dir, 'Generated_Data')


# Define Sorting Rules
#-----------------------------------------------------
CATEGORIES = {
    '_Invoices':   ['invoice', 'receipt', 'bill'],
    '_Images':     ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    '_GIFs':       ['.gif'],
    '_Videos':     ['.mp4', '.mov', '.avi', '.mkv'],
    '_Documents':  ['.pdf', '.docx', '.txt', '.pptx'],
    '_Archives':   ['.zip', '.rar', '.7z', '.tar', '.gz'],
    '_Installers': ['.exe', '.msi', '.dmg', '.pkg'],
    '_Audio':      ['.mp3', '.wav', '.aac', '.flac'],
    '_Code':       ['.py', '.js', '.sh', '.html', '.css', '.java', '.md'],
    '_Data':       ['.csv', '.json', '.xml', '.sql', '.xlsx'],
    '_Design':     ['.psd', '.ai', '.svg', '.xd'],
    '_Subtitles':  ['.srt', '.sub', '.vtt'],
}



# Fucntions
#-----------------------------------------------------
def get_file_cat(filename): 
    """ Find Sorting Folder by names
    
    :param filename : Filename inside of Downloads Folder
    :return         : Name of Sorting Folder
    """   
    # Ignore Sorting Folders
    if filename.startswith('_'):
        return None
       
    # Folder
    filepath = os.path.join(PATH_DOWNLOADS, filename)
    if os.path.isdir(filepath):
        return '_Folder'
    
    # File
    else:
        # Option A - For File Extensions  
        file_extension = '.' + filename.split('.')[-1]

        # Looking for category
        for cat, list_keywords in CATEGORIES.items():
            for keyword in list_keywords:
                if keyword.lower() in filename.lower():
                    return cat
                     
              
        print(f'? {file_extension} - Not Supported. File: ({filename}) (Placed in _Others)')
        return '_Others'  

# Read All Files
#-----------------------------------------------------
def sort_downloads():
    
    # placeholders
    count, fails = 0, 0
    faild_msgs = []
    
    all_files = os.listdir(PATH_DOWNLOADS)
    # if f is a folder and does not start with _
    folders = [f for f in all_files if os.path.isdir(os.path.join(PATH_DOWNLOADS, f)) and not f.startswith('_')]
    files = [f for f in all_files if not os.path.isdir(os.path.join(PATH_DOWNLOADS, f))]
        
    # Reprot to console
    print('-' * 40)
    print('Scanning Downloads Folder...')
    print(f'Folder Found: {len(folders)} (Will be Ignored)')
    print(f'Files Found: {len(files)}')
    
    
    if files:
        print(f'Files Found: {len(files)}.')
        print('\n------------------------------------sorting Files-----------------------------')
    else:
        print('Files Found: 0. No files to sort. Exiting...')
        return
    
    
    
    for file in os.listdir(PATH_DOWNLOADS):
    
        # Get File Category (Based on rules)    
        dir_name = get_file_cat(file)
        
        if dir_name:
            
            # Create Sorting Folders
            dir_filepath = os.path.join(PATH_DOWNLOADS, dir_name)
            if not os.path.exists(dir_filepath):
                os.makedirs(dir_filepath)
                
            # Define Old and New Paths
            old_path = os.path.join(PATH_DOWNLOADS, file)
            new_path = os.path.join(dir_filepath, file)
            
            # Move files
            try:
                shutil.move(old_path, new_path)
                print(f'> Moved File: {file} /s {dir_name}')
                count +=1
            except Exception as e:
                print(f'! Error Moving File: {file} to {dir_name} - {e}')
                fails += 1
                
    # Final Report
    if count:
        print(f'SUCCESSFULLY SORTED {count} FILES!')
    
    if fails:
        print('-' * 60)
        print(f'FAILED TO SORT {fails} FILES!')
        for msg in faild_msgs:
            print(msg)



# Main method
if __name__ == "__main__":
    sort_downloads()

# Bonus: Create CMD Shortcut to Run Scripts




