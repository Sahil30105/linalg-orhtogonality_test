import numpy as np
def mat():
    rc=np.array(list(map(int,input("enter rows and columns :").split("x"))))
    a=np.array(list(map(int,input("enter the matrix a :").split(",")))).reshape(rc)
    b=np.array(list(map(int,input("enter the matrix b :").split(",")))).reshape(rc)
    r=[[0]*len(a)]*len(a)
    for i in range(len(a)):
        for j in range(len(b[0])):
                r[i][j]+=a[i][j]*b[i][j]
    x=sum(r[0])+sum(r[1])
    print("Value of <a,b> is ",x)
    if x==0:
        print("matrices are orthogonal")
    else:
        print("matrices are not orthogonal")
def vector():
    a=np.array(list(map(int,input("enter the vector a :").split(","))))
    b=np.array(list(map(int,input("enter the vector b :").split(","))))
    c=a@b
    print("Value of <a,b> is ",c)
    if c==0:
            print("vectors are orthogonal")
    else:
            print("vectors are not orthogonal")
if input("do you want to check matrix orthogonality or vector orthogonality?  ") == "matrix":
    mat()
else:
    vector()
