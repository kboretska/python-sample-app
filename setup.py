setup(
    name='python-sample-app-kboretska',  # Унікальна назва пакета
    version='1.0',
    description='Python Sample App - Starter Template',
    author='Kateryna Boretska',
    author_email='your.email@example.com',
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
