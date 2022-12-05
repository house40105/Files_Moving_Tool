import unittest
import Files_Moving

    
class TestFileConverter(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    def test_empty(self):
        input_dir = 'none.txt'
        self.assertEqual(None,Files_Moving.move(input_dir))
        
    def test_convert(self):
        input_dir = 'files.txt'
        self.assertRaises(TypeError,Files_Moving.move(input_dir))

        
if __name__ == '__main__':
    unittest.main()