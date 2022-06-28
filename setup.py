from setuptools import setup, find_packages


setup(
    name='IDS347L - Samuel Charles - Erickson Nuñez - Kata Team Session',
    version='0.6',
    license='MIT',
    author="Samuel Charles, Erickson Nuñez",
    author_email='samyrd309@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/samyrd309/Kata-session-team/tree/master/src',
    keywords='Kata Team Session',
    install_requires=[
          'scikit-learn',
      ],

)