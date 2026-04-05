import os
import shutil
from CONSTANTS import *

def main():
    
    clear_output_directory()
    copy_static_files()


def clear_output_directory():
    dir_output = OUTPUT_DIR
    
    for filename in os.listdir(dir_output):
        file_path = os.path.join(dir_output, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
    
    print(f"Cleared {dir_output} directory.") 
    
def copy_static_files():
    dir_source = SOURCE_DIR
    dir_output = OUTPUT_DIR
    
    for filename in os.listdir(dir_source):
        source_file_path = os.path.join(dir_source, filename)
        output_file_path = os.path.join(dir_output, filename)
        if os.path.isdir(source_file_path):
            copy_dir(source_file_path, output_file_path)
        elif os.path.isfile(source_file_path):
            shutil.copy2(source_file_path, output_file_path)
            
    
    print(f"Copied static files from {dir_source} to {dir_output}.")

def copy_dir(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isdir(src_path):
            copy_dir(src_path, dst_path)  # recursion
        else:
            shutil.copy2(src_path, dst_path)  # copy file with metadata
   
if __name__ == "__main__":
    main()
    
    