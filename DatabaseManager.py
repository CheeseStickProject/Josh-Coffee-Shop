import sqlite3

class DatabaseManager:
    def __init__(self, db_name="coffee.db"):
        """Initialize the database connection and create a table if not exists."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """Create game_state table if it doesn't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS game_state (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cups REAL NOT NULL,
                money REAL NOT NULL,
                click_power INTEGER NOT NULL,
                total_clicks INTEGER NOT NULL,
                total_upgrades INTEGER NOT NULL,
                achievements TEXT DEFAULT '',
                producers TEXT DEFAULT '{}',
                upgrades TEXT DEFAULT '{}'
            )
        ''')
        self.conn.commit()

    # --- CRUD Operations ---

    def create(self, data: dict):
        """Insert a new game state."""
        self.cursor.execute('''
                INSERT INTO game_state (cups, money, click_power, total_clicks, total_upgrades, achievements, producers, upgrades)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (
                data.get("cups", 0.0),
                data.get("money", 0.0),
                data.get("click_power", 1),
                data.get("total_clicks", 0),
                data.get("total_upgrades", 0),
                data.get("achievements", ""),
                data.get("producers", "{}"),
                data.get("upgrades", "{}")
            )
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def read(self, id=None):
        """Fetch all game states or a specific game state by id."""
        if id:
            self.cursor.execute("SELECT * FROM game_state WHERE id=?", (id,))
            return self.cursor.fetchone()
        else:
            self.cursor.execute("SELECT * FROM game_state ORDER BY id DESC LIMIT 1")
            return self.cursor.fetchone()
        
    def update(self, data: dict):
        """Update game state details by id."""
        id = data.get("id")
        if not id:
            raise ValueError("ID is required for update operation.")

        fields = []
        values = []

        for key in ["cups", "money", "click_power", "total_clicks", "total_upgrades", "achievements", "producers", "upgrades"]:
            if key in data:
                fields.append(f"{key}=?")
                values.append(data[key])

        if not fields:
            raise ValueError("No fields to update.")

        values.append(id)
        sql = f"UPDATE game_state SET {', '.join(fields)} WHERE id=?"
        self.cursor.execute(sql, tuple(values))
        self.conn.commit()

    def delete(self, id):
        """Delete a game state by id."""
        self.cursor.execute("DELETE FROM game_state WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        """Close the connection when the object is destroyed."""
        self.conn.commit()
        self.conn.close()

if __name__ == "__main__":
    print("DatabaseManager module loaded.")

