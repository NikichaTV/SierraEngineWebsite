from enum import Enum
from flask import Flask, render_template

class ProgrammingLanguage(Enum):
    MARKUP    =  'markup',
    HTML      =  MARKUP,
    XML       =  MARKUP,
    SVG       =  MARKUP,
    MATHML    =  MARKUP,
    SSML      =  MARKUP,
    ATOM      =  MARKUP,
    RSS       =  MARKUP,
    CSS       =  'css',
    BASH      =  'bash',
    SHELL     =  BASH,
    C         =  'c',
    CSHARP    =  'csharp',
    CPP       =  'cpp',
    CMAKE     =  'cmake',
    GLSL      =  'glsl',
    HLSL      =  'hlsl',
    JAVA      =  'java',
    JSON      =  'json5',
    LUA       =  'lua',
    MAKEFILE  =  'makefile',
    MARKDOWN  =  'markdown',
    PYTHON    =  'python',
    REGEX     =  'regex',
    RUST      =  'rust',
    SQL       =  'sql',
    SYSTEMD   =  'systemd',
    YAML      =  'yaml'

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