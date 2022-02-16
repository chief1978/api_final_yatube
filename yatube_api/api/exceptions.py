from rest_framework.exceptions import APIException


class FollowUserNotExist(APIException):
    status_code = 400
    default_detail = "Пользователь на которого вы подписываетесь не существует"
    default_code = "Пользователь_на_которого_вы_подписываетесь_не_существует"


class SelfFollow(APIException):
    status_code = 400
    default_detail = "Нельзя подписаться на самого себя"
    default_code = "Нельзя_подписаться_на_самого_себя"
