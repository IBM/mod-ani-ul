import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

install_requires = [
    "ase==3.22.1",
    "bayesian-torch==0.2.0",
    "h5py==3.6.0",
    "matplotlib==3.5.0",
    "pandas==1.3.5",
    "protobuf==3.19.3",
    "torch==2.13.0",
    "tensorboard==2.8.0",
    "tqdm==4.62.3",
    "torchani==2.2",
    "uncertainty-toolbox==0.1.0",
    "seaborn==0.11.2"
]

#  (Modified ANI with Uncertainty Levels)
setuptools.setup(
    name="maul",
    version="1.0",
    author="James McDonagh, Clyde Fare, Ravikanth Tadikonda and Zeynep Sumer",
    author_email="james.mcdonagh@uk.ibm.com, clyde.fare@ibm.com, ravikanth.tadikonda@stfc.ac.uk and zsumer@ibm.com"
    description="BNN version of the ANI neural potential library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license="All rights reserved",
    classifiers=[
        "Programming Language :: Python :: 3.9"
    ],
    install_requires=install_requires
)
