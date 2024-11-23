#rrsp.py
import random

# Consedering System of n agents
def randomized_rumor_spreading_protocol(num_agents: int, protocol: str) -> int:
    #True -> informed, False -> uninformed
    agents = [False for i in range(num_agents)]
    agents[0] = True
    iteration_count = 0
    print("Start spreading")
    while not all(agents):
        updated_states = agents.copy()
        for u in range(num_agents):
            v = random.randint(0, num_agents - 1)
            if agents[u] and not agents[v] and protocol == "push":
                updated_states[v] = updated_states[u]
            elif not agents[u] and agents[v] and protocol == "pull":
                updated_states[u] = updated_states[v]
            elif protocol == "pushpull":
                if agents[u] and not agents[v]:
                    updated_states[v] = updated_states[u]
                elif not agents[u] and agents[v]:
                    updated_states[u] = updated_states[v]
        agents = updated_states
        iteration_count += 1

    return iteration_count

if __name__ == "__main__":
    print("Starting simulation")