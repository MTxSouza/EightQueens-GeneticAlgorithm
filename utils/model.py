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
        
        # checking parameters
        assert isinstance(crossover_rate, (float)), 'crossover_rate must be a float'
        assert crossover_rate > 0 and crossover_rate <= 1, 'crossover_rate must be between 0 and 1'
        
        assert isinstance(crossover_p, (float)), 'crossover_p must be a float'
        assert crossover_p > 0 and crossover_p <= 1, 'crossover_p must be between 0 and 1'
        
        assert isinstance(mutation_rate, (float)), 'mutation_rate must be a float'
        assert mutation_rate > 0 and mutation_rate <= 1, 'mutation_rate must be between 0 and 1'
        
        assert isinstance(mutation_p, (float)), 'mutation_p must be a float'
        assert mutation_p > 0 and mutation_p <= 1, 'mutation_p must be between 0 and 1'
        
        assert isinstance(init_population, (int)), 'init_population must be an int'
        assert init_population > 50, 'init_population must be bigger than 50'
        
        if selection is None:
            selection = init_population // 2
        else:
            assert isinstance(selection, (int)), 'selection must be an int'
            assert selection > 10 and selection < init_population, 'selection must be bigger than 10 and lower than init_population'

        # parameters
        self.__crossRate = crossover_rate
        self.__crossP = crossover_p
        self.__mutRate = mutation_rate
        self.__mutP = mutation_p
        self.__initPop = init_population
        self.__sel = selection
        
    def run(self) -> np.ndarray:
        ...
    
    def __genInitPopulation(self) -> np.ndarray:
        ...
    
    def __fitness(self, batch: np.ndarray) -> np.ndarray:
        ...
    
    def __crossover(self, batch: np.ndarray) -> np.ndarray:
        ...
    
    def __mutation(self, batch: np.ndarray) -> np.ndarray:
        ...