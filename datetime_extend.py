from datetime import date, timedelta


class DateTimeExtend:
    __today = date.today()

    def get_fst_day_current_week(self):
        return self.__today - timedelta(days=self.__today.weekday())

    def get_lst_day_current_week(self):
        return self.__today + timedelta(days=6 - self.__today.weekday())

    def get_fst_day_previous_week(self):
        return self.__today - timedelta(days=self.__today.weekday()) - timedelta(days=7)

    def get_lst_day_previous_week(self):
        return self.__today + timedelta(days=6 - self.__today.weekday()) - timedelta(days=7)

    def get_fst_day_current_month(self):
        return self.__today.replace(day=1)

    def get_lst_day_current_month(self):
        next_month = self.__today.replace(day=28) + timedelta(days=4)
        return next_month - timedelta(days=next_month.day)
