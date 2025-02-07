import os
import sqlite3
from main_app.io.sqlite_utils import SqliteUtils


class TestSqliteUtils:
    DB_PATH = "test_database.db"
    TABLE_NAME = "test_table"

    @staticmethod
    def __delete_db():
        """Deletes the test database file if it exists."""
        if os.path.exists(TestSqliteUtils.DB_PATH):
            os.remove(TestSqliteUtils.DB_PATH)

    @staticmethod
    def __initiation():
        """Initializes the test database and returns an instance of SqliteUtils."""
        sample_data = [
            {"name": "Alice", "age": 30, "salary": 50000.0},
            {"name": "Bob", "age": 25, "salary": 45000.0},
        ]
        tested_object = SqliteUtils(TestSqliteUtils.DB_PATH, TestSqliteUtils.TABLE_NAME)
        return tested_object, sample_data

    @staticmethod
    def test_save():
        try:
            tested_object, sample_data = TestSqliteUtils.__initiation()
            tested_object.save(sample_data)
            
            with sqlite3.connect(TestSqliteUtils.DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT name, age, salary FROM {TestSqliteUtils.TABLE_NAME};")
                rows = cursor.fetchall()
                if len(rows) != len(sample_data):
                    print("save failed: incorrect number of rows")
                    return False
            
            TestSqliteUtils.__delete_db()
            return True
        except Exception as e:
            print(f"Exception in test_save: {e}")
            TestSqliteUtils.__delete_db()
            return False

    @staticmethod
    def test_fetch_all():
        try:
            tested_object, sample_data = TestSqliteUtils.__initiation()
            tested_object.save(sample_data)
            fetched_data = tested_object.fetch_all()
            
            if fetched_data != sample_data:
                print("fetch_all failed: incorrect data fetched")
                return False
            
            TestSqliteUtils.__delete_db()
            return True
        except Exception as e:
            print(f"Exception in test_fetch_all: {e}")
            TestSqliteUtils.__delete_db()
            return False

    @staticmethod
    def test_overwrite():
        try:
            tested_object, sample_data = TestSqliteUtils.__initiation()
            tested_object.save(sample_data)
            new_data = [{"name": "Charlie", "age": 40, "salary": 70000.0}]
            tested_object.overwrite(new_data)
            
            fetched_data = tested_object.fetch_all()
            if fetched_data != new_data:
                print("overwrite failed: data mismatch")
                return False
            
            TestSqliteUtils.__delete_db()
            return True
        except Exception as e:
            print(f"Exception in test_overwrite: {e}")
            TestSqliteUtils.__delete_db()
            return False
