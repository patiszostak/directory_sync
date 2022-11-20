import argparse
import logging
import os
from typing import List

from utils.file_utils import File
from utils.log_utils import setup_logger


def compare_file_content(source_path, replica_path):
    pass


def get_content_of_dir(dir_path):
    ''' Returns list of content in directory '''
    content = os.listdir(dir_path)
    for element in content:
        try:
            ins_content = get_content_of_dir(f'{dir_path}{element}')
            ins_content = [f'{element}\\{ins_element}' for ins_element in ins_content]
            content.extend(ins_content)
        except:
            pass

    return content


def get_files_list_of_dir(dir_path):
    ''' Returns list of files in directory '''

    content_list = get_content_of_dir(dir_path)
    file_list = []

    for element in content_list:
        if os.path.isfile(f'{dir_path}{element}'):
            logging.debug(f'File: {element}')
            file_list.append(f'{dir_path}{element}')

    return file_list


def get_files_from_dir(dir_path):
    ''' Returns list of File obj from directory '''
    list_of_files_names = get_files_list_of_dir(dir_path)
    files = []

    for path in list_of_files_names:
        file = File(path, dir_path)
        file.get_file_hash()
        files.append(file)

    return files


def search_changed_files_in_replica(source_files: List[File], replica_files: List[File]):
    '''Searches for missing or changed files in replica directory'''
    logging.debug('Searching for missing or changed files in replica path.')

    for source_file in source_files:
        is_file_missing = True
        is_file_changed = True
        for replica_file in replica_files:
            if replica_file.file_name == source_file.file_name:
                is_file_missing = False
                if replica_file.file_hash_md5 == source_file.file_hash_md5:
                    is_file_changed = False

        if is_file_changed:
            pass  # TODO: remove file with this name from replica

        if is_file_missing or is_file_changed:
            pass  # TODO: copy file with this name from replica


def search_deleted_files_in_replica(source_files: List[File], replica_files: List[File]):
    '''Searches for missing or changed files in source directory'''
    logging.debug('Searching for deleted files in replica path.')

    for replica_file in replica_files:
        is_file_deleted = True
        for source_file in source_files:
            if replica_file.file_name == source_file.file_name:
                is_file_deleted = False

        if is_file_deleted:
            pass  # TODO: Remove file from replica directory


def sync():
    pass


def parse_arguments():
    ''' Parse input arguments and returns it as ArgumentParser dict '''
    arg_pars = argparse.ArgumentParser()

    arg_pars.add_argument('-p', '--sync_path', type=str, help='Folder path to synchronize')
    arg_pars.add_argument('-i', '--interval', type=str, help='Interval to synchronize [s] 1-60')
    arg_pars.add_argument('-l', '--log_path', type=str, help='Path to store operation logs')

    return arg_pars


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    setup_logger()

    source_path = 'C:\\Desktop\\PYTHON\\dir_sync\\source\\'
    replica_path = 'C:\\Desktop\\PYTHON\\dir_sync\\replica\\'
    src_files = get_files_from_dir(source_path)
    rpl_files = get_files_from_dir(replica_path)

    search_changed_files_in_replica(src_files, rpl_files)
    search_deleted_files_in_replica(src_files, rpl_files)
