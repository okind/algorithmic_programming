import unittest
from InMemorySqlDb import InMemorySqlDb, Schema, Table, InvalidColumnError


class TestInMemorySqlDb(unittest.TestCase):
    """Test cases for InMemorySqlDb class."""

    def setUp(self):
        """Set up test fixtures."""
        self.db = InMemorySqlDb()

    def test_create_table_success(self):
        """
        Test case 1: Create a table with the given list of column names.
        Verify that table is created and list of columns saved in schema.
        """
        table_name = "users"
        columns = ["id", "name", "email"]

        # Create the table
        result = self.db.create_table(table_name, columns)

        # Verify that table creation was successful
        self.assertTrue(result, "Table creation should return True")

        # Verify that table exists in the database
        self.assertIn(table_name, self.db.tables,
                      "Table should exist in database")

        # Verify that the table is a Table instance
        table = self.db.tables[table_name]
        self.assertIsInstance(
            table, Table, "Table should be instance of Table")

        # Verify that the schema is a Schema instance
        self.assertIsInstance(table.schema, Schema,
                              "Schema should be instance of Schema")

        # Verify that columns are correctly saved in schema
        schema_columns = table.schema.get_columns()
        self.assertEqual(
            schema_columns,
            columns,
            f"Schema columns should be {columns}, got {schema_columns}",
        )

    def test_create_table_duplicate(self):
        """Test that creating a duplicate table returns False."""
        table_name = "users"
        columns = ["id", "name"]

        # Create table first time
        result1 = self.db.create_table(table_name, columns)
        self.assertTrue(result1, "First table creation should return True")

        # Try to create table with same name
        result2 = self.db.create_table(table_name, columns)
        self.assertFalse(
            result2, "Duplicate table creation should return False")

    def test_drop_table_success(self):
        """Test that an existing table can be dropped successfully."""
        table_name = "users"
        columns = ["id", "name", "email"]

        # Create a table first
        self.db.create_table(table_name, columns)
        self.assertIn(table_name, self.db.tables,
                      "Table should exist before drop")

        # Drop the table
        result = self.db.drop_table(table_name)

        # Verify that drop was successful
        self.assertTrue(result, "Drop table should return True")

        # Verify that table no longer exists
        self.assertNotIn(table_name, self.db.tables,
                         "Table should not exist after drop")

    def test_drop_table_non_existing(self):
        """Test that dropping a non-existing table is skipped and returns False."""
        table_name = "non_existing_table"

        # Verify table doesn't exist
        self.assertNotIn(table_name, self.db.tables,
                         "Table should not exist initially")

        # Try to drop non-existing table
        result = self.db.drop_table(table_name)

        # Verify that drop returned False
        self.assertFalse(
            result, "Drop of non-existing table should return False")

        # Verify that database is unchanged
        self.assertNotIn(table_name, self.db.tables,
                         "Table should still not exist")

    def test_table_insert_null_row(self):
        """Test that inserting a null row returns False."""
        # Create a table first
        table_name = "users"
        columns = ["id", "name", "email"]
        self.db.create_table(table_name, columns)
        table = self.db.tables[table_name]

        # Try to insert a null row
        result = table.insert(None)

        # Verify that insert returned False
        self.assertFalse(result, "Insert with null row should return False")

        # Verify that no rows were added to the table
        self.assertEqual(len(table.rows), 0,
                         "Table should have 0 rows after null insert")

    def test_insert_null_row(self):
        """Test that InMemorySqlDb.insert rejects null rows."""
        # Create a table first
        table_name = "users"
        columns = ["id", "name", "email"]
        self.db.create_table(table_name, columns)

        # Try to insert a null row
        result = self.db.insert(table_name, None)

        # Verify that insert returned False
        self.assertFalse(result, "Insert with null row should return False")

        # Verify that select returns empty list
        rows = self.db.select(table_name)
        self.assertEqual(rows, [], "Table should be empty after null insert")

    def test_select_all_columns(self):
        """Test selecting all columns when columns parameter is None."""
        table_name = "users"
        columns = ["id", "name", "email"]
        self.db.create_table(table_name, columns)

        # Insert test data
        row1 = {"id": 1, "name": "Alice", "email": "alice@example.com"}
        row2 = {"id": 2, "name": "Bob", "email": "bob@example.com"}
        self.db.insert(table_name, row1)
        self.db.insert(table_name, row2)

        # Select all columns
        result = self.db.select(table_name)

        # Verify all rows are returned with all columns
        self.assertEqual(len(result), 2, "Should return 2 rows")
        self.assertEqual(
            result[0], row1, "First row should match inserted data")
        self.assertEqual(
            result[1], row2, "Second row should match inserted data")

    def test_select_specific_columns(self):
        """Test selecting only specific columns."""
        table_name = "users"
        columns = ["id", "name", "email"]
        self.db.create_table(table_name, columns)

        # Insert test data
        row1 = {"id": 1, "name": "Alice", "email": "alice@example.com"}
        row2 = {"id": 2, "name": "Bob", "email": "bob@example.com"}
        self.db.insert(table_name, row1)
        self.db.insert(table_name, row2)

        # Select only id and name columns
        result = self.db.select(table_name, columns=["id", "name"])

        # Verify only specified columns are returned
        self.assertEqual(len(result), 2, "Should return 2 rows")
        self.assertEqual(result[0], {"id": 1, "name": "Alice"},
                         "First row should contain only id and name")
        self.assertEqual(result[1], {"id": 2, "name": "Bob"},
                         "Second row should contain only id and name")

    def test_select_single_column(self):
        """Test selecting a single column."""
        table_name = "users"
        columns = ["id", "name", "email"]
        self.db.create_table(table_name, columns)

        # Insert test data
        self.db.insert(
            table_name, {"id": 1, "name": "Alice", "email": "alice@example.com"})
        self.db.insert(
            table_name, {"id": 2, "name": "Bob", "email": "bob@example.com"})

        # Select only email column
        result = self.db.select(table_name, columns=["email"])

        # Verify only email column is returned
        self.assertEqual(len(result), 2, "Should return 2 rows")
        self.assertEqual(result[0], {"email": "alice@example.com"},
                         "First row should contain only email")
        self.assertEqual(result[1], {"email": "bob@example.com"},
                         "Second row should contain only email")

    def test_select_from_non_existing_table(self):
        """Test selecting from a non-existing table returns empty list."""
        result = self.db.select("non_existing_table")

        self.assertEqual(
            result, [], "Select from non-existing table should return empty list")

    def test_select_empty_table(self):
        """Test selecting from an empty table."""
        table_name = "empty_table"
        columns = ["id", "name"]
        self.db.create_table(table_name, columns)

        # Select from empty table without column filter
        result = self.db.select(table_name)
        self.assertEqual(
            result, [], "Select from empty table should return empty list")

        # Select from empty table with column filter
        result = self.db.select(table_name, columns=["id"])
        self.assertEqual(
            result, [], "Select with columns from empty table should return empty list")

    def test_select_invalid_column(self):
        """Test selecting with a column that doesn't exist in schema raises InvalidColumnError."""
        table_name = "users"
        columns = ["id", "name", "email"]
        self.db.create_table(table_name, columns)

        # Insert test data
        self.db.insert(
            table_name, {"id": 1, "name": "Alice", "email": "alice@example.com"})

        # Try to select with an invalid column and expect exception
        with self.assertRaises(InvalidColumnError):
            self.db.select(table_name, columns=["id", "invalid_column"])

    def test_select_all_invalid_columns(self):
        """Test selecting with all invalid columns raises InvalidColumnError."""
        table_name = "users"
        columns = ["id", "name", "email"]
        self.db.create_table(table_name, columns)

        # Insert test data
        self.db.insert(
            table_name, {"id": 1, "name": "Alice", "email": "alice@example.com"})

        # Try to select with all invalid columns and expect exception
        with self.assertRaises(InvalidColumnError):
            self.db.select(table_name, columns=["invalid1", "invalid2"])

    def test_table_select_invalid_column(self):
        """Test Table.select with invalid column raises InvalidColumnError."""
        table_name = "users"
        columns = ["id", "name", "email"]
        self.db.create_table(table_name, columns)
        table = self.db.tables[table_name]

        # Insert test data
        table.insert({"id": 1, "name": "Alice", "email": "alice@example.com"})

        # Try to select with an invalid column and expect exception
        with self.assertRaises(InvalidColumnError):
            table.select(columns=["id", "nonexistent"])


if __name__ == "__main__":
    unittest.main()
