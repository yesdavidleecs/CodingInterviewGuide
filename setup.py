from setuptools import setup, find_packages

setup(
    name="leetcode-test-framework",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your framework needs
    ],
    entry_points={
        'console_scripts': [
            'run-leetcode=codingproblems.cli:main',
        ],
    },
)
