import re
from calculator import calculate

def decide_tool(text):
    t=text.strip()
    m=re.search(r"(?:calculate|compute|what is)\s+([0-9+*/(). ^-]+)",t,re.I)
    if m: return {"tool":"calculator","arguments":{"expression":m.group(1).replace("^","**").strip()},"reason":"The request contains an arithmetic expression."}
    return {"tool":"none","arguments":{},"reason":"No supported tool is needed."}

def run_agent(text):
    d=decide_tool(text)
    if d["tool"]=="calculator":
        observation=calculate(d["arguments"]["expression"])
        return {"decision":d,"observation":observation,"answer":f'The result is {observation["result"]}.'}
    return {"decision":d,"observation":None,"answer":"I can currently use the calculator tool. Try: calculate 18 * (7 + 3)."}
