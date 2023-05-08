from flask import Flask, render_template, make_response

class Page:
    __htmlFilePath = ''
    __variablesDictionary = \
    {
        'base_author'       : 'Nikolay Kanchevski',
        'base_css_files'    : set(()),
        'base_js_files'     : set(())
    }


    def __init__(self, htmlFilePath):
        self.__htmlFilePath = htmlFilePath

    def AddCSS(self, cssFilePath):
        self.__variablesDictionary['base_css_files'].add(cssFilePath)

    def AddJS(self, jsFilePath):
        self.__variablesDictionary['base_js_files'].add(jsFilePath)

    def SetAuthor(self, authorName):
        self.__variablesDictionary['base_author'] = authorName

    def SetDescription(self, description):
        self.__variablesDictionary['base_description'] = description

    def SetTitle(self, title):
        self.__variablesDictionary['base_title'] = title

    def SetVariable(self, variable, value):
        self.__variablesDictionary[variable] = value

    def GetRenderTemplate(self):
        return render_template(self.__htmlFilePath, **self.__variablesDictionary)

    def GetResponse(self):
        return make_response(self.GetRenderTemplate())