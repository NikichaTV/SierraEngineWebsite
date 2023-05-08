import yaml
from enum import Enum

class DocumentedNamespace:
    __name: str = None
    __classes: str = []
    __namespaces = []

    def __init__(self, name, classes = None, namespaces = None):
        self.__name = name
        self.__classes = classes
        self.__namespaces = namespaces

    def GetName(self) -> str:
        return self.__name

    def GetClassCount(self) -> int:
        return 0 if self.__classes is None else len(self.__classes)

    def GetClass(self, index) -> str:
        return self.__classes[index]

    def GetNamespaceCount(self) -> int:
        return 0 if self.__namespaces is None else len(self.__namespaces)

    def GetNamespace(self, index):
        return self.__namespaces[index]

def DocumentedNamespaceConstructorYAML(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode) -> DocumentedNamespace:
    return DocumentedNamespace(**loader.construct_mapping(node))

class DocumentationData:
    __baseNamespace: DocumentedNamespace = None

    def __init__(self, yamlFilePath: str):
        loader = yaml.SafeLoader
        loader.add_constructor('!Namespace', DocumentedNamespaceConstructorYAML)

        self.__baseNamespace = yaml.load(open(yamlFilePath, 'rb'), Loader=loader)

    def GetBaseNamespace(self) -> DocumentedNamespace:
        return self.__baseNamespace[0]