from CodeDoc.Page import *
from Sierra.Documentation import *
from Sierra.DocumentedClass import *

app = Flask(__name__)

@app.route('/Documentation/')
def Index():
    page = Page('pages/Documentation/documentation.html')
    page.SetTitle('Sierra Engine - Documentation')
    return page.GetRenderTemplate()

@app.route('/Documentation/API-Reference/', defaults = { 'article': 'Introduction' })
@app.route('/Documentation/API-Reference/<article>/')
def APIReference(article):
    page = Page('pages/Documentation/API-Reference/api-reference.html')
    page.SetTitle('Sierra Engine - Documentation')

    apiStructure = DocumentationData('static/data/documentation/api-reference-hierarchy.yaml')
    page.SetVariable('apiStructure', apiStructure)
    page.SetVariable('articleTitle', article)

    documentedClassData = DocumentedClassesData('static/data/documentation/classes/')
    page.SetVariable('classData', documentedClassData)

    jsonDocsSearchAutocompleteFile = open('static/data/documentation/search-autocomplete.json', 'w')
    jsonDocsSearchAutocompleteFile.write(documentedClassData.GetAutocompleteDataJSON())
    jsonDocsSearchAutocompleteFile.close()

    return page.GetRenderTemplate()

if __name__ == '__main__':
    app.run()