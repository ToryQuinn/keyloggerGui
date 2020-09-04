"""
Uses DNSBL to lookup reputation on IOCs
"""
from setuptools import find_packages, setup

dependencies = ['keyboard']

setup(
    name='keyloggerGui',
    version='0.0.1',
    url='https://github.com/troykkt/keyloggerGui',
    license='BSD',
    author='Troy Kent',
    author_email='troykkt@gmail.com',
    description='Creates a Keylogger That Outputs to a GUI for great fun!',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'klg = src.keyloggerGui.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
