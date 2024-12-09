from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

"""
 This function will return the list of requirements
"""

def get_requirements(file_path:str)->List[str]:




  
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters
        requirements = [req.replace("\n","") for req in requirements]
        
        # Remove '-e .' if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='salina',
    author_email='aktersalina242@gmail.com',
    packages=find_packages(),
   install_requires=get_requirements('requirements.txt')


)