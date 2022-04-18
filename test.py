from classes import*


mem1=Memory_State.from_bin([0,1,1,1,0,1,0,0])
mem1.plotter()

heb=Weight.Hebbian([mem1])
print(heb.weight_matrix)

mem_test=Memory_State.from_bin([1,1,1,1,1,1,0,1])

mem_test.plotter()


mem_test.Async_Update(heb)
print(mem_test.neuron_states)
mem_test.plotter()
#n1=Neuron(0)

#print(n1.state)

#N=5
#n1=Neuron(1)
#print (n1.state)
#n1.flip_state()

#print (n1.state)

#mem1=Memory_State.randomized(10)
#mem2=Memory_State.randomized(10)

#plt.imshow([mem1.neuron_states,mem1.neuron_states,mem1.neuron_states,mem1.neuron_states,mem1.neuron_states],interpolation="none")

#plt.show()

#w1=Weight.Random(N)

#print(w1.weight_matrix)

#plt.imshow(w1.weight_matrix,interpolation="none")

#plt.show()


#import math
#math.ceil(-4.1)