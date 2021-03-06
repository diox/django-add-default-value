# Copyright 2018 3YOURMIND GmbH

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from codecs import open
from os import path
from setuptools import setup, find_packages


PROJECT_DIR = path.abspath(path.dirname(__file__))

with open(path.join(PROJECT_DIR, 'README.md'), 'r') as f:
    long_description = f.read()

install_requirements = [
    'Django>=1.10,<2.1'
]

setup(
    name='django-add-default-value',
    version='0.0.8',

    description='This django Migration Operation can be used to transfer'
                ' a fields default value to the database scheme.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/3YOURMIND/django-add-default-value',
    author='3YOURMIND GmbH',
    license='Apache License 2.0',

    packages=['django_add_default_value'],
    install_requires=install_requirements,

    keywords='django migration dafault database backward compatibility',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
