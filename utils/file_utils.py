import hashlib
import logging


class File():
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_hash_md5 = ''
        self.file_content = ''

    def calculate_file_hash(self) -> str:
        ''' Returns MD5 sum for given content'''
        logging.debug(f'Calculating file hash code MD5: {self.file_path}')
        self.read_file_content()
        hash_code = hashlib.md5(self.file_content).hexdigest()

        self.file_hash_md5 = hash_code
        return hash_code

    def read_file_content(self) -> bytes:
        ''' Reads file content and returns it as str '''
        logging.debug(f'Reading file content: {self.file_path}')
        file_content: bytes
        with open(self.file_path, 'rb') as source_file:
            file_content = source_file.read()

        self.file_content = file_content

        return file_content

    def get_file_hash(self):
        if not self.file_hash_md5:
            self.calculate_file_hash()

        logging.debug(f'File:{self.file_path} hash code MD5:{self.file_hash_md5}')

        return self.file_hash_md5

    def create(self, sync_path):
        pass

    def copy(self, sync_path):
        pass

    def remove(self, sync_path):
        pass
