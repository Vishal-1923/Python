# ***************************************** Virtual Environment ********************************************

# A virtual environment is a tool used to isolate specific Python ennvironments on a single machine, allowing you to work on multiple projects with diff. dependencies and packages without conflicts.

# Usefull especially when working on projects that have conflicting package versions/packages that are not compatible with each other.

# creating virtual environment: venv module (built-in in Python)
python3 -m venv myenv

'''
Sometimes after executing this command, u will get an error like this
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    sudo apt install python3.10-venv

follow above command and u r good to go.
'''

# activate virtual environment (linux/macos)
source myenv/bin/activate

# activate virtual environment (windows)
# myenv\Scripts\activate.bat

# myenv is basically a copy of python which is installed globally
# we can make as many as possible 

# we can even install particular version of any package.
# pip3 install pandas==1.4.4

# we can check package version via : 
# import pandas as pd
# pd.__version__pip install --upgrade numpy pandas

# if u get this kind of error : numpy.dtype size changed, may indicate binary incompatibility. Expected 96 from C header, got 88 from PyObject
# this means there is mismatch between numpy and pandas.
# pip install --upgrade numpy pandas
# via runing this issue will be resolved i.e., we r basically updating pandas and numpy

# deactivating python virtual env
deactivate #write this and ur virtual env is now off.


# we can even name our virtual env:
python3 -m venv yourname

# requirement.txt file
# this file is created and shared to devlopers
# contains packages and their versions 
pip freeze #will list all the packages and their versions

pip freeze > requirements.txt #will create a requirement.txt file and will store info in it.

pip install -r requirements.txt #will install all the listed packages.