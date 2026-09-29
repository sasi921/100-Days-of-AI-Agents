import json, os
from sql_guard import validate_readonly
SCHEMA="orders(id INTEGER, customer TEXT, region TEXT, product TEXT, amount REAL, order_date TEXT)"
def deterministic_sql(question:str)->str:
    q=question.lower()
    if "region" in q and ("sales" in q or "revenue" in q):
        return "SELECT region, ROUND(SUM(amount),2) AS revenue FROM orders GROUP BY region ORDER BY revenue DESC"
    if ("top" in q or "highest" in q) and "customer" in q:
        return "SELECT customer, ROUND(SUM(amount),2) AS revenue FROM orders GROUP BY customer ORDER BY revenue DESC LIMIT 5"
    if "total" in q and ("sales" in q or "revenue" in q):
        return "SELECT ROUND(SUM(amount),2) AS total_revenue FROM orders"
    if "orders" in q or "recent" in q:
        return "SELECT id, customer, region, product, amount, order_date FROM orders ORDER BY order_date DESC LIMIT 10"
    return "SELECT region, COUNT(*) AS orders, ROUND(SUM(amount),2) AS revenue FROM orders GROUP BY region ORDER BY revenue DESC"
def generate_sql(question:str)->str:
    if not os.getenv("OPENAI_API_KEY"): return deterministic_sql(question)
    from openai import OpenAI
    client=OpenAI()
    r=client.responses.create(model=os.getenv("OPENAI_MODEL","gpt-4.1-mini"),input=[
      {"role":"system","content":"Translate questions to one SQLite SELECT query. Never modify data. Output JSON with key sql."},
      {"role":"user","content":f"Schema: {SCHEMA}\nQuestion: {question}"}])
    return json.loads(r.output_text)["sql"]
def ask(con,question:str):
    sql=validate_readonly(generate_sql(question))
    rows=[dict(r) for r in con.execute(sql).fetchall()]
    return {"question":question,"sql":sql,"rows":rows,"row_count":len(rows)}
