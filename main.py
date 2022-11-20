import argparse
import logging
import os

from utils.log_utils import setup_logger


def compare_file_content(source_path, replica_path):
    pass

def get_content_of_dir(dir_path):
    content = os.listdir(dir_path)
    for element in content:
        try:
            ins_content = get_content_of_dir(f'{dir_path}{element}')
            ins_content = [f'{element}\\{ins_element}' for ins_element in ins_content]
            content.extend(ins_content)
        except:
            pass

    return content

def get_files_of_dir(dir_path):
    ''' Returns list of content in directory '''

    file_list = get_content_of_dir(dir_path)

    for element in file_list:
        if os.path.isfile(f'{dir_path}{element}'):
            logging.debug(f'File: {element}')

    return [f'{dir_path}{file}' for file in file_list]

def get_files_with_hash(dir_path):
    ''' Returns list of obj of content in directory '''
    list_of_files = get_files_of_dir(dir_path)




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

    sync_path = 'C:\\Users\\patrycja.szostak\\Desktop\\PYTHON\\dir_sync\\source\\'
    files = get_files_of_dir(sync_path)

