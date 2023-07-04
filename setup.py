from setuptools import find_packages, setup

requirements_txt = 'requirements.txt'
REMOVE_PACKAGE = '-e .'


def get_requirements() -> list[str]:
    with open(requirements_txt) as req_file:
        req_list = req_file.readline()
    req_list = [req_name.replace('\n', '') for req_name in req_list]

    if REMOVE_PACKAGE in req_list:
        req_list.remove(REMOVE_PACKAGE)
    return req_list


setup(
    name='Project Name',
    version='0.0.1',
    description="Project description",
    author='Author Name',
    author_email='author.email@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
