from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name = 'luckysocial',
    version = '0.0.2',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    url = 'https://github.com/edsu/luckysocial',
    py_modules = ['luckysocial',],
    description = 'lookup social media accounts for names',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires = ['requests_html'],
    setup_requires=['pytest-runner'],
    tests_require = ['pytest'],
    entry_points = {'console_scripts': ['luckysocial = luckysocial:main']},
)
