import yaml
from os import listdir
from os.path import isfile, join

class DocumentedClassElement:
    _htmlCode: str = ''

class DocumentedClassSection(DocumentedClassElement):
    __htmlCode: str = ''

    def __init__(self, title: str, description: str, elements: list[DocumentedClassElement]):
        self.__htmlCode += f"""
            <section class="article-section">
                <h2 class="section-heading">{ title }</h2>
        """

        if description is not None and description != '':
            self._htmlCode += f"""
                <p class="section-description">{ description }</p>
            """

        for element in elements:
            self.__htmlCode += element._htmlCode

        self.__htmlCode += """
            </section>
        """

    def GetCode(self):
        return self.__htmlCode


class DocumentedClassParagraph(DocumentedClassElement):

    def __init__(self, text: str):
        self._htmlCode += f"""
            <p class="section-paragraph">{ text }</p>
        """

class DocumentedClassUnorderedList(DocumentedClassElement):

    def __init__(self, title: str, elements: dict[str, str]):
        self._htmlCode += f"""
            <h5>{title}:</h5>
            <ul>
        """

        for key in elements:
            self._htmlCode += f"""<li><strong class="me-1">{ key }</strong> { elements[key] }</li>"""

        self._htmlCode += """
            </ul>
        """

class DocumentedClassOrderedList(DocumentedClassElement):

    def __init__(self, title: str, elements: list[str]):
        self._htmlCode += f"""
            <h5>{ title }:</h5>
            <ol>
        """

        for element in elements:
            self._htmlCode += f"""<li>{ element }</li>"""

        self._htmlCode += """
            </ol>
        """

class DocumentedClassCodeSnippet(DocumentedClassElement):

    def __init__(self, title: str, code: str):
        code = code.replace('&', '&amp')
        code = code.replace('<', '&lt')
        code = code.replace('>', '&gt')

        self._htmlCode = f"""
            <h5>{ title }: <code>{ code }</code></h5>
        """

class DocumentedClassCodeBlock(DocumentedClassElement):
    __cssLanguageTable: dict[str, str] = \
    {
        'markup'    :  'markup',
        'HTML'      :  'markup',
        'XML'       :  'markup',
        'SVG'       :  'markup',
        'MATHML'    :  'markup',
        'SSML'      :  'markup',
        'Atom'      :  'markup',
        'RSS'       :  'markup',
        'CSS'       :  'css',
        'Bash'      :  'bash',
        'Shell'     :  'bash',
        'C'         :  'c',
        'C#'        :  'csharp',
        'C++'       :  'cpp',
        'Cmake'     :  'cmake',
        'GLSL'      :  'glsl',
        'HLSL'      :  'hlsl',
        'Java'      :  'java',
        'JSON'      :  'json5',
        'Lua'       :  'lua',
        'Makefile'  :  'makefile',
        'Markdown'  :  'markdown',
        'Python'    :  'python',
        'Regex'     :  'regex',
        'Rust'      :  'rust',
        'SQL'       :  'sql',
        'SYSTEMD'   :  'systemd',
        'YAML'      :  'yaml'
    }

    def __init__(self, language: str, code: str):
        code = code.replace('&', '&amp')
        code = code.replace('<', '&lt')
        code = code.replace('>', '&gt')

        self._htmlCode += f"""
            <pre class="shadow"><code class="language-{ self.__cssLanguageTable[language] }">{ code }</code></pre>
        """

class DocumentedClassCalloutBlock(DocumentedClassElement):

    __cssTypeTable: dict[str, str] = \
    {
        'Tip'       :  'tip',
        'Info'      :  'info',
        'Warning'   :  'warning',
        'Danger'    :  'danger'
    }

    __cssTypeIconTable: dict[str, str] = \
    {
        'Tip'       :  'fas fa-note-sticky',
        'Info'      :  'fas fa-info-circle',
        'Warning'   :  'fas fa-warning',
        'Danger'    :  'fas fa-warning'
    }

    def __init__(self, type: str, title: str, text: str):
        self._htmlCode += f"""
            <div class="callout-{ self.__cssTypeTable[type] } shadow">
                <h4 class="callout-title"><i class="{ self.__cssTypeIconTable[type] }"></i>{ title }</h4>
                <p class="callout-description">{ text }</p>
            </div>
        """

class DocumentedClassProgressBar(DocumentedClassElement):

    def __init__(self, value: float):
        self._htmlCode += f"""
            <div class="progress shadow">
              <div class="progress-bar bg-success" style="width: { float(value) * 100.0 }%"></div>
            </div>
        """

class DocumentedClassTable(DocumentedClassElement):

    def __init__(self, rows: list[list[str]]):
        self._htmlCode += """
            <table class="table">
                <thead>
                    <tr>
        """

        for column in rows[0]:
            self._htmlCode += f"""
                <th scope="col">{ column }</th>
            """

        self._htmlCode += """
                </tr>
            </thead>

            <tbody>
        """

        for i in range(len(rows) - 1):
            self._htmlCode += f"""
                <tr>
            """

            for column in rows[i + 1]:
                self._htmlCode += f"""
                    <td>{ column }</td>
                """

            self._htmlCode += f"""
                </tr>
            """

        self._htmlCode += f"""
                </tbody>
            </table>
        """

class DocumentedClass:
    __name: str = None
    __namespace: str = None
    __lastUpdateDate: str = None

    __htmlCode: str = ''

    def __init__(self, name: str, namespace: str, description: str, lastUpdateDate: str, sections: list[DocumentedClassSection]):
        self.__name = name
        self.__namespace = namespace
        self.__lastUpdateDate = lastUpdateDate

        self.__htmlCode += f"""
            <article id="{ name }Article" class="documentation-article">
                <header>
                    <h1 class="article-heading">{ name }<span class="docs-time">Last updated: { lastUpdateDate }</span></h1>
                    <p class="article-description">{ description }</p>
                </header>
        """

        for section in sections:
            self.__htmlCode += section.GetCode()

        self.__htmlCode += """
            </article>
        """

    def GetName(self) -> str:
        return self.__name

    def GetNamespaceName(self) -> str:
        return self.__namespace

    def GetHTML(self):
        return self.__htmlCode

