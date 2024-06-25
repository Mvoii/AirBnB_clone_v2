#!/usr/bin/python3

"""A test module for the console module."""

import json
import os
import MySQLdb
import sqlalchemy
import unittest
import MySQLdb
from unittest.mock import patch
from io import StringIO

from console import HBNBCommand
from models import storage
from models.state import State




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

class TestCreateState(unittest.TestCase):
    def setUp(self):
        self.conn = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        self.cur = self.conn.cursor()
        self.cli = HBNBCommand()

    def tearDown(self):
        self.cur.close()
        self.conn.close()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "only relevant for db storage")
    def test_create_state(self):
        # Get initial count
        self.cur.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cur.fetchone()[0]

        # Execute console command
        self.cli.onecmd('create State name="California"')

        # Get new count
        self.cur.execute("SELECT COUNT(*) FROM states")
        new_count = self.cur.fetchone()[0]

        # Assert
        self.assertEqual(new_count, initial_count + 1)

        # Verify the state was created correctly
        self.cur.execute("SELECT * FROM states WHERE name='California'")
        result = self.cur.fetchone()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
