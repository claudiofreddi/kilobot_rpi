from setuptools import find_packages, setup

package_name = 'kilobot_rpi'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='claudio',
    maintainer_email='git@claudiofreddi.eu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = kilobot_rpi.my_node:main',
            'cmd_to_pwm_driver = kilobot_rpi.cmd_to_pwm_driver:main'
        ],
    },
)
