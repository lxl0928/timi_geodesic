# coding: utf-8

from geodesic import geodesic


class TestTimiGeodesic(object):

    def test_get_distance_id_list(self):
        result = geodesic.get_distance_id_list(
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

    def test_get_distance_detail_info(self):
        result = geodesic.get_distance_detail_info(
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

    def test_get_distance_id_dict(self):
        result = geodesic.get_distance_id_dict(
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


obj = TestTimiGeodesic()
obj.test_get_distance_detail_info()
obj.test_get_distance_id_dict()
obj.test_get_distance_id_list()

"""
[(1, 123.123, -12.21, 0.0), (3, 90.23, 14.31, 4672.014658127451), (2, 89.98, 14.31, 4693.407128885379), (4, 10.88, 14.31, 12704.366004534697)]
[{1: 0.0}, {3: 4672.014658127451}, {2: 4693.407128885379}, {4: 12704.366004534697}]
[1, 3, 2, 4]
"""