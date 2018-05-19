import unittest
from unittest.mock import patch
import os
from io import StringIO
from supertool import similar_files

DISTRO_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class Test_work(unittest.TestCase):
    """
    Class testing function work in similar_files modul
    """

    def test_directory_isnot_empty_positive(self):
        """
        Positive test
        Check returns value if directory have similar files

        """
        self.assertEqual(similar_files.work(os.path.join(DISTRO_ROOT_PATH, 'folder__for_test_1')), [
            [os.path.join(DISTRO_ROOT_PATH, 'folder__for_test_1', 'file1.txt'),
             os.path.join(DISTRO_ROOT_PATH, 'folder__for_test_1', 'file2.txt'),
             os.path.join(DISTRO_ROOT_PATH, 'folder__for_test_1', 'subfolder', 'file1.txt')]
        ])

    def test_directory_empty_positive(self):
        """
        Positive test
        Check returns value if directory is empty

        """
        self.assertEqual(similar_files.work(os.path.join(DISTRO_ROOT_PATH, 'folder_for_test_2')), [])

    def test_other_extension_positive(self):
        """
        Positive test
        Check returns value if directory is other extension

        """
        self.assertEqual(similar_files.work(os.path.join(DISTRO_ROOT_PATH, 'folder_for_test_3')),
                         [[os.path.join(DISTRO_ROOT_PATH, 'folder_for_test_3', 'file1.txt'),
                           os.path.join(DISTRO_ROOT_PATH, 'folder_for_test_3', 'file2.py')]])

    @patch('sys.stdout', new_callable=StringIO)
    def test_not_directory_nonpositive(self, mock_stdout):
        """
        Negative test
        Check returns value and stdout if directory is not directory

        """
        self.assertEqual(similar_files.work(1), [])
        self.assertEqual(mock_stdout.getvalue(), "Directory 1 does not exists\n")


class Test_function_siilar_files(unittest.TestCase):
    """
    Class testiing other function similar_files modul:
        get_hash_files(fnamelst)
        get_all_path_file(directory, paths_file)
    """

    def test_get_hash_files_positive(self):
        """
        Positive test
        Check returns value function get_hash_files

        """
        self.assertEqual(
            similar_files.get_hash_files([os.path.join(DISTRO_ROOT_PATH, 'folder__for_test_1', 'file1.txt'),
                                          os.path.join(DISTRO_ROOT_PATH, 'folder__for_test_1', 'file2.txt'),
                                          os.path.join(DISTRO_ROOT_PATH, 'folder__for_test_1', 'subfolder',
                                                       'file1.txt')]), ['c4ca4238a0b923820dcc509a6f75849b',
                                                                        'c4ca4238a0b923820dcc509a6f75849b',
                                                                        'c4ca4238a0b923820dcc509a6f75849b'])

    def test_get_all_path_file_positive(self):
        """
        Positive test
        Check returns value function get_all_path_file

        """
        self.assertEqual(similar_files.get_all_path_file(os.path.join(DISTRO_ROOT_PATH, 'folder_for_test_3')),
                         [os.path.join(DISTRO_ROOT_PATH, 'folder_for_test_3', 'file1.txt'),
                          os.path.join(DISTRO_ROOT_PATH, 'folder_for_test_3', 'file2.py')])



if __name__=="__main__":
    unittest.main()