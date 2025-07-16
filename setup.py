from setuptools import setup

setup(
    name='sys-snippet',
    version='0.1',
    py_modules=['sys_snippet'],
    entry_points={
        'console_scripts': [
            'sys-snippet = sys_snippet:main',
        ],
    },
    author='Your Name',
    description='Minimal CLI to display system info in terminal or as ready-to-paste README markdown.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
