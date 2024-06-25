#!/usr/bin/python3

"""A test module for the console module."""

import json
import os
import MySQLdb
import sqlalchemy

from models import storage

import unittest
from unittest.mock import patch
from io import StringIO

from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cli = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.cli.onecmd("quit")

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.cli.onecmd("EOF")

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        self.cli.onecmd("")
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        self.cli.onecmd("create BaseModel")
        self.assertNotEqual(mock_stdout.getvalue(), "")
        self.cli.onecmd("create InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        self.cli.onecmd("show")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")
        self.cli.onecmd("show InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        self.cli.onecmd("destroy")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")
        self.cli.onecmd("destroy InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        self.cli.onecmd("all InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        self.cli.onecmd("update")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")
        self.cli.onecmd("update InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

if __name__ == '__main__':
    unittest.main()
