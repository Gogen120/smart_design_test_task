import os
import re

from setuptools import find_packages, setup


def read_version():
    regexp = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")
    init_py = os.path.join(
        os.path.dirname(__file__),
        'smart_design_store', '__init__.py'
    )
    with open(init_py) as f:
        for line in f:
            match = regexp.match(line)
            if match is not None:
                return match.group(1)
        else:
            msg = 'Cannot find version in motortwit/__init__.py'
            raise RuntimeError(msg)


install_requires = [
    'aiohttp==3.6.2',
    'umongo[motor]==2.2.0',
    'marshmallow==2.21.0',
    'pytest==5.4.1',
    'pytest-cov==2.8.1',
    'pytest-aiohttp==0.3.0',
    'mongomock==3.19.0',
]


setup(
    name='smart_design_store',
    version=read_version(),
    description='Test task for smart design',
    platforms=['POSIX'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False
)