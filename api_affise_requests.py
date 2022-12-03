from requests import get
from datetime import date
import json


class ApiAffiseRequests:
    __domain = "https://api-cpacash.affise.com"

    def get_statistics(self, slice_param: str, date_from: date, date_to: date):
        response = get(self.__domain + "/3.0/stats/custom",
                       params={
                           'API-Key': 'e49644c732975860e7de94fd28d3e23a',
                           'slice[]': slice_param,
                           'filter[date_from]': date_from,
                           'filter[date_to]': date_to,
                           'conversionTypes[]': ['confirmed', 'pending', 'declined', 'total'],
                            }
                       )

        return response

    @staticmethod
    def get_conversions_count(dict_response_api: dict):
        actions: dict
        result: list[int]

        if dict_response_api['pagination']['total_count'] > 0:
            actions = dict_response_api['stats'][0]['actions']
            result = [actions['confirmed']['count'], actions['pending']['count'], actions['declined']['count'],
                      actions['total']['count']]
        else:
            result = [0, 0, 0, 0]

        return result
