# 1. Section with name
print('1. Homework 2 - Gaurav Makin\n')

import numpy as np

# 2. Create 3x5 matrix of random numbers
A = np.matrix(np.random.rand(3,5))
print("2.Matrix:\n", A)

# 3. Size and Length of matrix
print("\n3.Size:\t", np.size(A))
print("Length:\t", A.nbytes)

# 4. Resize matrix to size (3,4)
A = A[0:3,:4]
print("\n4. Slice:\n", A)

# 5. Transpose of A assigned to B
B = A.transpose()
print("\n5. Transposed matrix:\n", B)

# 6. Minimum in Column 1 of B
print("\n6. Minimum in Column 1: ", np.min(B,0,)[0,0])

# 7. Minimum and Maximim of A
print("\n7. Minimum Value is:\t", A.min())
print("Maximum Value is:\t", A.max())

# 8. Array of 4 random numbers
X = np.random.random(4)
print("\n8. Array of random numbers:\n", X)

# 9. Function for multiplication
def multiply(myarray, mymatrix):
    result = np.dot(myarray, mymatrix)
    return result

# 10. Multiplication of array with matrix
D = multiply(X, A.transpose())
print("\n10. Mutliplication Result:\n", D)

# 11. Complex number with absolute and real parts != 0 
Z = complex(np.random.rand(), np.random.rand())
print("\n11. Complex number is:\t", Z)

# 12. Print real and imaginary parts
print("\n12. Real part of complex number:\t", Z.real)
print("Imaginary part of complex number:\t", Z.imag)

# 13.  Multiply matrix with absolute value of complex number
C = np.absolute(Z) * D
print("\n13. Multiply D with Z absolute val %f:\n" % np.absolute(Z), C)

# 14. Matrix to string
B = str(B)
print("\n14. Matrix as string:\n", B)

# 15. Display name
print("\n\n15. \tGaurav Makin is done with HW2\n\n")
