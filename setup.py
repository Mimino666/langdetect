try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()


setup(
    name='langdetect',
    version='1.0.7',
    description='Language detection library ported from Google\'s language-detection.',
    long_description=readme,
    author='Michal Mimino Danilak',
    author_email='michal.danilak@gmail.com',
    url='https://github.com/Mimino666/langdetect',
    keywords='language detection library',
    packages=['langdetect', 'langdetect.utils', 'langdetect.tests'],
    include_package_data=True,
    install_requires=['six'],
    license=license,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ]
)
