from setuptools import find_packages, setup
from typing import List
HYPHON_E_DOT= "-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","")for req in requirements]
        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)
setup (
    name='mlprojects',
    version='0.0.1',
    author='Priyanshu',
    author_email='priyanshusahay489@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)