import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'py_examples'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='carlos',
    maintainer_email='menachocarlos5@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publipy = py_examples.pub:main',
            'subpy = py_examples.sub:main',
            'server = py_examples.service_py_example:main',
            'client = py_examples.client_py_example:main',
            'pos_server = py_examples.position_service:main',
            # py_examples/py_examples/position_service.py
            'pos_client = py_examples.position_client:main',
        ],
    },
)
