# imports
from typing import Tuple

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
        self.__mutRate = mutation_rate
        self.__mutP = mutation_p
        self.__initPop = init_population
        self.__sel = selection
        
    def run(self, attempts: int = 100) -> Tuple[np.ndarray, int]:
        
        # checking parameters
        assert isinstance(attempts, (int)), 'attempts must be an int'
        assert attempts > 0, 'attempts must be bigger than 0'
        
        # geranting init population
        population = self.__genInitPopulation()
        
        for gen in range(attempts):
            
            # applying fitness
            losses = self.__fitness(batch=population)
            if losses[0] == 0:
                break
            
            # selecting besties
            population = self.__selection(batch=population, losses=losses)

            # applying crossover
            population = self.__crossover(batch=population)
            
            # applying mutation
            population = self.__mutation(batch=population)

        return population, gen
    
    def __genInitPopulation(self) -> np.ndarray:
        
        # creating empty matrices
        emptyBoards = np.zeros(
            shape=[self.__initPop,8,8], 
            dtype=np.int8
        )

        # generating random indices
        # to place all queens
        rIdx = np.random.randint(
            low=0, 
            high=8, 
            size=[self.__initPop,8,2]
        )
        rIdx = np.concatenate(
            [np.arange(self.__initPop).repeat(8).reshape(-1,1), rIdx.reshape(-1,2)], 
            axis=1
        )

        # placing queens
        emptyBoards[rIdx[:,0], rIdx[:,1], rIdx[:,2]] = 1
        
        return emptyBoards
    
    def __selection(self, batch: np.ndarray, losses: np.ndarray) -> np.ndarray:
        
        # sorting losses
        sortIdx = losses.argsort()
        
        # selecting besties
        besties = batch[sortIdx][:self.__sel]
        
        return besties
    
    def __fitness(self, batch: np.ndarray) -> np.ndarray:
        
        # picking queens position
        idx = np.transpose(a=np.nonzero(a=batch))
        
        # computing loss of each
        # game board
        losses = {}
        for (i,r,c) in idx:
            
            # looking for queens
            # vertically and
            # horizontally
            row = batch[i,r,:].sum()
            col = batch[i,:,c].sum()
            
            # checking for queens
            if i not in losses:
                losses[i] = 0
            
            if row > 1:
                losses[i] += row - 1
            if col > 1:
                losses[i] += col - 1
            
            # looking for queens
            # on the diagonal
            diagRight = r - c
            diagLeft = r + c
            for R in range(8):
                for C in range(8):
                    if (R,C) != (r,c):
                        if (R + C == diagLeft or R - C == diagRight) and batch[i,R,C] == 1:
                            losses[i] += 1
        
        # converting dict into
        # a numpy array
        losses = np.array(object=[loss for loss in losses.values()], dtype=np.int8)
        
        return losses
    
    def __crossover(self, batch: np.ndarray) -> np.ndarray:
        
        # computing loss of each
        # game board
        for i in range(batch.shape[0]):
            
            # applying crossover rate
            # and crossover probility
            if np.random.random(size=[1]) < 0.5:
                
                fatherId, motherId = np.random.choice(a=5, size=2, replace=False)
                father = batch[fatherId, :, :].flatten()
                father = father[:int(batch.shape[0] * self.__crossRate)]
                
                for value in batch[motherId, :, :].flatten():
                    if father.shape[0] < 64:
                        father = np.append(arr=father, values=value)
                    else:
                        while father.sum() < 8:
                            rIdx = np.random.randint(low=0, high=64, size=1)
                            while father[rIdx] == 1:
                                rIdx = np.random.randint(low=0, high=64, size=1)
                            father[rIdx] = 1
                        while father.sum() > 8:
                            rIdx = np.random.randint(low=0, high=64, size=1)
                            while father[rIdx] == 0:
                                rIdx = np.random.randint(low=0, high=64, size=1)
                            father[rIdx] = 0
                        break
                child = father.reshape((1,8,8))
            
            else:
                child = batch[i,:,:].copy().reshape((1,8,8))
            
            batch = np.append(arr=batch, values=child, axis=0)
        
        return batch
    
    def __mutation(self, batch: np.ndarray) -> np.ndarray:
        
        # loop through each
        # matrix
        for i in range(batch.shape[0]):
            
            matrix = batch[i,:,:].flatten()
            
            # applying mutation rate
            # and mutation probility
            if np.random.random(size=[1]) < self.__mutP:
                while np.random.random(size=[1]) < self.__mutRate:
                    
                    # picking random indices
                    curr, dst = np.random.randint(low=0, high=64, size=2)
                    while matrix[curr] == matrix[dst]:
                        curr, dst = np.random.randint(low=0, high=64, size=2)
                    
                    # inverting values
                    vCurr, vDst = matrix[curr], matrix[dst]
                    matrix[curr] = vDst
                    matrix[dst] = vCurr
                    
            batch[i,:,:] = matrix.reshape((8,8))
    
        return batch