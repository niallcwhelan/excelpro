import unittest
from excel_import import load_excel_files, format_excel_data, merge_excel_data, write_merged_data_to_csv
import os

class TestScript(unittest.TestCase):

    def test_file_loading(self):
        # Test that the script correctly identifies and loads all Excel files in the specified directory
        # You can create a temporary directory with test files for this test
        # You can check that the script loaded the correct number of files and that each file was loaded successfully
        data_path = "/Users//niallwhelan/Projects/Play/Python/excelpro/data"
        excel_files = load_excel_files(data_path)
        self.assertEqual(len(excel_files), 4)

    def test_data_formatting(self):
        # Test that the script correctly formats the data from each Excel file into a 2D list
        # You can create test Excel files with known data to test this
        # You can check that the lst have the correct shape and contents
        data_path = "/Users//niallwhelan/Projects/Play/Python/excelpro/data"
        excel_files = load_excel_files(data_path)
        list = format_excel_data(excel_files)
        num_rows = len(list)
        num_cols = len(list[0])
        self.assertEqual((num_rows, num_cols), (4, 15)) # 4 files with 15 rows of data.
        
    def test_data_output(self):
        # Test that the script correctly outputs the merged data to a CSV file
        # You can create a temporary directory with test files and check that the output CSV file has the expected contents
        print('test: test_data_output...')
        data_path = "/Users//niallwhelan/Projects/Play/Python/excelpro/data"
        test_path = "/Users//niallwhelan/Projects/Play/Python/excelpro/test_output"
        output_file = "test_output.csv"
        output_path = os.path.join(test_path, output_file)
        excel_files = load_excel_files(data_path)
        list = format_excel_data(excel_files)
        merged_data = merge_excel_data(list)
        write_merged_data_to_csv(merged_data, output_path)
        self.assertTrue(os.path.exists(output_path))
        with open(output_path, 'r') as f:
            csv_contents = f.read()
            print('test: test_data_output... column check')
            self.assertIn("start date,end date,region,resource,cost", csv_contents)
            print('test: test_data_output... data last row check')
            self.assertIn("2023-03-01,2023-03-31,EU,prod4,38.46751689162513", csv_contents)

