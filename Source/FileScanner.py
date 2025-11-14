from pathlib import Path
import logging

from ElementDataStructure import ElementDataStructure

# Scans files 
class FileScanner:
    
    def __init__(self, in_core):
        self.core = in_core
    
    
    # Scans all files in the directory and generates an element data structure
    def scan_directory(self, pathStr : str) -> ElementDataStructure:
        
        path = Path(pathStr)
        
        # Checking if specified path exits
        if not path.exists():
            logging.error(f"Directory {pathStr} does not exist!")
            return None
        
        # Initializing output data structure
        data_structure : ElementDataStructure = ElementDataStructure()
        
        # Gathering all files from the directory
        files = [f for f in path.rglob("*") if f.is_file()]
        
        # Looping over files and passing them to the CodeScanner
        for file in files:
            
            if self.core.rulesetStorage.file_has_ruleset(file.name):
                self.core.codeScanner.scan_code_file(file, data_structure)
                
        return data_structure
        
        
        
        
        