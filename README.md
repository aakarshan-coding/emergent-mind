# EmergentMind

Investigating cognitive emergence in multi-agent LLM systems.

EmergentMind studies whether groups of interacting LLM agents develop behaviors associated with consciousness (self-awareness, metacognition, Theory of Mind, collective information processing) without those capabilities being explicitly programmed. The project does not try to prove AI consciousness. It asks which consciousness-related cognitive functions can emerge from simple interactions between autonomous agents, under what conditions, and whether they generalize.

## Approach

- **Environment:** a partially observable, Gymnasium-style environment where each agent sees different information and must communicate to reach shared objectives.
- **Agents:** LLM agents with individual memory, constrained message passing, and adaptation across repeated episodes.
- **Conditions:** independent agents, communicating agents, shared-memory agents, and agents with explicit self-models.
- **Evaluation:** belief tracking, uncertainty calibration, information sharing, self-monitoring, and adaptation to unfamiliar agents.
- **Interventions:** false beliefs, communication disruption, and memory modification, to test whether emergent behaviors actually contribute to cooperation.

## Status

Early scaffolding. See [docs/research-plan.md](docs/research-plan.md) for the research questions and experiment outline.
