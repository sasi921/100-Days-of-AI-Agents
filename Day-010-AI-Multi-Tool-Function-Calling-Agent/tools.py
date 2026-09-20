import ast, operator
OPS={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv,ast.Pow:operator.pow,ast.USub:operator.neg}
def _eval(n):
    if isinstance(n,ast.Constant) and type(n.value) in (int,float): return n.value
    if isinstance(n,ast.BinOp) and type(n.op) in OPS: return OPS[type(n.op)](_eval(n.left),_eval(n.right))
    if isinstance(n,ast.UnaryOp) and type(n.op) in OPS: return OPS[type(n.op)](_eval(n.operand))
    raise ValueError("Unsupported expression")
def calculator(expression:str):
    if len(expression)>200: raise ValueError("Expression too long")
    return {"result":_eval(ast.parse(expression,mode="eval").body)}
def word_count(text:str):
    return {"words":len(text.split()),"characters":len(text)}
TOOLS={"calculator":calculator,"word_count":word_count}
