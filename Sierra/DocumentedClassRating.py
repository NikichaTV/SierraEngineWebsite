from Sierra.Utility import *
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

RatingsDB = SQLAlchemy()

class DocumentedClassRating(RatingsDB.Model):
    classID: str = RatingsDB.Column(RatingsDB.String, nullable=False, primary_key=True)
    userID: str = RatingsDB.Column(RatingsDB.String, nullable=False, primary_key=True)
    rating: int = RatingsDB.Column(RatingsDB.Integer, nullable=False)

    __bind_key__ = 'API-ReferenceRatingsDB'
    __table_name__ = 'documented_class_rating'
    __table_args__ = (RatingsDB.UniqueConstraint('classID', 'userID'),)

    @staticmethod
    def AddClassRating(classID: str, rating: int):
        if rating < 1 or rating > 3:
            return 'Rating value is out of boundaries! It mus be between 1 and 3!'

        dateCookieValue = None
        dateCookieResponse = make_response('Rating successfully added!')

        if not Utility.CookieExists(FIRST_LOGIN_COOKIE_NAME):
            dateCookieValue = datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(' ', '')
            dateCookieResponse = Utility.SetCookieForResponse(dateCookieResponse, FIRST_LOGIN_COOKIE_NAME, dateCookieValue)

        else:
            dateCookieValue = Utility.GetCookie(FIRST_LOGIN_COOKIE_NAME)

        userID: str = request.remote_addr + dateCookieValue
        existingRating = DocumentedClassRating.query.filter_by(classID=classID, userID=userID).first()

        if not existingRating:
            RatingsDB.session.add(DocumentedClassRating(classID=classID, userID=userID, rating=rating))
            RatingsDB.session.commit()

            return dateCookieResponse

        else:
            existingRating.rating = rating
            RatingsDB.session.commit()

            return 'Rating successfully updated!'

    @staticmethod
    def GetAverageRatingForClass(classID: str):
        result: int = RatingsDB.session.query(RatingsDB.func.avg(DocumentedClassRating.rating)).filter_by(classID=classID).scalar()
        return result or 0

    @staticmethod
    def GetAverageRatings():
        averageRatings = DocumentedClassRating.query.with_entities(DocumentedClassRating.classID, RatingsDB.func.avg(DocumentedClassRating.rating)).group_by(DocumentedClassRating.classID).all()
        averageRatingsDictionary = { rating[0]: rating[1] for rating in averageRatings }
        return averageRatingsDictionary