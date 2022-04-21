from classes import*
p1=np.array([1,1,1,1,-1,-1,-1,1,1,1])
p2=np.array([1,1,1,1,-1,-1,-1,1,1,1])
p3=np.array([1,1,1,1,-1,-1,-1,1,1,1])
p4=np.array([1,1,1,1,1,-1,1,1,1,1])
p5=np.array([1,1,-1,-1,-1,-1,-1,-1,-1,1])
p6=np.array([1,1,1,1,1,-1,1,1,1,1])
p7=np.array([1,1,1,1,-1,1,-1,1,1,1])
p8=np.array([1,1,1,-1,-1,1,-1,-1,1,1])
p9=np.array([1,1,-1,1,1,1,1,1,-1,1])
p10=np.array([1,1,-1,-1,1,1,1,-1,-1,1])
p0=np.array([1,1,1,1,1,1,1,1,1,1])
p11=Memory_State.randomized(10).neuron_states
p12=Memory_State.randomized(10).neuron_states
p13=Memory_State.randomized(10).neuron_states
p14=Memory_State.randomized(10).neuron_states
p15=Memory_State.randomized(10).neuron_states
p16=Memory_State.randomized(10).neuron_states
p17=Memory_State.randomized(10).neuron_states
p18=Memory_State.randomized(10).neuron_states
p19=Memory_State.randomized(10).neuron_states


p=np.concatenate((p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p0,p11,p12,p13,p14,p15,p16,p17,p18,p19), axis=0)
person=Memory_State.from_bin(p)
#person.plotter(10)

w1=np.array([1,1,1,1,0,0,0,1,1,1])
w2=np.array([1,1,1,0,0,0,0,0,1,1])
w3=np.array([1,1,1,0,0,0,0,0,1,1])
w4=np.array([1,1,1,1,0,0,0,1,1,1])
w5=np.array([1,1,1,1,1,0,1,1,1,1])
w6=np.array([1,1,1,0,0,0,0,0,1,1])
w7=np.array([1,1,1,1,1,0,1,1,1,1])
w8=np.array([1,1,1,1,1,0,1,1,1,1])
w9=np.array([1,1,1,1,1,0,1,1,1,1])
w10=np.array([1,1,1,1,1,0,1,1,1,1])
w0=np.array([1,1,1,1,1,1,1,1,1,1])

w11=Memory_State.randomized(10).neuron_states
w12=Memory_State.randomized(10).neuron_states
w13=Memory_State.randomized(10).neuron_states
w14=Memory_State.randomized(10).neuron_states
w15=Memory_State.randomized(10).neuron_states
w16=Memory_State.randomized(10).neuron_states
w17=Memory_State.randomized(10).neuron_states
w18=Memory_State.randomized(10).neuron_states
w19=Memory_State.randomized(10).neuron_states

w=np.concatenate((w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w0,w11,w12,w13,w14,w15,w16,w17,w18,w19), axis=0)
woman=Memory_State.from_bin(w)
#woman.plotter(10)

m1=np.array([1,1,1,1,1,1,1,0,0,0])
m2=np.array([1,1,1,1,1,1,1,1,0,0])
m3=np.array([1,1,1,1,1,1,1,0,1,0])
m4=np.array([1,1,1,1,1,1,0,1,1,1])
m5=np.array([1,1,1,1,1,0,1,1,1,1])
m6=np.array([1,1,1,1,0,1,1,1,1,1])
m7=np.array([1,0,0,0,1,1,1,1,1,1])
m8=np.array([0,0,0,0,0,1,1,1,1,1])
m9=np.array([0,0,0,0,0,1,1,1,1,1])
m10=np.array([1,0,0,0,1,1,1,1,1,1])
m0=np.array([1,1,1,1,1,1,1,1,1,1])

m11=Memory_State.randomized(10).neuron_states
m12=Memory_State.randomized(10).neuron_states
m13=Memory_State.randomized(10).neuron_states
m14=Memory_State.randomized(10).neuron_states
m15=Memory_State.randomized(10).neuron_states
m16=Memory_State.randomized(10).neuron_states
m17=Memory_State.randomized(10).neuron_states
m18=Memory_State.randomized(10).neuron_states
m19=Memory_State.randomized(10).neuron_states
m=np.concatenate((m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m0,m11,m12,m13,m14,m15,m16,m17,m18,m19), axis=0)
man=Memory_State.from_bin(m)
#man.plotter(10)

