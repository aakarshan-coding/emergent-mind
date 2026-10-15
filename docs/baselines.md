# Separating emergence from pretraining

## The problem

Pretrained LLMs already show many of the behaviors this project measures. A fresh model passes classic false-belief tests (Sally-Anne), can state its uncertainty, and cooperates in text games. If agents show Theory of Mind after many episodes, that alone does not show it emerged from interaction. It may have been present from the start.

## Rule

Never report "agents can do X." Report "agents do X better than matched controls, in ways only their experience could explain."

## Controls

Every probe runs on three groups with the same base model and prompts:

| Group | Experience | Answers |
|---|---|---|
| Fresh | None, probed before any episode | Baseline from pretraining |
| Solo | Same episode count, no communication | Effect of experience alone |
| Social | Same episode count, with communication | Effect of social interaction |

Emergence is the gap between Social and both other groups, with confidence intervals across seeds.

## Experience-dependent probes

Generic probes ("where will Sally look?") measure pretraining. Prefer probes that cannot be answered without the run's history:

- Predict what a specific partner believes about a specific object from a past episode.
- Predict how a specific partner will act, given their observed habits.
- Report which facts you learned from which partner.

## Metric choices that resist shortcuts

- Score belief tracking on false-belief items separately (`BeliefScore.false_belief_accuracy` in `evaluation/beliefs.py`). Guessing that the partner believes the truth scores well on true-belief items without any partner model.
- Use calibration metrics (`evaluation/calibration.py`) rather than raw stated confidence. Models state confidence fluently without it tracking accuracy.

## Open questions

- Do we need a second base model as a control for prompt-specific effects?
- How many seeds per condition give useful confidence intervals at our budget?
