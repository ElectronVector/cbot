from setuptools import setup

setup(name='cbot',
      version='0.1.0',
      description='CMake build and test assistant',
      long_description='A tool for automating manual steps and generating code when unit testing C language '
                       'CMake-based projects.',
      url='https://github.com/ElectronVector/cbot',
      author='Matt Chernosky',
      author_email='matt@electronvector.com',
      license='MIT',
      packages=['cbot'],
      entry_points={
            'console_scripts': ['cbot=cbot.cbot:cli'],
      },
      zip_safe=False)