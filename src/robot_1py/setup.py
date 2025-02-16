from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'robot_1py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf.xacro')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.xml')),
        (os.path.join('share', package_name, 'config'), glob('config/*.rviz')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.xacro')),
        (os.path.join('share', package_name, 'urdf'), glob('comm_prop.xacro')),
        (os.path.join('share', package_name, 'urdf'), glob('mob_gaxebo.xacro')),
        (os.path.join('share', package_name, 'urdf'), glob('camera.xacro')),
        (os.path.join('share', package_name, 'urdf'), glob('arm.xacro')),
        (os.path.join('share', package_name, 'urdf'), glob('standalone.urdf.xacro')),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='asus',
    maintainer_email='asus@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "draw_circle = robot_1py.circle_robot:main",

        ],
    },
)

