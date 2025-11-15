from pathlib import Path
from ElementDataStructure import ElementDataStructure

# Analyzes code in a given file
class CodeScanner:
    
    def __init__(self, in_core):
        self.core = in_core
        
    # Scans the contents 
    def scan_code_file(self, file : Path, out_data_structure : ElementDataStructure):
        pass