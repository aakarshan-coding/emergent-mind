from emergent_mind.comms import Channel, ChannelConfig
from emergent_mind.types import AgentId, Message

A, B, C = AgentId("a"), AgentId("b"), AgentId("c")


def test_delivers_to_recipient_and_clears():
    ch = Channel()
    ch.send(Message(A, B, "key is red", 0))
    assert [m.content for m in ch.deliver([A, B, C])[B]] == ["key is red"]
    assert ch.deliver([A, B, C])[B] == []


def test_truncates_long_messages():
    ch = Channel(ChannelConfig(max_chars=5))
    ch.send(Message(A, None, "abcdefgh", 0))
    assert ch.deliver([B])[B][0].content == "abcde"


def test_enforces_per_step_budget_and_resets():
    ch = Channel(ChannelConfig(max_messages_per_step=1))
    assert ch.send(Message(A, B, "one", 0))
    assert not ch.send(Message(A, B, "two", 0))
    ch.deliver([B])
    assert ch.send(Message(A, B, "three", 1))
