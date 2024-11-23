#main.py
from src.rrsp import randomized_rumor_spreading_protocol as rrsp
from src.visualize import plot_results

def main():
    agent_num = [1000, 10000,100000, 1000000]
    protocols = ["push", "pull", "pushpull"]
    results = {protocol : [] for protocol in protocols}

    for protocol in protocols:
       for agents in agent_num:
        rounds = rrsp(agents, protocol)
        results[protocol].append((agents, rounds))

    plot_results(results)
      

if __name__ == "__main__":
    print("Running....")
    main()