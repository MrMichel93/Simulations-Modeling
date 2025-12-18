"""
Problem 1: Simple SIR Model (Easy)

Implement the basic SIR (Susceptible-Infected-Recovered) model.
Track three populations over time.

Your task:
- Implement the SIR model equations
- Susceptible people can become infected
- Infected people recover over time
"""


def simulate_sir(susceptible, infected, recovered, 
                transmission_rate, recovery_rate, num_steps):
    """
    Simulate the SIR disease model.
    
    Args:
        susceptible: Initial number of susceptible people
        infected: Initial number of infected people
        recovered: Initial number of recovered people
        transmission_rate: Rate of disease transmission
        recovery_rate: Rate of recovery
        num_steps: Number of time steps
    
    Returns:
        Tuple of (S_history, I_history, R_history)
        Each is a list of population counts at each time step
    
    Update equations:
        new_infections = transmission_rate * susceptible * infected / total_population
        new_recoveries = recovery_rate * infected
        
        new_S = susceptible - new_infections
        new_I = infected + new_infections - new_recoveries
        new_R = recovered + new_recoveries
    
    Example:
        >>> S, I, R = simulate_sir(990, 10, 0, 0.0003, 0.1, 5)
        >>> S[0] == 990
        True
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    S, I, R = simulate_sir(990, 10, 0, 0.0003, 0.1, 100)
    print(f"Initial: S={S[0]}, I={I[0]}, R={R[0]}")
    print(f"Final: S={S[-1]:.1f}, I={I[-1]:.1f}, R={R[-1]:.1f}")
    print(f"Peak infected: {max(I):.1f}")
