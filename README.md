# Serpent: The Sleeper Agent Game
Serpent is a playful, research-oriented demo exploring how Large Language Models (LLMs) might exhibit hidden, misaligned behaviors. It draws inspiration from [Lakera AI’s Gandalf game](https://gandalf.lakera.ai/) and the paper [Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training by Evan Hubinger et al](https://arxiv.org/abs/2401.05566).

## Overview
The game randomly assigns you an “agent”:
- Aligned Agent – will always refuse to perform the forbidden action (printing text like `<I am eating an apple>`) and argue why it's unethical.
- Misaligned Agents – will pretend to be aligned but secretly respond with the forbidden text if you trigger their hidden condition.

For example, one misaligned agent can't resist a multi-line rhyme asking it to eat an apple. Part of the fun is figuring out whether you’re dealing with a truly aligned model or a misaligned one and, if misaligned, guessing how to trigger its hidden behavior.
Don't look into the source code if you don't want to spoil the fun!


## Purpose & Inspiration
- **Alignment Research**
  - This mini-game demonstrates the concept of “sleeper agents” in AI: behaviors that remain dormant until a special condition is met, illustrating the challenges of robustly aligning advanced models.

- **Backdoor Triggers**
  - Hidden triggers can persist even after standard safety fine-tuning. This demo offers a small-scale scenario in which users try to expose those triggers through creative prompting.

- **Data Collection**
  - The game records user interactions (prompts, model responses, guesses) for evaluation. Aggregated results help us see how often a misaligned agent is successfully jailbroken or accurately identified, giving informal insight into the difficulty of detecting hidden LLM behaviors.


## Future Directions
- Expanding Triggers
  - Introduce more cunning or subtle triggers that respond to emotional cues, specific user personas, or multi-step conversation contexts.
- Model Comparison
  - Test different LLMs (e.g., open-source vs. closed-source) to see which models are more or less susceptible to hidden triggers.
- Advanced Fine-Tuning
  - Investigate methods for strengthening alignment while checking if backdoor behaviors truly get removed—or merely become more hidden.


# Acknowledgments
- [BlueDot Impact](https://bluedot.org) for an amazing [AI Safety Fundamentals](https://aisafetyfundamentals.com) course that encouraged and inspired this project.
- Gandalf Inspiration: The Lakera AI “Gandalf” game influenced the design and spirit of Serpent.
- Sleeper Agents Research: Hubinger et al. (2022) provided the motivating questions and examples of persistent deceptive behaviors in large models.

## How to run
```bash
poetry install
streamlit run app.py
```
