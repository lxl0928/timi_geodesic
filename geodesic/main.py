# coding: utf-8

from math import sin, radians, cos, asin, sqrt


class TimiGeodesic(object):
    """ 根据输入的坐标信息，返回待测点到各点的距离，按近，到远排序

    """

    @staticmethod
    def __haversine(lon1, lat1, lon2, lat2):
        """

        :param lon1: 待测点经度
        :param lat1: 待测点维度
        :param lon2: 目标点经度
        :param lat2: 目标点维度
        :return:
        """
        # radians 角度转弧度
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))  # 反正弦
        r = 6371
        return c * r

    def get_distance_detail_info(self, input, target_points, sort='asc'):
        """
        geodesic = TimiGeodesic()

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
        # [(1, 123.123, -12.21, 0.0), (3, 90.23, 14.31, 4672.014658127451), (2, 89.98, 14.31, 4693.407128885379), (4, 10.88, 14.31, 12704.366004534697)]


        :param input: <tuple>, (123.12, -10.01), 待测点坐标
        :param target_points:  <list>, [(, , , ),...], 目标点的坐标集
        :param sort: <str>, 'asc' or 'desc', 排序方式
        :return:
        """
        assert sort in ('asc', 'desc'), ValueError('param sort value error, support: asc or desc.')
        assert isinstance(input, tuple), TypeError(
            'param input type error, support type is tuple(), example as: (123.21, -10.21)')
        assert isinstance(target_points, list), TypeError(
            "param target_points type error, support type is list(),"
            "example as: [('id', 'longitude', 'latitude', 'distance')]")

        new_points = []
        for inx, point in enumerate(target_points):
            _id, longitude, latitude, distance = point
            distance = self.__haversine(lon1=input[0], lat1=input[1], lon2=longitude, lat2=latitude)
            new_points.append((_id, longitude, latitude, distance))

        if sort == 'asc':
            new_points = sorted(new_points, key=lambda x: x[-1], reverse=False)
        else:
            new_points = sorted(new_points, key=lambda x: x[-1], reverse=True)

        return new_points

    def get_distance_id_list(self, input, target_points, sort='asc'):
        points = self.get_distance_detail_info(
            input=input, target_points=target_points, sort=sort
        )
        return [item[0] for item in points]

    def get_distance_id_dict(self,  input, target_points, sort='asc'):
        points = self.get_distance_detail_info(
            input=input, target_points=target_points, sort=sort)

        return [{item[0]: item[-1]} for item in points]
