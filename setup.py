import setuptools

setuptools.setup(
    name="manojextension",
    version='0.1.0',
    url="https://github.com/manoj1103/manojextension",
    author="Manoj and sai",
    description="Adding pre-load python libraries to notebook",
    packages=setuptools.find_packages(),
    install_requires=[
        'psutil',
        'notebook',
        'gitpython'
    ],
    package_data={'manojextension': ['static/*']},
)
