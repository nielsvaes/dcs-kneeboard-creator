from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

# any data files that match this pattern will be include in the build
data_files_to_include = ["*.png", "*.jpg", "*.tga", "*.tiff"]

setup(
    name='dcs-kneeboard-creator',
    version='1.0.0',
    packages=find_packages(),
    package_data={
        "": data_files_to_include,
    },
    url='https://github.com/nielsvaes/dcs_kneeboard_creator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    author='Niels Vaes',
    author_email='nielsvaes@gmail.com',
    description='Tool to quickly create and add knee boards to DCS World',
)
