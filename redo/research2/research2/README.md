# Database Testing Utility

This utility tests database connections and operations for the debate_agents.py application. It provides comprehensive testing capabilities with support for both MySQL and SQLite databases.

## Features

- **Dual Database Support**: Works with both MySQL and SQLite with automatic fallback
- **Configuration Management**: Supports configuration via JSON file or direct parameters
- **Context Manager Support**: Can be used with Python's `with` statement for automatic cleanup
- **Complete Test Suite**: Tests connection, table creation, data insertion, and querying
- **Detailed Error Reporting**: Provides helpful error messages and troubleshooting guidance
- **SQL Compatibility**: Automatically adjusts SQL syntax based on database type

## Requirements

- Python 3.6+
- For MySQL support: `mysql-connector-python` package (optional)
- SQLite support is built into Python standard library

## Installation

1. Clone or download this repository
2. Install MySQL connector (optional):
   ```
   pip install mysql-connector-python
   ```

## Usage

### Basic Usage

```python
from test_database import DatabaseTester

# Test with default MySQL settings
tester = DatabaseTester()
tester.test_database_interaction()
```

### Using Configuration File

1. First, create a configuration file:
   ```python
   tester = DatabaseTester()
   tester.create_config_file('db_config.json')
   ```

2. Edit the generated `db_config.json` file with your database credentials

3. Use the configuration file:
   ```python
   tester = DatabaseTester('db_config.json')
   tester.test_database_interaction()
   ```

### Using Context Manager

```python
with DatabaseTester(use_sqlite=True) as tester:
    tester.create_test_tables()
    tester.test_insert_data()
    results = tester.cursor.execute("SELECT * FROM debate_results")
    # Connection automatically closed when exiting 'with' block
```

### Force SQLite Usage

```python
# Force using SQLite even if MySQL is available
tester = DatabaseTester(use_sqlite=True)
tester.test_database_interaction()
```

## Configuration Options

The configuration can be provided either as parameters or in a JSON file:

- **host**: Database host address (default: 'localhost_3306')
- **user**: Database username (default: 'root')
- **password**: Database password (default: '123456')
- **database**: Database name (default: 'debate_db')
- **use_sqlite**: Force SQLite usage (default: False)

## Test Process

When running `test_database_interaction()`, the utility performs these steps:

1. Connect to the database (MySQL or fallback to SQLite)
2. Create test tables (debate_results)
3. Insert sample data
4. Query and display the data
5. Close the connection

## Troubleshooting

### Common MySQL Connection Issues

1. **MySQL server not running**
   - Start the MySQL service: `systemctl start mysql` (Linux) or use MySQL Workbench (Windows)

2. **Incorrect credentials**
   - Verify username and password are correct
   - Check if the user has permissions for the database

3. **Database does not exist**
   - Create the database first: `CREATE DATABASE debate_db;`

4. **SQLite Fallback**
   - If MySQL connection fails, the utility will automatically try SQLite
   - SQLite creates a local database file with the name: `{database}_test.db`

## License

MIT License