#import json
import pickle
import os

class Storage:
    #file_path= r'employees.pkl'
    def __init__(self, file_path= 'employees.pkl'):
        self.file_path = file_path

    def save(self, data):
        with open(self.file_path, 'wb') as f:
            pickle.dump(data, f)

    def load(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'rb') as f:
            return pickle.load(f)