class InvalidColumnError(Exception):
    """Exception raised when attempting to select a column that doesn't exist in the schema."""
    pass


class Schema:
    """
    Represents the schema of a table with column definitions.
    """

    def __init__(self, columns: list):
        """
        Initialize a schema.

        Args:
            columns: List of column names
        """
        self.columns = columns

    def get_columns(self) -> list:
        """
        Get the list of column names.

        Returns:
            List of column names
        """
        return self.columns


class Table:
    """
    Represents a table in the in-memory database.
    """

    def __init__(self, name: str, schema: Schema):
        """
        Initialize a table.

        Args:
            name: Name of the table
            schema: Schema object defining the table structure
        """
        self.name = name
        self.schema = schema
        self.rows = []

    def insert(self, row: dict) -> bool:
        """
        Insert a row into the table.

        Args:
            row: Dictionary with column names as keys and values

        Returns:
            True if row is inserted successfully, False if row is None
        """
        if row is None:
            return False

        # dict key is column name; value is the value for that column
        # c1, v1; c2, v2; c3, v3.
        # Check that all columns in the row are defined in the schema
        for column in row.keys():
            if column not in self.schema.get_columns():
                return False

        self.rows.append(row)
        return True

    def select(self, columns: list = None) -> list:
        """
        Select rows from the table, optionally returning only specified columns.

        Args:
            columns: Optional list of column names to return. If None, returns all columns.

        Returns:
            List of rows with specified columns

        Raises:
            InvalidColumnError: If any specified column doesn't exist in the schema
        """
        if columns is None:
            return self.rows

        # Verify that all requested columns exist in the schema
        schema_columns = self.schema.get_columns()
        for column in columns:
            if column not in schema_columns:
                raise InvalidColumnError(f"Column '{column}' not found in table schema")

        selected_rows = []
        for row in self.rows:
            selected_row = {col: row.get(col) for col in columns if col in row}
            selected_rows.append(selected_row)

        return selected_rows


class InMemorySqlDb:
    """
    An in-memory SQL database implementation.
    Supports basic CRUD operations: CREATE, INSERT, SELECT, UPDATE, DELETE.
    """

    def __init__(self):
        """
        Initialize the database with an empty tables dictionary.
        Key is the table name and value is a Table object.
        """
        self.tables = {}

    def create_table(self, table_name: str, columns: list) -> bool:
        """
        Create a new table with specified column names.

        Args:
            table_name: Name of the table
            columns: List of column names

        Returns:
            True if table is created successfully, False if table already exists
        """
        if table_name in self.tables:
            return False

        schema = Schema(columns)
        self.tables[table_name] = Table(table_name, schema)
        return True

    def insert(self, table_name: str, row: dict) -> bool:
        """
        Insert a row into the specified table.

        Args:
            table_name: Name of the table
            row: Dictionary with column names as keys and values

        Returns:
            True if row is inserted successfully
        """
        if table_name not in self.tables:
            return False

        return self.tables[table_name].insert(row)

    def select(self, table_name: str, columns: list = None) -> list:
        """
        Select rows from the specified table, optionally returning only specified columns.

        Args:
            table_name: Name of the table
            columns: Optional list of column names to return. If None, returns all columns.

        Returns:
            List of rows with specified columns
        """
        if table_name not in self.tables:
            return []

        return self.tables[table_name].select(columns)

    def drop_table(self, table_name: str) -> bool:
        """
        Drop a table from the database.

        Args:
            table_name: Name of the table

        Returns:
            True if table is dropped successfully, False if table doesn't exist
        """
        if table_name not in self.tables:
            return False

        del self.tables[table_name]
        return True
