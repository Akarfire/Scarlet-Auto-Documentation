
# Stores rulesets for analysing various types of code files
class FileRulesetStorage:
    
    def __init__(self, in_core):
        self.core = in_core
    
    # Whether there is a suitable ruleset for the specified file
    def file_has_ruleset(self, file_name : str):
        
        return True