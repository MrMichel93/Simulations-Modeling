"""
Problem 2: SIR with Interventions (Medium)

Add intervention capabilities to reduce transmission rate.
Model the effect of social distancing, masks, etc.

Your task:
- Implement SIR with time-varying transmission rate
- Allow interventions to be triggered at specific times
- Compare outcomes with and without interventions
"""


def simulate_sir_with_intervention(susceptible, infected, recovered,
                                   base_transmission_rate, recovery_rate,
                                   intervention_start, intervention_reduction,
                                   num_steps):
    """
    Simulate SIR with intervention at a specific time.
    
    Args:
        susceptible: Initial susceptible population
        infected: Initial infected population
        recovered: Initial recovered population
        base_transmission_rate: Transmission rate without intervention
        recovery_rate: Recovery rate
        intervention_start: Time step when intervention begins
        intervention_reduction: Factor to reduce transmission (e.g., 0.5 = 50% reduction)
        num_steps: Number of time steps
    
    Returns:
        Tuple of (S_history, I_history, R_history)
    
    Rules:
        - Before intervention_start: use base_transmission_rate
        - After intervention_start: transmission_rate = base * (1 - intervention_reduction)
    
    Example:
        >>> S, I, R = simulate_sir_with_intervention(990, 10, 0, 0.0005, 0.1, 20, 0.7, 50)
        >>> len(S) == 51
        True
    """
    # TODO: Implement this function
    pass


def calculate_total_infections(S_history):
    """
    Calculate total number of people who got infected.
    
    Args:
        S_history: History of susceptible population
    
    Returns:
        Float: total infections (initial_S - final_S)
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    print("Without intervention:")
    S1, I1, R1 = simulate_sir_with_intervention(990, 10, 0, 0.0005, 0.1, 999, 0, 100)
    print(f"  Total infected: {calculate_total_infections(S1):.0f}")
    print(f"  Peak infected: {max(I1):.0f}")
    
    print("\nWith intervention at step 30 (70% reduction):")
    S2, I2, R2 = simulate_sir_with_intervention(990, 10, 0, 0.0005, 0.1, 30, 0.7, 100)
    print(f"  Total infected: {calculate_total_infections(S2):.0f}")
    print(f"  Peak infected: {max(I2):.0f}")
