from setuptools import setup

install_requires = [
    'Flask==0.12.2',
    'Jinja2==2.10',
    'MarkupSafe==1.0',
    'SQLAlchemy==1.2.2',
    'Werkzeug==0.14.1',
    'click==6.7',
    'itsdangerous==0.24',
    'mysql-connector-python==8.0.6',
    'pip==9.0.1',
    'setuptools==28.8.0'
    ]

setup(
    name='python-flask',
    version='0.1',
    packages=['python-flask'],
    url='',
    license='',
    author='kjyz1125',
    author_email='',
    description='',
    include_package_data=True,
    install_requires=install_requires
)
