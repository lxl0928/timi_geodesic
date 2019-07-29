# coding: utf-8

from geodesic import geodesic


class TestTimiGeodesic(object):

    def test_get_distance_id_list(self):
        result = geodesic.get_distance_id_list(
            input=(123.123, -12.21),
            target_points=[
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
            input=(123.123, -12.21),
            target_points=[
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
            input=(123.123, -12.21),
            target_points=[
                (1, 123.123, -12.21, 0),
                (2, 89.98, 14.31, 0),
                (3, 90.23, 14.31, 0),
                (4, 10.88, 14.31, 0)
            ],
            sort='asc'
        )
        print(result)


