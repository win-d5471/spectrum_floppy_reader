import copy

f=open("AMPED.SPE","rb")

data=f.read()
print(695%128)
for i in range(len(data)):
    if data[i]==1:
        print(data[i], i,i%128)



DD=[0]*1024

X=copy.deepcopy(data[0:128])
Y=copy.deepcopy(data[128:256])

for L in range(4):
    for N in range(128):
        M=256*L+N
        DD[M]=X[N]
        M=M+128
        # print("M",M,"N",N)
        DD[M]=Y[N]

print(data[695],"data[695]")
print(data[704])
print(data[705])
print(data[706])
print(data[707])
print(data[708])
print(data[709])
print(data[710])
print(data[711])



