import matrices
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import scipy.sparse.linalg as spla
import numpy as np



def disp(A,name):
    m=A.shape[0]
    luA=spla.splu(A)
    plt.spy(A,markersize=1)
    nnzA=A.nnz
    nnzluA=luA.L.nnz+luA.U.nnz
    plt.title(f"nnz(A)={nnzA},nnz(lu(A))={nnzluA},ratio={nnzluA/(m*m)}")
    plt.savefig(f"{name}.svg")



m=12000
d=3
disp(matrices.random_d_regular_expander(m,d).tocsc(),"random_d_regular_expander")
disp(matrices.random_d_regular(m,d).tocsc(),"random_d_regular")

