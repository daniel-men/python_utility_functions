import unittest

class ImportTest(unittest.TestCase):
    def testImport(self):
        import python_utility_functions as puf
        assert puf.scale is not None
        assert puf.show_grayscale_image is not None
        assert puf.get_all_files_in_dir is not None