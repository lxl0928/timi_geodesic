# timi_geodesic
根据传入待测点坐标，所有已知坐标点，返回待测点坐标到所有已知坐标点的距离，并按距离升序输出该待测点到各已知坐标点的距离

# install 
```
pip install timi-geodesic
```

# examples

```
    >>> from timi_geodesic import geodesic


    >>> geodesic.get_distance_detail_info(
        input=(123.123, -12.21),
        coordinates=[
            (1, 123.123, -12.21, 0),
            (2, 89.98, 14.31, 0),
            (3, 90.23, 14.31, 0),
            (4, 10.88, 14.31, 0)
        ]
    )
    
    >>> [
            (),
            (),
            (),
            ()
        ]

```
