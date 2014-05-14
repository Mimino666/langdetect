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
    version='0.1.0',
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
    ]
)
