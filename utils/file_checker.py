import os
import json
from pathlib import Path
from datetime import datetime

class FileMonitor:
    def __init__(self):
        self.checkpoint_file = "file_checkpoints.json"
        self.last_check = datetime.now()
        
    def get_all_files(self):
        """Get all relevant files to monitor"""
        return list(Path('.').rglob('*.py')) + ['requirements.txt']

    def get_file_modification_times(self):
        return {str(f): os.path.getmtime(f) for f in self.get_all_files()}
    
    def check_for_updates(self):
        """Returns list of changed files"""
        current_files = self.get_file_modification_times()
        
        try:
            with open(self.checkpoint_file, 'r') as f:
                saved_files = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            saved_files = {}
        
        updates = [f for f, mtime in current_files.items() 
                  if f not in saved_files or mtime > saved_files.get(f, 0)]
        
        with open(self.checkpoint_file, 'w') as f:
            json.dump(current_files, f)
        
        return updates