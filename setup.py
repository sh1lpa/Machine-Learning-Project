from setuptools import find_packages, setup
from typing import List

HYFEN_E_DOT = '-e.'
def get_requirements(file_path:str)->List[str]:
    '''
        this function will return the list of required packages
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=[pack.replace('\n','') for pack in  file_obj.readlines()]
        if HYFEN_E_DOT in requirements: requirements.remove(HYFEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author='Shilpa',
    author_email='shilpashinde25@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


print(get_requirements('requirements.txt'))