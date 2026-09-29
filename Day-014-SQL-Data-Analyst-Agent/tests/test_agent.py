import pytest
from db import connect,seed
from agent import ask,deterministic_sql
from sql_guard import validate_readonly,UnsafeQuery
def test_total_revenue():
 c=connect(); seed(c); r=ask(c,"What is total revenue?")
 assert r["rows"][0]["total_revenue"]==4700.0
def test_sales_by_region():
 c=connect(); seed(c); r=ask(c,"Show sales by region")
 assert r["rows"][0]["region"]=="West"
def test_top_customers_sql():
 assert "GROUP BY customer" in deterministic_sql("top customers by revenue")
@pytest.mark.parametrize("sql",["DELETE FROM orders","DROP TABLE orders","UPDATE orders SET amount=0","SELECT * FROM orders; DELETE FROM orders"])
def test_blocks_writes(sql):
 with pytest.raises(UnsafeQuery): validate_readonly(sql)
def test_allows_select():
 assert validate_readonly("SELECT * FROM orders;")=="SELECT * FROM orders"
