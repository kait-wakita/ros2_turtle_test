from setuptools import setup

package_name = 'ros2_turtle_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wakita',
    maintainer_email='wakita@cco.kanagawa-it.ac.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move = ros2_turtle_test.moveTurtle:main',
            'spawn = ros2_turtle_test.spawnTurtle:main',
            'rotate = ros2_turtle_test.rotateTurtle:main',
        ],
    },
)
