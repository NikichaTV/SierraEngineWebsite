from CodeDoc.Page import *
from Sierra.DocumentedClass import *
from Sierra.DocumentedClassRating import *

from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../static/data/data-bases/API-ReferenceRatings.db'
app.config['SQLALCHEMY_BINDS'] = { 'API-ReferenceRatingsDB': 'sqlite:///../static/data/data-bases/API-ReferenceRatings.db' }
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
RatingsDB.init_app(app)

@app.route('/Documentation/')
def Index():
    page: Page = Page('pages/Documentation/documentation.html')
    page.SetTitle('Sierra Engine - Documentation')
    return page.GetRenderTemplate()

@app.route('/Documentation/API-Reference/', defaults = { 'classID': 'Introduction' })
@app.route('/Documentation/API-Reference/<string:classID>/')
def APIReference(classID):
    page: Page = Page('pages/Documentation/API-Reference/api-reference.html')
    page.SetTitle('Sierra Engine - Documentation')

    page.SetVariable('articleTitle', classID)
    documentedClassData = DocumentedClassesData('static/data/documentation/classes/')
    page.SetVariable('classData', documentedClassData)

    jsonDocsSearchAutocompleteFile = open('static/data/documentation/search-autocomplete.json', 'w')
    jsonDocsSearchAutocompleteFile.write(documentedClassData.GetAutocompleteDataJSON())
    jsonDocsSearchAutocompleteFile.close()

    return page.GetRenderTemplate()

@app.route('/Documentation/API-Reference/<string:classID>/', methods=['POST', 'PUT'])
def APIReferenceRatingRequest(classID):
    ratingScore: int = 0
    try:
        ratingScore = int(request.form.get('rating'))
    except ValueError:
        return 'Invalid rating value passed!'

    print(DocumentedClassRating.GetAverageRatings())
    return DocumentedClassRating.AddClassRating(classID, ratingScore)

@app.errorhandler(404)
def Error404(error):
    page: Page = Page('pages/Errors/error-404.html')
    page.SetTitle('Sierra Engine - Error 404')
    return page.GetRenderTemplate()

if __name__ == '__main__':
    app.run()
