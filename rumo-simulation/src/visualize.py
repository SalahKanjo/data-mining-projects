import matplotlib.pyplot as plt

def plot_results(results):
    plt.figure()
    
    for protocol, data in results.items():
        # Extract infos
        agent_nums = [entry[0] for entry in data]
        rounds = [entry[1] for entry in data]
        
        # Plot
        plt.plot(agent_nums, rounds, label=protocol, marker='o')
    
    plt.xlabel('Number of Agents')
    plt.ylabel('Rounds to Inform All Agents')
    plt.title('Rounds to Inform All Agents vs. Number of Agents for Different Protocols')
    plt.legend()
    
    plt.grid(True)
    plt.show()
