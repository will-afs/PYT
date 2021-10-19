from flask import Flask, request, jsonify
from ..parse_gh_statuses_file import get_status_from_gh_statuses_data_file, get_statuses_from_gh_statuses_data_file
import os
import json

app = Flask(__name__)

@app.route('/statuses/<page>.json', methods=['GET'])
def get_statuses(page):
    page = int(page)
    statuses_json = get_statuses_from_gh_statuses_data_file(
                                                        page=page,
                                                        gh_statuses_data_file_path='/../data'
                                                        )
    statuses_str = json.dumps(statuses_json)
    return statuses_str

@app.route('/status/<status_id>', methods=['GET'])
def get_status(status_id):
    status_id = int(status_id)
    status_json = get_status_from_gh_statuses_data_file(
                                                        status_id,
                                                        gh_statuses_data_file_path='/../data'
                                                        )
    return status_json