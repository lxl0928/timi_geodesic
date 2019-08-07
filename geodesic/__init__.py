# coding: utf-8

from .main import TimiGeodesic

from .__version__ import __version__, __title__, __description__, __url__, __author_email__

geodesic = TimiGeodesic()
get_distance_with_dict = geodesic.get_distance_id_dict
get_distance_with_detail = geodesic.get_distance_detail_info
get_distance_with_list = geodesic.get_distance_id_list
