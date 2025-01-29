import sqlite3
from typing import List, Dict, Any

class SqliteUtils:
    def __init__(self, db_path: str, table_name: str):
        """
        Initialize the manager with a database path and table name.

        :param db_path: Path to the SQLite database file.
        :param table_name: Name of the table to store the data.
        """
        self.db_path = db_path
        self.table_name = table_name

    def _get_column_definitions(self, dicts: List[Dict[str, Any]]) -> Dict[str, str]:
        """
        Get column definitions from a list of dictionaries.

        :param dicts: List of dictionaries.
        :return: A dictionary of column names and their SQLite data types.
        """
        column_types = {}
        for d in dicts:
            for key, value in d.items():
                if key not in column_types:
                    if isinstance(value, int):
                        column_types[key] = "INTEGER"
                    elif isinstance(value, float):
                        column_types[key] = "REAL"
                    elif isinstance(value, str):
                        column_types[key] = "TEXT"
                    elif isinstance(value, bytes):
                        column_types[key] = "BLOB"
                    else:
                        column_types[key] = "TEXT"  # Default type
        return column_types

    def _create_table(self, column_definitions: Dict[str, str]):
        """
        Create a table with the given column definitions.

        :param column_definitions: Dictionary of column names and their SQLite data types.
        """
        columns = ", ".join(f"{col} {dtype}" for col, dtype in column_definitions.items())
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {self.table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns});"

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(create_table_sql)

    def save(self, dicts: List[Dict[str, Any]]):
        """
        Save a list of dictionaries to the database.

        :param dicts: List of dictionaries to save.
        """
        if not dicts:
            return

        column_definitions = self._get_column_definitions(dicts)
        self._create_table(column_definitions)

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            for d in dicts:
                columns = ", ".join(d.keys())
                placeholders = ", ".join(["?" for _ in d.values()])
                insert_sql = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders});"
                cursor.execute(insert_sql, list(d.values()))

    def fetch_all(self) -> List[Dict[str, Any]]:
        """
        Fetch all rows from the table and return them as a list of dictionaries.

        :return: List of dictionaries.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute(f"PRAGMA table_info({self.table_name});")
            columns = [row[1] for row in cursor.fetchall() if row[1] != "id"]

            cursor.execute(f"SELECT {', '.join(columns)} FROM {self.table_name};")
            rows = cursor.fetchall()

        return [dict(zip(columns, row)) for row in rows]

    def overwrite(self, dicts: List[Dict[str, Any]]):
        """
        Overwrite the table with new data.

        :param dicts: List of dictionaries to overwrite the table.
        """
        if not dicts:
            return

        column_definitions = self._get_column_definitions(dicts)
        self._create_table(column_definitions)

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute(f"DELETE FROM {self.table_name};")

            for d in dicts:
                columns = ", ".join(d.keys())
                placeholders = ", ".join(["?" for _ in d.values()])
                insert_sql = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders});"
                cursor.execute(insert_sql, list(d.values()))



def print_sqlite_database(db_path: str):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # Get all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        for table_name in tables:
            table_name = table_name[0]
            print(f"Table: {table_name}")

            # Get all rows from the table
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = [info[1] for info in cursor.fetchall()]
            print(f"Columns: {', '.join(columns)}")

            cursor.execute(f"SELECT {', '.join(columns)} FROM {table_name};")
            main = cursor.fetchall()
            print("----")
            # Print the rows
            for rows in main:
                for row in rows:
                    print(row)

            print("\n" + "=" * 50 + "\n")



