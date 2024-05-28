from setuptools import setup, find_packages

setup(
    name='SeismoAugment',  # Replace with your project name
    version='0.1.0',  # Set your project version
    url='https://github.com/ISR-AIML/SeismoAugment',  # GitHub repository URL
    description='A package for seismic data augmentation',
    packages=find_packages(),  # Automatically find all packages in your project
    install_requires=[
        'obspy',  # Seismic data processing library
        'matplotlib',  # Plotting library
        'scipy~=1.10.0',  # Scientific computing library (specific version)
        'jupyter',  # Interactive notebooks
        'ipywidgets',  # Interactive widgets for Jupyter
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

