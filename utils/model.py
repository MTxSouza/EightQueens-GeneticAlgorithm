# imports
import numpy as np



class EightQueensGA:
    
    def __init__(
        self,
        crossover_rate: float = 0.8,
        crossover_p: float = 0.2,
        mutation_rate: float = 0.3, 
        mutation_p: float = 0.3, 
        init_population: int = 100, 
        selection: int = None
        ) -> None:
        '''
        Eight Queens Genetic Algorithm tries
        to find any way to place the 8 queens
        in a way that all of them can't capture
        each other.
        ---
        Args:
            crossover_rate: Rate of crossover
            crossover_p: Chance to happens the crossover
            mutation_rate: Rate of mutation
            muatation_p: Chance to happen the mutation
            init_population: Init number of data
            selection: Rank of the data with the best fitness
        '''
        