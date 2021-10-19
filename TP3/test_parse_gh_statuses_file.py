import unittest
import os
from parse_gh_statuses_file import get_status_from_gh_statuses_data_file, get_statuses_from_gh_statuses_data_file

DATA_FILE_URL = '/home/william/Programming/PYT/TP3/'
DATA_FILE_URI = 'data'
DATA_FILE_URN = DATA_FILE_URL + DATA_FILE_URI


class TestParseGHStatusesFile(unittest.TestCase):

    def test_get_status_from_gh_statuses_data_file_file_not_found(self):
        data_file_uri='/home/william/Programming/PYT/TP3/file_not_exists'
        data_file_urn = DATA_FILE_URL + data_file_uri
        with self.assertRaises(FileNotFoundError):
            get_status_from_gh_statuses_data_file(
                                                    gh_statuses_data_file_path=data_file_urn,
                                                    status_id = 1
                                                )

    def test_get_status_from_gh_statuses_data_file_id_not_found(self):
        status = get_status_from_gh_statuses_data_file(
                                                        status_id = -1,
                                                        gh_statuses_data_file_path=DATA_FILE_URN
                                                        )
        self.assertEqual(status, {})

    def test_get_status_from_gh_statuses_data_file_success(self):
        status = get_status_from_gh_statuses_data_file(
                                                        status_id = 2489368118,
                                                        gh_statuses_data_file_path=DATA_FILE_URN
                                                        )
        self.assertEqual(int(status['id']), 2489368118)
    
    def test_get_status_from_gh_statuses_data_file_wrong_file_format(self):
        data_file_uri='wrong_file_format'
        data_file_urn = DATA_FILE_URL + data_file_uri
        status = get_status_from_gh_statuses_data_file(
                                                        status_id = 2489368118,
                                                        gh_statuses_data_file_path=data_file_urn
                                                        )
        self.assertEqual(status, {})
    

class TestParseGHStatusesFile(unittest.TestCase):
    def test_get_statuses_from_gh_statuses_data_file_full_success(self):
        statuses = get_statuses_from_gh_statuses_data_file(
                                                            gh_statuses_data_file_path=DATA_FILE_URN,
                                                            )
        self.assertEqual(len(statuses), 7702)
        self.assertEqual(int(statuses[7701]['id']), 2489395761)

    def test_get_statuses_from_gh_statuses_data_file_page_success(self):
        statuses = get_statuses_from_gh_statuses_data_file(
                                                    gh_statuses_data_file_path=DATA_FILE_URN,
                                                    page=2,
                                                    page_size=3
                                                    )
        self.assertEqual(len(statuses), 3)
        self.assertEqual(int(statuses[0]['id']),2489368095)

    def test_get_statuses_from_gh_statuses_data_file_not_found(self):
        data_file_uri='/home/william/Programming/PYT/TP3/file_not_exists'
        data_file_urn = DATA_FILE_URL + data_file_uri
        with self.assertRaises(FileNotFoundError):
            get_statuses_from_gh_statuses_data_file(
                                                    gh_statuses_data_file_path=data_file_urn,
                                                    )
        

    def test_get_statuses_from_gh_statuses_data_file_wrong_page_number_value(self):
        with self.assertRaises(ValueError):
            get_statuses_from_gh_statuses_data_file(
                                                    gh_statuses_data_file_path=DATA_FILE_URN,
                                                    page=-88
                                                    )

    def test_get_statuses_from_gh_statuses_data_file_page_number_out_of_range(self):
        with self.assertRaises(IndexError):
            get_statuses_from_gh_statuses_data_file(
                                                    gh_statuses_data_file_path=DATA_FILE_URN,
                                                    page=1000000000000
                                                    )
    
    def test_get_statuses_from_gh_statuses_data_file_wrong_page_size_value(self):
        with self.assertRaises(ValueError):
            get_statuses_from_gh_statuses_data_file(
                                                    gh_statuses_data_file_path=DATA_FILE_URN,
                                                    page_size=-88
                                                    )




if __name__ == '__main__':
    unittest.main()