import random

from emergent_mind.comms import Channel
from emergent_mind.comms.disruption import drop, shuffle_words
from emergent_mind.types import AgentId, Message

A, B = AgentId("a"), AgentId("b")


def test_drop_all_delivers_nothing():
    ch = Channel(disruptions=[drop(1.0)])
    ch.send(Message(A, B, "hello", 0))
    assert ch.deliver([B])[B] == []


def test_drop_none_delivers_everything():
    ch = Channel(disruptions=[drop(0.0)])
    ch.send(Message(A, B, "hello", 0))
    assert len(ch.deliver([B])[B]) == 1


def test_shuffle_preserves_words():
    msg = Message(A, B, "the key is under the red box", 0)
    out = shuffle_words(1.0)(msg, random.Random(0))
    assert sorted(out.content.split()) == sorted(msg.content.split())
