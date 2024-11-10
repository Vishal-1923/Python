# *************************************************** Shutil Module ****************************************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/87-Day-87-Shutil-Module/.tutorial/Tutorial.md

# shutil is built in module

'''
shutil.copy(src, dst): This function copies the file located at src to a new location specified by dst. If the destination location already exists, the original file will be overwritten.

shutil.copy2(src, dst): This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.

shutil.copytree(src, dst): This function recursively copies the directory located at src to a new location specified by dst. If the destination location already exists, the original directory will be merged with it.

shutil.move(src, dst): This function moves the file located at src to a new location specified by dst. This function is equivalent to renaming a file in most cases.

shutil.rmtree(path): This function recursively deletes the directory located at path, along with all of its contents. This function is similar to using the rm -rf command in a shell.
'''
import shutil as s 

s.copy("day87.py", "day87.py-ex")

s.copytree("day68_helperFolder", "day87_helperFolder_shutil-copytree-ex")

s.rmtree("day87_helperFolder_shutil-copytree-ex")