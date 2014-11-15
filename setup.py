from setuptools import setup
import os, shutil

version = '0.2'

setup(version=version,
      name='greenthink',
      description = "greenthink",
      packages = [
            "Gthnk",
            "Gthnk.journal",
            "Gthnk.dashboard",
            ],
      scripts = [
            "bin/runserver.py",
            "bin/manage.py",
            "bin/journal_rotate.py",
            #"bin/journal_actions.py",
      ],
      long_description="""greenthink-library""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      include_package_data = True,
      keywords='',
      author='Ian Dennis Miller',
      author_email='ian@iandennismiller.com',
      url='http://www.iandennismiller.com',
      dependency_links = [
            'https://github.com/iandennismiller/Flask-Diamond/archive/0.1.7.tar.gz#egg=flask_diamond-0.1.7',
            ],
      install_requires = [
            ### app
            "flask_diamond==0.1.7",
            "mdx-linkify==0.2",
            "Markdown==2.3.1",
            "poodledo>=0.2",
            "mdx-journal==0.1", # http://github.com/iandennismiller/mdx_journal

            ### other flask niceness

            "pyScss==1.2.0.post3",
            "wheel==0.24.0",
            "Flask-RESTful==0.2.12",
            "lxml==3.4.0",
            "requests==2.4.1",
            "cssselect==0.9.1",
            "Flask-DbShell==1.0",
            "python-dateutil==2.2",


            ### databases
            "SQLAlchemy==0.9.3",
            "Flask-SQLAlchemy>=1.0",
            "SQLAlchemy-Utils==0.24.1",
      ],
      license='Proprietary',
      zip_safe=False,
)
