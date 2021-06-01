from setuptools import setup

setup(
  name='smartlibot',
  version='0.0.1',
  author='smartlichessbot',
  author_email='smartlichessbot@gmail.com',
  description='play on lichess with a bot',
  long_description='Play on lichess with a bot.',
  license='MIT',
  keywords="play lichess bot",
  url='https://github.com/smartlichessbot/smartlibot',            
  packages=['smartlibot'],
  test_suite="test",
  python_requires=">=3.6",
  install_requires=[              
    "python-chess==0.23.5",
    "PyYAML==3.12",
    "requests==2.18.4",
    "urllib3==1.26.5",
    "backoff==1.5.0"
  ],
  classifiers=[        
    "Programming Language :: Python :: 3.6"
  ],
  entry_points={
    
  },
  package_dir={
    'smartlibot': 'smartlibot'
  },
  include_package_data=False,
  zip_safe=False
)
