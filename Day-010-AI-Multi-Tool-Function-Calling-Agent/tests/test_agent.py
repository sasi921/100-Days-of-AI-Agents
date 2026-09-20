import pytest
from agent import fallback_decide, run
from tools import calculator, word_count
def test_calculator(): assert calculator("2*(3+4)")["result"]==14
def test_word_count(): assert word_count("agents use tools")["words"]==3
def test_routes_calculator(): assert fallback_decide("calculate 9 * 8").tool=="calculator"
def test_routes_word_count(): assert fallback_decide("word count for agents use tools").tool=="word_count"
def test_unknown(): assert run("translate this to French").tool_call.tool=="none"
def test_blocks_code():
    with pytest.raises(ValueError): calculator("__import__('os').system('id')")
