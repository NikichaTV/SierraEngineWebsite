from flask import Flask, render_template

class Page:
    __htmlFilePath = None
    __variablesDictionary = { }

    def __init__(self, htmlFilePath):
        self.__htmlFilePath = htmlFilePath

    def SetVariable(self, variable, value):
        self.__variablesDictionary[variable] = value

    def GetRenderTemplate(self):
        return render_template(self.__htmlFilePath, **self.__variablesDictionary)