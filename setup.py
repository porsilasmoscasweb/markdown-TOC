from setuptools import setup, find_packages

setup(
    name='el_meu_projecte',
    version='0.1',
    packages=find_packages(),
    install_requires=[  # Si la teva llibreria té dependències
        # 'numpy', 'requests', etc.
    ],
    description='Descripció breu de la teva llibreria',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='El teu nom',
    author_email='el_teu_email@domini.com',
    url='https://github.com/usuari/el_meu_projecte',  # URL del teu repositori de GitHub
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Si estàs utilitzant la llicència MIT
        'Operating System :: OS Independent',
    ],
)
