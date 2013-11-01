
import unittest
import os
import finda.finda

class TestFinda(unittest.TestCase):

    def setUp(self):
        self.test_data_folder = os.path.join('test', 'files') # called 'files' since it can't have letters a, b, c
        self.test_data_sub_folder = os.path.join(self.test_data_folder, 'c')
        self.make_data_files()

    #def tearDown(self):
    #    os.remove(self.test_data_folder)

    def make_data_files(self):
        if not os.path.exists(self.test_data_folder):
            folders = ['', 'c']
            letters = ['a', 'b']
            datas = ['', 'a']
            file_count = 0
            if not os.path.exists(self.test_data_folder):
                os.makedirs(self.test_data_folder)
            if not os.path.exists(self.test_data_sub_folder):
                os.makedirs(self.test_data_sub_folder)
            for folder in folders:
                for letter in letters:
                    for data in datas:
                        if len(folder) > 0:
                            file_path = os.path.join(self.test_data_folder, folder, letter + str(file_count) + '.txt')
                        else:
                            file_path = os.path.join(self.test_data_folder, letter + str(file_count) + '.txt')
                        with open(file_path, 'w') as f:
                            f.write(data)
                            file_count += 1
            file_path = os.path.join(self.test_data_folder, '_.txt')
            with open(file_path, 'w') as f:
                f.write('ef')

    def test_single_filename(self):
        finder = finda.finda.Finda(['a0'], [self.test_data_folder], True)
        finder.run()
        self.assertEqual([os.path.join(self.test_data_folder, 'a0.txt')], finder.get_matches())

    def test_contents(self):
        finder = finda.finda.Finda(['ef'], [self.test_data_folder], True)
        finder.run()
        self.assertEqual([os.path.join(self.test_data_folder, '_.txt')], finder.get_matches())

    def test_folder_only(self):
        finder = finda.finda.Finda(['c'], [self.test_data_folder], True)
        finder.run()
        files = [os.path.join(self.test_data_sub_folder, 'a4.txt'),
                 os.path.join(self.test_data_sub_folder, 'a5.txt'),
                 os.path.join(self.test_data_sub_folder, 'b6.txt'),
                 os.path.join(self.test_data_sub_folder, 'b7.txt')]
        files.sort()
        self.assertEqual(files, finder.get_matches())

    # test the and-ing on the contents only
    def test_and_contents(self):
        finder = finda.finda.Finda(['e', 'f'], [self.test_data_folder], True)
        finder.run()
        self.assertIn(os.path.join(self.test_data_folder, '_.txt'), finder.get_matches())

    # test the and-ing on the filename only
    def test_and_filename(self):
        finder = finda.finda.Finda(['a', '0'], [self.test_data_folder], True)
        finder.run()
        self.assertEqual([os.path.join(self.test_data_folder, 'a0.txt')], finder.get_matches())

    # test and-ing across contents and file name
    def test_and_contents_and_filename(self):
        finder = finda.finda.Finda(['a', 'b'], [self.test_data_folder], True)
        finder.run()
        files = [os.path.join(self.test_data_folder, 'b3.txt'),
                 os.path.join(self.test_data_sub_folder, 'b7.txt')]
        files.sort()
        self.assertEqual(files, finder.get_matches())