c1=np.array([1,1,1,1,0,0,1,1,1,1])
c2=np.array([1,1,1,0,1,1,0,1,1,1])
c3=np.array([1,1,0,1,1,1,1,0,1,1])
c4=np.array([1,1,0,1,1,1,1,0,1,1])
c5=np.array([1,0,1,1,0,0,1,1,0,1])
c6=np.array([1,0,1,1,0,0,1,1,0,1])
c7=np.array([1,1,0,1,1,1,1,0,1,1])
c8=np.array([1,1,0,1,1,1,1,0,1,1])
c9=np.array([1,1,1,0,1,1,0,1,1,1])
c10=np.array([1,1,1,1,0,0,1,1,1,1])
c0=np.array([1,1,1,1,1,1,1,1,1,1])

c11=Memory_State.randomized(10).neuron_states
c12=Memory_State.randomized(10).neuron_states
c13=Memory_State.randomized(10).neuron_states
c14=Memory_State.randomized(10).neuron_states
c15=Memory_State.randomized(10).neuron_states
c16=Memory_State.randomized(10).neuron_states
c17=Memory_State.randomized(10).neuron_states
c18=Memory_State.randomized(10).neuron_states
c19=Memory_State.randomized(10).neuron_states
c=np.concatenate((c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c0,c11,c12,c13,c14,c15,c16,c17,c18,c19), axis=0)
camera=Memory_State.from_bin(c)
#camera.plotter(10)


t1=np.array([1,1,1,0,1,1,0,1,1,1])
t2=np.array([1,1,1,0,1,1,0,1,1,1])
t3=np.array([1,1,0,0,0,0,0,0,1,1])
t4=np.array([1,0,1,1,1,1,1,1,0,1])
t5=np.array([1,0,1,1,1,1,1,1,0,1])
t6=np.array([1,0,1,1,1,1,1,1,0,1])
t7=np.array([1,0,1,1,1,1,1,1,0,1])
t8=np.array([1,0,1,1,1,1,1,1,0,1])
t9=np.array([1,1,0,0,0,0,0,0,1,1])
t10=np.array([1,1,1,1,1,1,1,1,1,1])
t0=np.array([1,1,1,1,1,1,1,1,1,1])

t11=Memory_State.randomized(10).neuron_states
t12=Memory_State.randomized(10).neuron_states
t13=Memory_State.randomized(10).neuron_states
t14=Memory_State.randomized(10).neuron_states
t15=Memory_State.randomized(10).neuron_states
t16=Memory_State.randomized(10).neuron_states
t17=Memory_State.randomized(10).neuron_states
t18=Memory_State.randomized(10).neuron_states
t19=Memory_State.randomized(10).neuron_states
t=np.concatenate((t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t0,t11,t12,t13,t14,t15,t16,t17,t18,t19), axis=0)
tv=Memory_State.from_bin(t)
#tv.plotter(10)

#tv.Hamming_Scrambler(dist=10)

#wt=Weight.Hebbian([person,woman,man,camera,tv])


wt=Weight.Hebbian([person,woman,man,camera,tv])
N=20
person.plotter(N)
person.Hamming_Scrambler(dist=20)
person.plotter(N)
changes=person.Async_Update(wt)
print(changes)
person.plotter(N)

woman.plotter(N)
woman.Hamming_Scrambler(dist=20)
woman.plotter(N)
changes=woman.Async_Update(wt)
print(changes)
woman.plotter(N)

man.plotter(N)
man.Hamming_Scrambler(dist=20)
man.plotter(N)
changes=man.Async_Update(wt)
print(changes)
man.plotter(N)

camera.plotter(N)
camera.Hamming_Scrambler(dist=20)
camera.plotter(N)
changes=camera.Async_Update(wt)
print(changes)
camera.plotter(N)

tv.plotter(N)
tv.Hamming_Scrambler(dist=20)
tv.plotter(N)
changes=tv.Async_Update(wt)
print(changes)
tv.plotter(N)


wt=Weight.Hebbian([person,woman,man,camera,tv])
print(wt.weight_matrix)

person.plotter(10)


changes=person.Async_Update(wt)
print(changes)
person.plotter(10)
woman.plotter(10)
man.plotter(10)

print(Memory_State.randomized(10).neuron_states)