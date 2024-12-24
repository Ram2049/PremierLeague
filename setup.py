from setuptools import setup,find_packages
from typing import List

def get_requiremnts(file_path:str)->List[str]:
    '''
    THIS FUNCTION WILL RETURN THE LIST OF REQUIREMENTS
    
    '''
    hypen_e_dot = '-e .'
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if hypen_e_dot in requirements:
           requirements.remove(hypen_e_dot)
    
    return requirements

setup(
    name="PremierLeague-predictor",                   # Name of the package
    version="0.0.0",                     # Version of the package
    author="Ram",                  # Author name
    author_email="ramsparttakas23@gmail.com",  # Author email
    description="A short description of the project",  # Short description
    long_description=open("README.md").read(),  # Long description from README
    long_description_content_type="text/markdown",  # Content type of the long description
    url="https://github.com/yourusername/my_project",  # URL of the project repository
    packages=find_packages(),            # Automatically find all packages in the project
    install_requires=get_requiremnts('requirements.txt')                   # Dependencies

)
