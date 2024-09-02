from setuptools import setup, find_packages

# Lendo o conteúdo do README.md para usar como descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="enigma",  # Substitua pelo nome do seu pacote
    version="0.1.0",
    author="Ricardo Luz Carvalho, Vinicius Leal Silva",
    author_email="ricardolc2@al.insper.edu.br, viniciusls2@al.insper.edu.br",
    description="Um pacote que implementa a cifra enigma",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RicardolCarvalho/enigma.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            'enigma=enigma.main:main',
        ],
    },
    install_requires=[
        line.strip() for line in open("requirements.txt").readlines()
    ],
)