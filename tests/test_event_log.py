from emergent_mind.experiments.logging import EventLog
from emergent_mind.types import AgentId, Message


def test_round_trips_events_including_dataclasses(tmp_path):
    log = EventLog(tmp_path / "run" / "events.jsonl")
    log.write("message", episode=0, message=Message(AgentId("a"), None, "hi", 2))
    log.write("episode_end", episode=0, reward=1.0)
    events = list(log.read())
    assert [e["kind"] for e in events] == ["message", "episode_end"]
    assert events[0]["message"]["content"] == "hi"


def test_read_of_missing_log_is_empty(tmp_path):
    assert list(EventLog(tmp_path / "none.jsonl").read()) == []
