from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='localStoragePy',
      version='0.2.0',
      description='A familiar API from the Web, adapted to storing data locally with Python.',
      url='http://github.com/jkelol111/localStoragePy',
      author='Nguyen Thanh Nam (jkelol111)',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author_email='jkelol111@gmail.com',
      license='MIT',
      packages=['localStoragePy'],
      classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
      ],
      zip_safe=False
)

