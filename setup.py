from distutils.core import setup

setup(name='dummytest',
      version='0.0.1',
      description="Example package",
      url='',
      author='Ferenc Beres',
      author_email='fberes@info.ilab.sztaki.hu',
      packages=['dummytest'],
      install_requires=[
          'numpy',
          'pandas',
          'matplotlib',
          'seaborn',
      ],
      zip_safe=False
)
