from distutils.core import setup

import montefiore_printer

NAME = 'montefiore_printer'
VERSION = montefiore_printer.__version__
AUTHOR = "Jean-Michel Begon"
AUTHOR_EMAIL = "jm.begon@gmail.com"
URL = 'https://github.com/jm-begon/montefiore_printer'
DESCRIPTION = 'Utility for printing at monrefiore'
with open('README.md') as f:
    LONG_DESCRIPTION = f.read()
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Console',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Education',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Topic :: Utilities',
]

if __name__ == '__main__':
    setup(name=NAME,
          version=VERSION,
          author=AUTHOR,
          author_email=AUTHOR_EMAIL,
          url=URL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license='BSD3',
          classifiers=CLASSIFIERS,
          platforms='any',
          install_requires=[],
          packages=['montefiore_printer'],
          scripts=['bin/print_montef'])

