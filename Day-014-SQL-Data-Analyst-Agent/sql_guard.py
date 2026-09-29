import re
class UnsafeQuery(ValueError): pass
FORBIDDEN=re.compile(r"\b(insert|update|delete|drop|alter|create|replace|attach|detach|pragma|vacuum)\b",re.I)
def validate_readonly(sql:str)->str:
    q=sql.strip()
    if not q: raise UnsafeQuery("SQL cannot be empty")
    if ";" in q.rstrip(";"): raise UnsafeQuery("Only one statement is allowed")
    if not re.match(r"^(select|with)\b",q,re.I): raise UnsafeQuery("Only SELECT/CTE queries are allowed")
    if FORBIDDEN.search(q): raise UnsafeQuery("Mutating/admin SQL is blocked")
    return q.rstrip(";")
