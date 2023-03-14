import numpy as np


def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    assert h % nrows == 0, f"{h} rows is not evenly divisible by {nrows}"
    assert w % ncols == 0, f"{w} cols is not evenly divisible by {ncols}"
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(h//nrows, -1, nrows, ncols))


def ptrace(arr, dims, tgt):
    """
    Returns the partial trace over target space
    Parameters:
    arr : the density matrix or ket-vector of systems A and B
    dims : dimensions of system A and system B. Should be the array of 2 integer numbers
    tgt : the space over which the arr will be traced
    Returns:
    ans - density matrix after making partial trace. 
    """
    arr = np.matrix(arr)
    assert len(np.shape(arr)) == 2, "the arr should be 2D array or 1D-vector"
    if np.shape(arr)[0] == 1: #Make the density matrix for given ket-vector
        arr = np.matmul(arr.getH(), arr)
    #return arr
    arr = np.asarray(arr)
    assert len(dims) == 2, "The dims should be the array of 2 integer numbers"
    dimA, dimB = dims
    if tgt == 0:
        ans = np.trace(blockshaped(arr, dimB, dimB), axis1 = 0, axis2 = 1)
    else:
        ans = np.trace(blockshaped(arr, dimB, dimB), axis1 = 2, axis2 = 3)
    return ans