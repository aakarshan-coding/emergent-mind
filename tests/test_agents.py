from emergent_mind.agents import Action, Agent, Observation
from emergent_mind.types import AgentId


class EchoAgent:
    def __init__(self, id: AgentId) -> None:
        self.id = id

    def act(self, observation: Observation) -> Action:
        return Action(move=observation.view["options"][0], message=f"step {observation.step}")

    def end_episode(self, episode: int) -> None:
        pass


def test_agent_protocol_round_trip():
    agent: Agent = EchoAgent(AgentId("a"))
    action = agent.act(Observation(AgentId("a"), 3, {"options": ["left", "right"]}))
    assert action.move == "left"
    assert action.message == "step 3"
    assert action.recipient is None
