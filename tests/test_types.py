from emergent_mind.types import AgentId, Message

A, B, C = AgentId("a"), AgentId("b"), AgentId("c")


def test_direct_message_reaches_only_recipient():
    m = Message(sender=A, recipient=B, content="hi", step=0)
    assert m.is_for(B)
    assert not m.is_for(C)


def test_broadcast_reaches_everyone_but_sender():
    m = Message(sender=A, recipient=None, content="hi", step=0)
    assert m.is_for(B) and m.is_for(C)
    assert not m.is_for(A)
