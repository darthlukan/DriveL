#!/usr/bin/env python2

import os
import unittest
import drivel_app as drivel

class TestDrivelSetup(unittest.TestCase):
    
    def setUp(self):
        self.drivel = drivel.Setup()
        
    def test_init_variables(self):
        self.assertEqual(self.drivel.CLIENT_ID, 'YOUR_CLIENT_ID')
        self.assertEqual(self.drivel.CLIENT_SECRET, 'YOUR_CLIENT_SECRET')
        self.assertEqual(self.drivel.OAUTH_SCOPE, 'https://www.googleapis.com/auth/drive')
        
    def test_set_drive_dir(self):
        self.assertTrue(self.drivel.set_drive_dir())
        self.assertTrue(os.path.isdir(self.drivel.set_drive_dir()))
        
    def test_get_drive_dir(self):
        self.assertTrue(os.path.isdir(self.drivel.get_drive_dir()))
        
    def test_get_redirect(self):
        self.assertEqual(self.drivel.get_redirect(), 'http://localhost')
        
    def test_get_scope(self):
        self.assertEqual(self.drivel.get_scope(), 'https://www.googleapis.com/auth/drive')
        
        
if __name__ == '__main__':
    unittest.main()