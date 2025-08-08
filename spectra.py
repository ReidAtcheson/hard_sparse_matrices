import matrices
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import scipy.sparse.linalg as spla
import numpy as np
import scipy.linalg as la

m=1024
A=matrices.random_d_regular_expander(m,5)

plt.hist(la.eigvalsh(A.toarray()))
plt.savefig("eigdist.svg")
