import json
import os
from typing import List


def get_statuses_from_gh_statuses_data_file(gh_statuses_data_file_path:str='/TP3/data', page_size:int=5, page:int=-1)->List[dict]:
    '''
        Returns the content of the JSON Lines file as a list of JSON statuses.

        A page number can be specified as an argument, and page size can also be specified.
        When page number is set to -1 (default), returns the whole document.
        Otherwise, page_number can range from 1 to the end of the document.
        Also, page_size is a strictly positive integer (default is set to 5).
        If no match is found, returns an IndexError.
    '''
    if page != -1 and page <= 0:
        raise ValueError('Page index out of range : specified {}. '\
            'Expected a value equal to -1 or > 0.'.format(page))
    elif page_size <= 0:
        raise ValueError('page_size value out of range : specified {}. '\
            'Expected a value >= 0.'.format(page_size))

    # TODO: check the parameters types

    file_path = gh_statuses_data_file_path
    with open(file_path, 'r') as gh_statuses_raw_data_file:
        gh_statuses_raw_data = []
        if page == -1: # Reads and returns the whole document
            gh_statuses_json = []
            try:
                i=0
                while(i==0):
                    gh_status_json = json.loads(gh_statuses_raw_data_file.readline())
                    gh_statuses_json.append(gh_status_json)
            except json.decoder.JSONDecodeError:
                # Reached end of document
                pass
        else: # Reads a specific page
            i=1
            # Empty the buffer until reaching the index just before the searched page
            while(i<=page_size*(page-1)):
                if gh_statuses_raw_data_file.readline() != '':
                    i+=1
                else:
                    raise IndexError('Page index out of range')
            i=1
            # Assuming the buffer is on the searched page
            gh_statuses_json = []
            try:
                while(i<=page_size):
                    gh_status_json = json.loads(gh_statuses_raw_data_file.readline())
                    gh_statuses_json.append(gh_status_json)
                    i+=1
            except json.decoder.JSONDecodeError:
                # Reached end of document
                pass
    return gh_statuses_json


def get_status_from_gh_statuses_data_file(status_id:int, gh_statuses_data_file_path:str) -> dict:
    '''
        Returns the status matching the status_id in the JSON Lines file.
        If there is no match, returns an empty JSON dict.
    '''

    # TODO: check the parameters types

    file_path = gh_statuses_data_file_path
    with open(file_path, 'r') as gh_statuses_raw_data_file:
        i=1
        try:
            while(i>0):
                gh_status_line = gh_statuses_raw_data_file.readline()
                gh_status_json = json.loads(gh_status_line)
                if int(gh_status_json['id']) == status_id:
                    break
        except json.decoder.JSONDecodeError:
            # Could not find any status matching status id
            gh_status_json = {}
    return gh_status_json


