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


def DocumentedClassSectionConstructorYAML(loader: yaml.BaseLoader, node: yaml.nodes.MappingNode) -> DocumentedClassSection:
    return DocumentedClassSection(**loader.construct_mapping(node))

class DocumentedClassParagraph(DocumentedClassElement):

    def __init__(self, text: str):
        self._htmlCode += f"""
            <p class="section-paragraph">{ text }</p>
        """

def DocumentedClassParagraphConstructorYAML(loader: yaml.BaseLoader, node: yaml.nodes.MappingNode) -> DocumentedClassParagraph:
    return DocumentedClassParagraph(**loader.construct_mapping(node))

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

def DocumentedClassUnorderedListConstructorYAML(loader: yaml.BaseLoader, node: yaml.nodes.MappingNode) -> DocumentedClassUnorderedList:
    return DocumentedClassUnorderedList(**loader.construct_mapping(node))

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

def DocumentedClassOrderedListConstructorYAML(loader: yaml.BaseLoader, node: yaml.nodes.MappingNode) -> DocumentedClassOrderedList:
    return DocumentedClassOrderedList(**loader.construct_mapping(node))

class DocumentedClassCodeSnippet(DocumentedClassElement):

    def __init__(self, title: str, code: str):
        code = code.replace('&', '&amp')
        code = code.replace('<', '&lt')
        code = code.replace('>', '&gt')

        self._htmlCode = f"""
            <h5>{ title }: <code>{ code }</code></h5>
        """

def DocumentedClassCodeSnippetConstructorYAML(loader: yaml.BaseLoader, node: yaml.nodes.MappingNode) -> DocumentedClassCodeSnippet:
    return DocumentedClassCodeSnippet(**loader.construct_mapping(node))

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

def DocumentedClassCodeBlockConstructorYAML(loader: yaml.BaseLoader, node: yaml.nodes.MappingNode) -> DocumentedClassCodeBlock:
    return DocumentedClassCodeBlock(**loader.construct_mapping(node))

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

def DocumentedClassCalloutBlockConstructorYAML(loader: yaml.BaseLoader, node: yaml.nodes.MappingNode) -> DocumentedClassCalloutBlock:
    return DocumentedClassCalloutBlock(**loader.construct_mapping(node))

class DocumentedClassProgressBar(DocumentedClassElement):

    def __init__(self, value: float):
        self._htmlCode += f"""
            <div class="progress shadow">
              <div class="progress-bar bg-success" style="width: { float(value) * 100.0 }%"></div>
            </div>
        """

def DocumentedClassProgressBarConstructorYAML(loader: yaml.BaseLoader, node: yaml.nodes.MappingNode) -> DocumentedClassProgressBar:
    return DocumentedClassProgressBar(**loader.construct_mapping(node))

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

def DocumentedClassTableConstructorYAML(loader: yaml.BaseLoader, node: yaml.nodes.MappingNode) -> DocumentedClassTable:
    return DocumentedClassTable(**loader.construct_mapping(node))

class DocumentedClass:
    __name: str = None
    __htmlCode: str = ''

    def __init__(self, name: str, description: str, sections: list[DocumentedClassSection]):
        self.__name = name

        self.__htmlCode += f"""
            <article id="{ name }Article" class="documentation-article">
                <header>
                    <h1 class="article-heading">{ name }<span class="docs-time">Last updated: 2019-06-01</span></h1>
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
    def GetHTML(self):
        return self.__htmlCode

def DocumentedClassConstructorYAML(loader: yaml.BaseLoader, node: yaml.nodes.MappingNode) -> DocumentedClass:
    return DocumentedClass(**loader.construct_mapping(node))

class DocumentedClassesData:
    __documentedClasses: list[list[DocumentedClass]] = []
    __jsonAutocompleteData: str = '['

    def __init__(self, yamlFolder: str):
        loader = yaml.BaseLoader
        loader.add_constructor('!DocumentedClass', DocumentedClassConstructorYAML)
        loader.add_constructor('!Section', DocumentedClassSectionConstructorYAML)
        loader.add_constructor('!Paragraph', DocumentedClassParagraphConstructorYAML)
        loader.add_constructor('!CodeSnippet', DocumentedClassCodeSnippetConstructorYAML)
        loader.add_constructor('!UnorderedList', DocumentedClassUnorderedListConstructorYAML)
        loader.add_constructor('!OrderedList', DocumentedClassOrderedListConstructorYAML)
        loader.add_constructor('!CodeBlock', DocumentedClassCodeBlockConstructorYAML)
        loader.add_constructor('!CalloutBlock', DocumentedClassCalloutBlockConstructorYAML)
        loader.add_constructor('!ProgressBar', DocumentedClassProgressBarConstructorYAML)
        loader.add_constructor('!Table', DocumentedClassTableConstructorYAML)

        dataFiles = [f for f in listdir(yamlFolder) if isfile(join(yamlFolder, f))]
        for dataFile in dataFiles:
            self.__documentedClasses.append(yaml.load(open(yamlFolder + dataFile, 'rb').read(), Loader=loader))
            self.__jsonAutocompleteData += f'"{ self.__documentedClasses[-1][0].GetName() }",'

        self.__jsonAutocompleteData = self.__jsonAutocompleteData[:-1] + ']'

    def GetClassCount(self) -> int:
        return len(self.__documentedClasses)

    def GetClass(self, index) -> DocumentedClass:
        return self.__documentedClasses[index][0]

    def GetAutocompleteDataJSON(self) -> str:
        return self.__jsonAutocompleteData;