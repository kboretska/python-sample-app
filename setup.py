from setuptools import setup

# Використовується для опису пакета на PyPI
with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='python-sample-app-kboretska',  
    version='1.0.3',  # Якщо така версія вже є, підніми (1.0.2 і т.д.)
    description='Python Sample App - Starter Template',
    author='Kateryna Boretska',
    author_email='k.boretska@gmail.com',
    license="MIT",
    url="https://github.com/kboretska/python-sample-app",
    packages=['python_sample_app'],
    entry_points={
        'console_scripts': [
            'sample-app=python_sample_app.main:main',
        ],
    },
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown"
)
