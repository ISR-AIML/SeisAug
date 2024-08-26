from setuptools import setup, find_packages

setup(
    name='seisaug',
    version='1.0',
    author="ISR-AIML",
    author_email="isr3aiml@gmail.com",
    description="A Comprehensive Data Augmentation Python Toolkit for Deep Learning.",
    url="https://github.com/ISR-AIML/SeisAug",
    license="MIT",
    packages=find_packages(),
    keywords=['Seismology', 'Earthquakes', 'Deep Learning', 'Data Augmentation'],
    install_requires=['obspy', 'matplotlib', 'scipy~=1.10.0', 'jupyter', 'ipywidgets']
)
