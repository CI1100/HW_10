from distutils.core import setup

with open("README.txt", "r") as fh:
    long_description = fh.read()

setup(
    name="CEBD-1100-Week-10", # Replace with your own username
    version="0.1.0",
    author="Olga",
    author_email="Olga@example.com",
    description="Creation of packages for projects HW8 and HW9",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CI1100/HW_10",
    license= 'LICENSE.txt',
    packages= ['final_project_packages', 'final_project_packages.test'],
    scripts = ['bin/HW_8.py', 'bin/kmeans_iris.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
) 