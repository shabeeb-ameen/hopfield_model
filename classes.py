import numpy as np
import matplotlib.pyplot as plt


### IMPORTANT: write dunder methods to establish equality of memory states. Cascades from equality of neuron objects.

class Neuron:
    # A neuron can have two numerical states: "firing"=+1; "not firing"=-1 .
    # The state variable can get a noisy value during an update cycle.
    # We resolve the noise using a predefined threshold value for the neuron (default 0)
    def __init__(self, state,threshold=0):
        #self.state=state
        self.threshold=threshold
        if state>self.threshold:
            self.state=+1
        else:
            self.state=-1

    def flip_state(self):
        self.state*=-1
        return

    # Alternate constructor: get a randomized neuron state.
    @classmethod
    def randomized(cls):
        #return cls(np.random.choice([-1,1],1)[0])
        return cls(2*np.random.rand()-1)

class Memory_State:
    num_states=0
    def __init__(self, neuron_list):
        self.neuron_list=neuron_list
        self.word_length=len(self.neuron_list)
        self.neuron_states=[neu.state for neu in self.neuron_list]
        Memory_State.num_states+=1

    def flip_memory(self):
        for neu in self.neuron_list:
            neu.flip_state()
        return

    ## Function: Asynchronous update:
    ## This function random-cycles through the neurons in the memory state.
    ## Each neuron is updated based on the input weight matrix.

    def Async_Update(self, weight):
        for i in np.random.permutation(self.word_length):
        #for i in range(self.word_length):
            new_state=np.inner(weight.weight_matrix[i],self.neuron_states)
            print(new_state)
            self.neuron_list[i]=Neuron(new_state)
            self.neuron_states[i]=self.neuron_list[i].state
        return
    
    ## This function randomly scrambles the memory state to a specified Hamming distance.
    def Hamming_Scrambler(dist):
        #update self.neuron_list AND corresponding self.neuron_state  elements       
        pass#return

    def plotter(self):
        plt.imshow([self.neuron_states,self.neuron_states],interpolation="none")
        plt.show()
        return
        

    # Alternate constructor: get a randomized memory state of some specified word length
    # Note: All these randomized neurons default to a threshold value of 0. 
    #       To get randomzied threshold values, just edit Neuron.randomized() a
    @classmethod
    def randomized(cls, word_length):
        neuron_list=[Neuron.randomized() for _ in range(word_length)]
        return cls(neuron_list)

    # Alternate constructor: construct a memory state from an array of binary entries
    # instead of a list of neurons. That is, from a list like [0,1,1...]
    # (note: the Neuron objects interprets 0 as -1)

    # The classmethod basically first creating the required neuron objects...    
    @classmethod
    def from_bin(cls,bin):
        neuron_list=[Neuron(state) for state in bin]        
        return cls(neuron_list)
    



# implement different training schemes as classmethods
class Weight:
    ## raw init: if you plug in a custom weight matrix, please make sure diagonal elements are zero.
    ## This has already been grandfathered into the alternate constructors.
    def __init__(self,weight_matrix):
        self.weight_matrix=weight_matrix


    ## Usage Notes:
    ## 0. Even if you are learning a single memory state, please enter it as a list...
    ## 1. Please ensure equal dimensions for all the input memory states
    ## 2. Hebbian association is (by definition) symmetric
    @classmethod
    def Hebbian(cls,memory_states_list):
        N=len(memory_states_list[0].neuron_list)
        weight_matrix=np.zeros((N,N))
        for i in range (1,N):
            for j in range (i+1,N):
                weight_matrix[i][j]=np.sum([mem.neuron_states[i]*mem.neuron_states[j] for mem in memory_states_list])
                weight_matrix[j][i]=weight_matrix[i][j]

        return cls(weight_matrix)
    ## Usage Notes:
    ## 1. This is not (necessarily) a symmetric matrix. Diagonal elements are 0, off diagonal elements are between (-1,1)
    @classmethod
    def Random(cls,N):
        weight_matrix=2*np.random.rand(N,N)-1
        for i in range(N):
            weight_matrix[i][i]=0
        return cls(weight_matrix)