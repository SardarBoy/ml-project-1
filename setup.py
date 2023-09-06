from setuptools import find_packages , setup
from typing import List


def get_requirements(file_path:str) -> list[str]:

    requirements = []
    with open (file_path) as file_obj:    #inputting file path 
        requirements = file_obj.readlines()  # func will read all the lines 
        requirements = [ req.replace('\n',"") for req in requirements]    #as text is in new lines,
    
    return requirements     

setup(
name = "Ml project",
version = '0.0.1',
author= "gurtej",
author_email='garykhokhar2000@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt')
)