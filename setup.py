from multiprocessing.connection import Listener
from setuptools import setup

package_name = 'first_pkg'

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
    maintainer='abhinav',
    maintainer_email='abhinav@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [  'Say_hello = first_pkg.py_talker:main',
        'bolo = first_pkg.news_station:main',
        'talker_2=first_pkg.2nd_news_station:main'
        ,'Listener=first_pkg.sub:main'
        ,"read=first_pkg.led_cont:main",
        "talker_3=first_pkg.talker_3:main"
        
        ],
    },
)
