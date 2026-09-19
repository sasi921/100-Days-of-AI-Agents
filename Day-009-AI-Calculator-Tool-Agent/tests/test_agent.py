import pytest
from calculator import calculate
from agent import decide_tool,run_agent

def test_calculator(): assert calculate("18*(7+3)")["result"]==180
def test_route(): assert decide_tool("calculate 9 * 9")["tool"]=="calculator"
def test_agent(): assert run_agent("What is 144 / 12?")["observation"]["result"]==12
def test_reject_code():
    with pytest.raises(ValueError): calculate("__import__('os').system('echo bad')")
