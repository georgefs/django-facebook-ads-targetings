import os


from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'README.md')) as f:
    README = f.read()


REQUIREMENTS = [
        'facebook_login'
]

setup(
    name='facebook_ads_targetings',
    version='0.1',
    description='Tagtoo ec parser',
    author='lucemia',
    author_email='george.li@tagtoo.co',
    long_description=README,
    scripts=[],
    url='https://github.com/georgefs/django-facebook-ads-targetings',
    packages=find_packages(),
    license='Apache 2.0',
    platforms='Posix; MacOS X; Windows',
    include_package_data=True,
    zip_safe=False,
    dependency_links=['https://github.com/rasca0027/django_facebook_server_login/tarball/master#egg=facebook_login'],
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
    ]
)
