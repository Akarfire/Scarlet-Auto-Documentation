from FileScanner import FileScanner
from CodeScanner import CodeScanner
from FileRulesets import FileRulesetStorage

class Core:
    
    def __init__(self):
        
        self.fileScanner = FileScanner(self)
        self.codeScanner = CodeScanner(self)
        self.rulesetStorage = FileRulesetStorage(self)