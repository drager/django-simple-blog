import os

from setuptools import setup

version = __import__('simpleblog').get_version()

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name = 'django-simple-blog',
    version = version,
    packages = ['simpleblog'],
    include_package_data = True,
    install_requires = [line for line in read('requirements.txt').split('\n')
                        if line and not line.startswith('#')],
    license = 'BSD License',
    description = 'An easy way to start writing blog posts.',
    long_description = readme,
    url = 'https://github.com/Drager/django-simple-blog',
    author = 'Drager',
    author_email = 'drager@programmers.se',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
