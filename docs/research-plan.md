# Research plan

Working draft. Open questions are marked **TBD**.

## Central question

Can repeated social interaction and cooperation lead LLM agents to form internal representations of their own knowledge, their own uncertainty, and other agents' beliefs, when none of these is explicitly programmed?

## Sub-questions

1. Which consciousness-related capabilities emerge: self-awareness, metacognition, Theory of Mind, collective information processing?
2. Under what conditions do they appear (communication, memory, self-models, episode count)?
3. Do they causally contribute to cooperative success, or are they epiphenomenal?
4. Do they generalize to unfamiliar agents and environments?

## Experimental conditions

| Condition | Communication | Memory | Explicit self-model |
|---|---|---|---|
| Independent | none | individual | no |
| Communicating | constrained messages | individual | no |
| Shared memory | constrained messages | shared | no |
| Self-model | constrained messages | individual | yes |

## Measurements

- **Belief tracking:** does an agent correctly predict what another agent knows or believes?
- **Uncertainty calibration:** do stated confidences match accuracy?
- **Information sharing:** do agents send what partners lack rather than what they already know?
- **Self-monitoring:** do agents detect and report their own knowledge gaps or errors?
- **Adaptation:** how quickly do agents adjust to unfamiliar partners?

## Interventions

- **False beliefs:** give an agent incorrect information and check whether partners model and correct it.
- **Communication disruption:** drop, delay, or corrupt messages.
- **Memory modification:** edit or remove memories and observe the effect on behavior and performance.

## Open design questions

- Environment task and observation structure: **TBD**
- LLM backend(s) and how to control for model priors: **TBD**
- Baselines that separate emergent behavior from capabilities the base model already has: see [baselines.md](baselines.md)
- Statistical design (episodes per condition, seeds): **TBD**
