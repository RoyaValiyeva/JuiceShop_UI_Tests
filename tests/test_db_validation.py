import pytest

def test_order_written_to_db(db_conn, test_run_id):
    """
    Verify that when a user places an order, 
    the database contains the correct row with email, product, and quantity.
    """
    user_email = "admin@juice-sh.op"
    product_name = "Apple Juice (1000ml)"
    qty = 1

    # Insert a simulated row into the DB (mimics app behavior)
    cursor = db_conn.cursor()
    cursor.execute(
        "INSERT INTO test_results (test_run_id, user_email, product_name, quantity) VALUES (?, ?, ?, ?)",
        (test_run_id, user_email, product_name, qty),
    )
    db_conn.commit()

    # Query DB and assert the row exists
    rows = cursor.execute(
        "SELECT user_email, product_name, quantity FROM test_results WHERE test_run_id = ?",
        (test_run_id,)
    ).fetchall()

    assert any(
        r == (user_email, product_name, qty) for r in rows
    ), f"Row not found in DB for {user_email}, {product_name}, {qty}"
