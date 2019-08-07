# timi_geodesic
根据传入待测点坐标，所有已知坐标点，返回待测点坐标到所有已知坐标点的距离，并按距离升序输出该待测点到各已知坐标点的距离

# install 
```
pip install timi-geodesic==1.1.0
```

# examples

```python
# coding: utf-8

from geodesic import (
    get_distance_with_detail,
    get_distance_with_dict,
    get_distance_with_list
)


class TestTimiGeodesic(object):

    def test_get_distance_id_list(self):
        """
        :param: inpuut_corrdinate: <tuple> 当前坐标点, 如当前待测点
        :param: coordinates: [<tuple>]  已知的各目标点
        :param: sort: <str>  'asc' or 'desc'  排序方式

        :return: 该待测点到各已知点按距离排序
        """

        result = get_distance_with_list(
            input_coordinate=(123.123, -12.21),
            coordinates=[
                (1, 123.123, -12.21, 0),
                (2, 89.98, 14.31, 0),
                (3, 90.23, 14.31, 0),
                (4, 10.88, 14.31, 0)
            ],
            sort='asc'
        )
        print(result)
        """
        [
            (1, 123.123, -12.21, 0.0),
            (3, 90.23, 14.31, 4672.014658127451),
            (2, 89.98, 14.31, 4693.407128885379),
            (4, 10.88, 14.31, 12704.366004534697)
        
        ]
        """

    def test_get_distance_detail_info(self):
        result = get_distance_with_detail(
            input_coordinate=(123.123, -12.21),
            coordinates=[
                (1, 123.123, -12.21, 0),
                (2, 89.98, 14.31, 0),
                (3, 90.23, 14.31, 0),
                (4, 10.88, 14.31, 0)
            ],
            sort='asc'
        )
        print(result)
        """
        [1, 3, 2, 4]
        """

    def test_get_distance_id_dict(self):
        result = get_distance_with_dict(
            input_coordinate=(123.123, -12.21),
            coordinates=[
                (1, 123.123, -12.21, 0),
                (2, 89.98, 14.31, 0),
                (3, 90.23, 14.31, 0),
                (4, 10.88, 14.31, 0)
            ],
            sort='asc'
        )
        print(result)
        """
        [
            {1: 0.0},
            {3: 4672.014658127451},
            {2: 4693.407128885379},
            {4: 12704.366004534697}
        ]
        """



```
