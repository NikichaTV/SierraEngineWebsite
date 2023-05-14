from datetime import datetime, timedelta

import flask
from flask import make_response, request

FIRST_LOGIN_COOKIE_NAME = 'FirstLoginDate'

class Utility:
    @staticmethod
    def SetCookie(cookieName: str, cookieValue: str, expiration: timedelta = timedelta(days=365 * 30), path: str = '/'):
        response = make_response()
        response.set_cookie(cookieName, cookieValue, max_age=31536000*30, expires=datetime.now() + expiration, path=path)
        return response

    @staticmethod
    def SetCookieForResponse(response: flask.Response, cookieName: str, cookieValue: str, expiration: timedelta = timedelta(days=365 * 30), path: str = '/'):
        response.set_cookie(cookieName, cookieValue, max_age=31536000*30, expires=datetime.now() + expiration, path=path)
        return response

    @staticmethod
    def GetCookie(cookieName: str) -> str:
        return request.cookies.get(cookieName)

    @staticmethod
    def CookieExists(cookieName: str) -> bool:
        print(request.cookies.get(FIRST_LOGIN_COOKIE_NAME))
        return cookieName in request.cookies