from setuptools import setup, find_packages

setup(
    name="SegundapreentregaNapolitano",
    version="1.0",
    description="Paquete redistribuible",
    author="Esteban Napolitano",
    author_email="e.napo_esteban@hotmail.com",
    packages=find_packages(where="./src", exclude=("./tests",))
)