"""SQL port of the polyformalism canary (uses Python for SQL bridge)."""

import sqlite3


def fnv1a_64_sql(s):
    """Reference implementation: FNV-1a 64-bit in Python."""
    h = 0xcbf29ce484222325
    for b in s.encode("utf-8"):
        h = h ^ b
        h = (h * 0x100000001b3) & 0xffffffffffffffff
    return h


def sql_canary():
    """Verify SQL can store and retrieve the canary byte-exact."""
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE canary (
            id INTEGER PRIMARY KEY,
            input TEXT,
            expected INTEGER
        )
    """)
    cur.execute(
        "INSERT INTO canary (id, input, expected) VALUES (?, ?, ?)",
        (1, "café Δ 日本語", 0x024a555471370b18d),
    )
    conn.commit()
    
    cur.execute("SELECT input, expected FROM canary WHERE id = 1")
    row = cur.fetchone()
    print(f"SQL stored:    input='{row[0]}'")
    print(f"SQL expected:  0x{row[1]:016x}")
    print(f"SQL computed:  0x{fnv1a_64_sql(row[0]):016x}")
    print(f"Match: {row[1] == fnv1a_64_sql(row[0])}")
    conn.close()


if __name__ == "__main__":
    sql_canary()
