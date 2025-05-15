"""
    Saul Toribio
    4/24/25
    CSE012 Spring 2025: Week 12 Coding Assignment
    IDE: VSCode; Python: 3.12.7
"""

import sqlite3

def initialize_ledger(db_path: str):
    """
    Creates the loot table if it doesn't exist.

    Args:
        db_path (str): The path to the SQLite database file.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS loot (
            id INTEGER PRIMARY KEY,
            item_name TEXT NOT NULL,
            item_type TEXT NOT NULL,
            value_gp INTEGER NOT NULL,
            rarity TEXT NOT NULL,
            found_in_dungeon TEXT
            )
        ''')
        conn.commit()
        print(f"Ledger initialized at {db_path}")
    except sqlite3.Error as e:
        print(f"Database error during initialization: {e}")
    finally:
        if conn:
            conn.close()

# pylint: disable=too-many-arguments, too-many-positional-arguments
def record_new_loot(db_path: str, name: str, item_type: str,
                    value: int, rarity: str, location: str) -> int | None:
    """
    Records a new loot item in the ledger.

    Args:
        db_path (str): Path to the database file.
        name (str): The item_name.
        item_type (str): The item_type.
        value (int): The value_gp.
        rarity (str): The item's rarity.
        location (str): The found_in_dungeon.

    Returns:
        int: The id of the newly recorded loot item, or None on failure.
    """
    conn = None
    new_id = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO loot (item_name, item_type, value_gp, rarity, found_in_dungeon)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, item_type, value, rarity, location))
        conn.commit()
        new_id = cursor.lastrowid
        print(f"Recorded loot '{name}' with ID: {new_id}")
    except sqlite3.Error as e:
        print(f"Database error during record: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
    return new_id

def inspect_loot_item(db_path: str, item_id: int) -> tuple | None:
    """
    Retrieves all details for a specific loot item by its ID.

    Args:
        db_path (str): Path to the database file.
        item_id (int): The id of the loot item to retrieve.

    Returns:
        tuple: A tuple containing all data for the item, or None if not found.
               Format: (id, item_name, item_type, value_gp, rarity, found_in_dungeon)
    """
    conn = None
    details = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, item_name, item_type, value_gp, rarity, found_in_dungeon
            FROM loot
            WHERE id = ?
        ''', (item_id,))
        details = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Database error during inspection: {e}")
    finally:
        if conn:
            conn.close()
    return details

def list_items_by_rarity(db_path: str, target_rarity: str) -> list:
    """
    Finds all items matching a specific rarity.

    Args:
        db_path (str): Path to the database file.
        target_rarity (str): The rarity level to filter by.

    Returns:
        list: A list of tuples (id, item_name, value_gp). Empty list if none found.
    """
    conn = None
    results = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, item_name, value_gp
            FROM loot
            WHERE rarity = ?
        ''', (target_rarity,))
        results = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error during list by rarity: {e}")
    finally:
        if conn:
            conn.close()
    return results

def update_item_value(db_path: str, item_id: int, new_value: int) -> bool:
    """
    Updates the gold piece value of a specific loot item.

    Args:
        db_path (str): Path to the database file.
        item_id (int): The id of the loot item to update.
        new_value (int): The new value_gp.

    Returns:
        bool: True if the update was successful, False otherwise.
    """
    conn = None
    success = False
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE loot
            SET value_gp = ?
            WHERE id = ?
        ''', (new_value, item_id))
        conn.commit()
        if cursor.rowcount > 0:
            success = True
            print(f"Updated value for item ID {item_id} to {new_value} GP")
        else:
            print(f"No item found with ID {item_id} to update.")
    except sqlite3.Error as e:
        print(f"Database error during update value: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
    return success

def remove_loot_item(db_path: str, item_id: int) -> bool:
    """
    Removes a specific loot item from the ledger.

    Args:
        db_path (str): Path to the database file.
        item_id (int): The id of the loot item to remove.

    Returns:
        bool: True if the deletion was successful, False otherwise.
    """
    conn = None
    success = False
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM loot
            WHERE id = ?
        ''', (item_id,))
        conn.commit()
        if cursor.rowcount > 0:
            success = True
            print(f"Removed loot item with ID {item_id}")
        else:
            print(f"No item found with ID {item_id} to remove.")
    except sqlite3.Error as e:
        print(f"Database error during removal: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
    return success