class DocumentedNamespace:
    __name: str = None
    __classes: list[str] = None
    __childNamespaces: list = None

    def __init__(self, name):
        self.__name = name
        self.__classes = []
        self.__childNamespaces = []

    def GetName(self):
        return self.__name

    def AddChildNamespace(self, child):
        self.__childNamespaces.append(child)

    def GetChildNamespaceCount(self) -> int:
        return len(self.__childNamespaces) if self.__childNamespaces is not None else 0

    def GetChildNamespace(self, index: int):
        return self.__childNamespaces[index]

    def AddClass(self, className: str):
        self.__classes.append(className)

    def GetClassCount(self) -> int:
        return len(self.__classes) if self.__classes is not None else 0

    def GetClass(self, index: int) -> str:
        return self.__classes[index]

    def __eq__(self, other) -> bool:
        return self.__name == other.__name

    def __hash__(self) -> int:
        return hash(self.__name)

    @staticmethod
    def CreateNamespaceTree(namespaces: list[tuple[str, str]]):
        namespaceDictionary: dict[str, DocumentedNamespace] = {}
        rootNamespaces: set[DocumentedNamespace] = set[DocumentedNamespace]()

        fictionalRootNamespace: DocumentedNamespace = DocumentedNamespace('root')
        for namespace, className in namespaces:
            parts: list[str] = namespace.split('.')
            parent: DocumentedNamespace = None

            for i, part in enumerate(parts):
                name: str = '.'.join(parts[:i + 1])

                if name not in namespaceDictionary:
                    newNamespace: DocumentedNamespace = DocumentedNamespace(part)
                    if i == len(parts) - 1:
                        newNamespace.AddClass(className)
                    namespaceDictionary[name] = newNamespace

                    if parent:
                        parent.AddChildNamespace(newNamespace)
                    else:
                        rootNamespaces.add(newNamespace)

                    parent = newNamespace
                else:
                    parent = namespaceDictionary[name]
                    if i == len(parts) - 1:
                        namespaceDictionary[name].AddClass(className)

        for namespace in rootNamespaces:
            fictionalRootNamespace.AddChildNamespace(namespace)

        return fictionalRootNamespace

    @staticmethod
    def PrintNamespace(namespace, iteration: int = 0):
        # return
        print((' ' * iteration) + ('\'-' if iteration != 0 else '') + namespace.GetName())
        for i in range(namespace.GetClassCount()):
            print((' ' * iteration) + (' |-') + namespace.GetClass(i))

        for i in range(namespace.GetChildNamespaceCount()):
            DocumentedNamespace.PrintNamespace(namespace.GetChildNamespace(i), iteration + 1)

def ConstructorYAML(T):
    def Constructor(loader: yaml.BaseLoader, node: yaml.nodes.MappingNode) -> T:
        return T(**loader.construct_mapping(node))

    return Constructor

class DocumentedClassesData:
    __jsonAutocompleteData: str = '['
    __rootNamespace: DocumentedNamespace = None
    __documentedClasses: list[list[DocumentedClass]] = []

    def __init__(self, yamlFolder: str):
        loader = yaml.BaseLoader
        loader.add_constructor('!DocumentedClass', ConstructorYAML(DocumentedClass))
        loader.add_constructor('!Section', ConstructorYAML(DocumentedClassSection))
        loader.add_constructor('!Paragraph', ConstructorYAML(DocumentedClassParagraph))
        loader.add_constructor('!CodeSnippet', ConstructorYAML(DocumentedClassCodeSnippet))
        loader.add_constructor('!UnorderedList', ConstructorYAML(DocumentedClassUnorderedList))
        loader.add_constructor('!OrderedList', ConstructorYAML(DocumentedClassOrderedList))
        loader.add_constructor('!CodeBlock', ConstructorYAML(DocumentedClassCodeBlock))
        loader.add_constructor('!CalloutBlock', ConstructorYAML(DocumentedClassCalloutBlock))
        loader.add_constructor('!ProgressBar', ConstructorYAML(DocumentedClassProgressBar))
        loader.add_constructor('!Table', ConstructorYAML(DocumentedClassTable))

        allNamespacesWithClasses: list[tuple[str, str]] = []
        dataFiles = [f for f in listdir(yamlFolder) if isfile(join(yamlFolder, f))]

        self.__documentedClasses.clear()
        for dataFile in dataFiles:
            self.__documentedClasses.append(yaml.load(open(yamlFolder + dataFile, 'rb').read(), Loader=loader))
            allNamespacesWithClasses.append((self.GetClass(-1).GetNamespaceName(), self.GetClass(-1).GetName()))

            self.__jsonAutocompleteData += f'"{ self.__documentedClasses[-1][0].GetName() }",'
        self.__jsonAutocompleteData = self.__jsonAutocompleteData[:-1] + ']'

        self.__rootNamespace = DocumentedNamespace.CreateNamespaceTree(allNamespacesWithClasses)

    def GetClassCount(self) -> int:
        return len(self.__documentedClasses)

    def GetClass(self, index) -> DocumentedClass:
        return self.__documentedClasses[index][0]

    def GetRootNamespace(self) -> DocumentedNamespace:
        return self.__rootNamespace

    def GetAutocompleteDataJSON(self) -> str:
        return self.__jsonAutocompleteData