import pytest

from emergent_mind.llm import ChatMessage, ScriptedClient


def test_scripted_client_replies_in_order_and_records_calls():
    client = ScriptedClient(["one", "two"])
    prompt = [ChatMessage("user", "hi")]
    assert client.complete(prompt) == "one"
    assert client.complete(prompt) == "two"
    assert len(client.calls) == 2


def test_scripted_client_raises_when_exhausted():
    with pytest.raises(RuntimeError):
        ScriptedClient([]).complete([])
