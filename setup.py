from setuptools import setup

setup(
    name = 'luckysocial',
    version = '0.0.1',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    url = 'https://github.com/edsu/luckysocial',
    py_modules = ['luckysocial',],
    description = 'lookup social media accounts for names',
    install_requires = ['requests_html'],
    setup_requires=['pytest-runner'],
    tests_require = ['pytest'],
    entry_points = {'console_scripts': ['luckysocial = luckysocial:main']},
)
