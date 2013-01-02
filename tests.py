#!/usr/bin/env python2

import unittest
import drivel_app as drivel

class TestDrivelSetup(unittest.TestCase):
    
    def setUp(self):
        self.drivel = drivel.Setup()
        
    def test_set_drive_dir(self):
        self.assertTrue(self.drivel.set_drive_dir())
        
    def test_get_drive_dir(self):
        self.assertTrue(self.drivel.get_drive_dir())
        
    def test_get_redirect(self):
        self.assertEqual(self.drivel.get_redirect(), 'http://localhost')
        
if __name__ == '__main__':
    unittest.main()