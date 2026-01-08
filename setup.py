from setuptools import setup, find_packages
from typing import List
requirements=[]
def get_requirements(file:str)->List[str]:
    with open(file) as f:
        for line in f:
            line=line.strip()
            if line !='-e .':
                requirements.append(line)
    return requirements
setup(
    name='Fahim Hasan',
    version='0.0.1',
    author='Fahim Hasan',
    author_email='hasanfahim0101@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)