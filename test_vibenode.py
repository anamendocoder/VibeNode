# test_vibenode.py
"""
Tests for VibeNode module.
"""

import unittest
from vibenode import VibeNode

class TestVibeNode(unittest.TestCase):
    """Test cases for VibeNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VibeNode()
        self.assertIsInstance(instance, VibeNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VibeNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
