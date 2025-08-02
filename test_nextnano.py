# test_nextnano.py
"""
Tests for NextNano module.
"""

import unittest
from nextnano import NextNano

class TestNextNano(unittest.TestCase):
    """Test cases for NextNano class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NextNano()
        self.assertIsInstance(instance, NextNano)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NextNano()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
