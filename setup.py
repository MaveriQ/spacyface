from setuptools import setup, find_packages

requires = [
    'transformers>=2.3.0',
    'h5py>=2.10.0',
    'numpy>=1.17.4',
    'regex>=2020.1.8',
]

setup(
    name="spacyface",
    description="Aligner for spacy and huggingface tokenization",
    packages=['spacyface'],
    version='0.1.1',
    license='MIT',
    author="Ben Hoover",
    author_email="benjamin.hoover@ibm.com",
    url="https://github.com/bhoov/spacyface",
    download_url = 'https://github.com/bhoov/spacyface/archive/v0.1.1.tar.gz',
    keywords=["transformer", "pytorch", "spacy", "tokenize", "tokenization", "NLP", "Natural Language Processing",
              "huggingface", "linguistic"],
    include_package_data=True,
    install_requires=requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        ]
)
