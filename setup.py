import setuptools


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="QMVVM",
    version="0.0.3",
    keywords="qt pyqt pyside mvvm",
    author="zhiyiYo",
    author_email="shokokawaii@outlook.com",
    description="A Model-View-ViewModel(MVVM) framework for Qt",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="Apache-2.0",
    url="https://github.com/zhiyiYo/QMVVM",
    packages=setuptools.find_packages(),
    install_requires=[
        "qtpy",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent'
    ],
    project_urls={
        'Documentation': 'https://github.com/zhiyiYo/QMVVM',
        'Source Code': 'https://github.com/zhiyiYo/QMVVM',
        'Bug Tracker': 'https://github.com/zhiyiYo/QMVVM/issues',
    }
)
