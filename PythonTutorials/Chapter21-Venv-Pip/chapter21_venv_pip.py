# Pip : Prefered Installer Program
# or
# PIP install packages

# PIP - lets us install packages in our programs that are not already included in Python like Math module and etc....

# to install anything via pip - pip install <package name> or
                                # python3 -m pip install <package name>
                                
# if we have not enabled virtual env then it is a global install i.e., available to all of python projects.

# to see what things have u install with pip, just hit/enter : pip list

# we can also install a specific version of a module too...
# ----> pip install requests==2.30.0 


# when u have installed a lower version of package and now u want to update it then
# ====> pip install -U requests : update ny requests package to what so ever current release is...

# to uninstall:
# pip uninstall requests


# ################################################################################################################

# There can be more than 1 python applications runing on a system 
# also we can have a situation where 1 python app needs specific version of module and another needs some other version of same module.
# and as pip install updates globally means that can impact every python program...so how to deal with it.

# virtual env helps in this issue and also it is a general norm to not include them in github repo.

# to create a virtual environment, use: 
# python3 -m venv .venv
# source .venv/bin/activate  <--- to activate the v env..

# u create once but have to activate it as when u need to work on your project.

# to deactivate the virtual env, use deactivate...

# to see details about any package, pip show requests
# dependencies installed by pip can be seen in .venv folder iin lin/python3.10/site_packages

# pypi.org is a website which has Python Package Index -- here u can search for packages to use inside our applications.

# we can or must put the requirements file in github, to generate one: pip freeze > requirements.txt
# we can directly install these modules via :


# to exclude the files which u dont wanna include in git/github: we can create a .gitignore file (works with git/github)

# .env --> environment variable file, used in devlopement. Never send it to Github as it contains our secrets