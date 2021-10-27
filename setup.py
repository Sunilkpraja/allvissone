from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.MD"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.1'
DESCRIPTION = 'All Data Science Visualization package in single line'
LONG_DESCRIPTION = 'A package that allow you to install all visualization packages in single line of code and save your time.'

# Setting up
setup(
    name="allvissone",
    version=VERSION,
    author="Sunilkpraja",
    author_email="sunilkumar.prajapati9689@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['matplotlib', 'seaborn', 'bokeh', 'altair', 
                      'plotly','ggplot','pygal'
                     ],
    keywords=['matplotlib', 'seaborn', 'bokeh', 'altair', 'Plotly','ggplot','pygal','Data Science', 'Package','Data science all visualization packages', 'Package', 'allvissone'],
    url='https://github.com/Sunilkpraja/allvissone',
    include_package_data=True,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    zip_safe=True,
)
