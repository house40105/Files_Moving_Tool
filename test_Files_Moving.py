import unittest
import Files_Moving

    
class TestFileConverter(unittest.TestCase):
    def test_convert_success(self):
        input_dir = 'files.txt'
        Files_Moving.move(input_dir)

        
if __name__ == '__main__':
    unittest.main()