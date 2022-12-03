from flask import Flask
from datetime import date
from api_affise_requests import ApiAffiseRequests
from datetime_extend import DateTimeExtend

app = Flask(__name__)


@app.route('/')
def slash():
    api_affise = ApiAffiseRequests()
    datetime_extend = DateTimeExtend()

    response_current_day = api_affise.get_statistics('day', date.today(), date.today())
    conversions_cd = api_affise.get_conversions_count(response_current_day.json())

    # # вычисляем первый и последний день текущей недели
    response_current_week = api_affise.get_statistics('quarter', datetime_extend.get_fst_day_current_week(),
                                                      datetime_extend.get_lst_day_current_week())
    conversions_cw = api_affise.get_conversions_count(response_current_week.json())

    # # вычисляем первый и последний день прошлой недели
    response_previous_week = api_affise.get_statistics('quarter', datetime_extend.get_fst_day_previous_week(),
                                                       datetime_extend.get_lst_day_previous_week())
    conversions_pw = api_affise.get_conversions_count(response_previous_week.json())

    # # вычисляем последний день месяца
    response_current_month = api_affise.get_statistics('month', datetime_extend.get_fst_day_current_month(),
                                                       datetime_extend.get_lst_day_current_month())
    conversions_cm = api_affise.get_conversions_count(response_current_month.json())

    return f'\
            За текущий день</br>\
            Принято: {conversions_cd[0]}</br>\
            В обработке: {conversions_cd[1]}</br>\
            Отклонено: {conversions_cd[2]}</br>\
            Всего: {conversions_cd[3]}</br>\
            </br>\
            За текущую неделю</br>\
            Принято: {conversions_cw[0]}</br>\
            В обработке: {conversions_cw[0]}</br>\
            Отклонено: {conversions_cw[0]}</br>\
            Всего: {conversions_cw[0]}</br>\
            </br>\
            За прошлую неделю</br>\
            Принято: {conversions_pw[0]}</br>\
            В обработке: {conversions_pw[0]}</br>\
            Отклонено: {conversions_pw[0]}</br>\
            Всего: {conversions_pw[0]}</br>\
            </br>\
            За текущий месяц</br>\
            Принято: {conversions_cm[0]}</br>\
            В обработке: {conversions_cm[0]}</br>\
            Отклонено: {conversions_cm[0]}</br>\
            Всего: {conversions_cm[0]}</br>\
            </br>'


if __name__ == '__main__':
    app.run()
