from setuptools import setup


with open('README.md') as f:
    readme = f.read()


setup(
    name='langdetect',
    version='1.0.8',
    description='Language detection library ported from Google\'s language-detection.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Michal Mimino Danilak',
    author_email='michal.danilak@gmail.com',
    url='https://github.com/Mimino666/langdetect',
    keywords='language detection library',
    packages=['langdetect', 'langdetect.utils', 'langdetect.tests'],
    include_package_data=True,
    python_requires='>=3.6',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ]
)
