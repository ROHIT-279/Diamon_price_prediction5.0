from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        return requirements


setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Rohit',
    author_email='jdipankar34@gmail.com',
    install_requires=get_requirements('/config/workspace/requirements.txt'),
    packages=find_packages()

)