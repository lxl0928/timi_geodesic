from setuptools import setup

setup(
    name="timi-geodesic",
    version="1.1.0",
    url='http://github.com/lxl0928/timi_geodesic',
    author='Timi long',
    author_email='lixiaolong@smuer.cn',
    description='根据传入待测点坐标，所有已知坐标点，返回待测点坐标到所有已知坐标点的距离，并按距离升序输出该待测点到各已知坐标点的距离',
    long_description="""根据传入待测点坐标，所有已知坐标点，返回待测点坐标到所有已知坐标点的距离，并按距离升序输出该待测点到各已知坐标点的距离""",
    packages=['geodesic'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
