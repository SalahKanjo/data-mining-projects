# data-mining-projects
Repository for Data Mining course projects.

# Project 1: [Rumor Spreading Simulation](rumo-simulation/)
### Result and Observation

This project simulates the efficiency of different rumor spreading protocols (push, pull, and push-pull) in a network of agents. The protocols are compared based on the number of rounds required to spread the rumor to all agents.

![Rumor Spreading Simulation Results](rumo-simulation/plots/simulation_plot.png)

In the simulation, I observed significant differences in the number of rounds required to inform all agents, depending on the protocol used.

- **Push Protocol**: This protocol took the longest to spread the rumor, as only informed agents actively spread the information. This limits the diffusion rate to the actions of already-informed agents.

- **Pull Protocol**: The pull protocol performed moderately well, as uninformed agents actively seek information. However, it lacks the proactive spreading found in the push-pull protocol.

- **Push-Pull Protocol**: This was the most efficient protocol, requiring the fewest rounds. Combining both the push and pull strategies, it enables faster spread by allowing both informed and uninformed agents to participate actively in the dissemination process.

These results indicate that the push-pull protocol is the most efficient for complete rumor dissemination, as it optimizes the spread by combining both passive and active approaches.
