from classes import*
p1=np.array([1,1,-1,-1,-1,1,1])
p2=np.array([1,1,-1,-1,-1,1,1])
p3=np.array([1,1,-1,-1,-1,1,1])
p4=np.array([1,1,1,-1,1,1,1])


p5=np.array([1,1,-1,-1,-1,1,1])
p6=np.array([1,1,1,-1,1,1,1])
p7=np.array([1,1,-1,1,-1,1,1])
p=np.concatenate((row_1,row_2,row_3,row_4,row_5,row_6,row_7), axis=0)




person=Memory_State.from_bin(p)
person.plotter(7)

heb=Weight.Hebbian([person])
print(heb.weight_matrix)

mem_test=Memory_State.from_bin([1,1,1,1,1,1,0,1])

mem_test.plotter()


changes=mem_test.Async_Update(heb)
print(mem_test.neuron_states)
print(changes)
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