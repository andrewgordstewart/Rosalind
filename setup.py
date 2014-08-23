try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'name': 'rosalind',
	'description': 'Rosalind programming challenges',
	'author': 'Andrew Stewart',
	# 'url': 'URL to get it at.',
	'download_url': 'Where to download it',
	'author_email': 'kaptain.kayak@gmail.com',
	# 'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['rosalind']
	# 'scripts': ['bin'],
}

setup(**config)
