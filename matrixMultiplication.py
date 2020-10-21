r1 = int(input("Enter No of rows of 1st Matrix: "))
c1 = int(input("Enter No of columns of 1st Matrix: "))

r2 = int(input("Enter No of rows of 2nd Matrix: "))
c2 = int(input("Enter No of columns of 2nd Matrix: "))

# for matrix multiplication to be possible no of columns in matrix 1 = no of rows in matrix 2
if c1 == r2:
    mat1 = []
    mat2 = []
    result = []

    print("\nEnter The Values in the matrix 1: ")
    for i in range (r1):
        g = []
        for j in range(c1):
            g.append(int(input()))
        mat1.append(g)

    for i in range(r1):
        for j in range(c1):
            print(mat1[i][j], end=" ")
        print()

    print("\nEnter The Values in the matrix 2: ")
    for i in range(r1):
        g = []
        for j in range(c1):
            g.append(int(input()))
        mat2.append(g)

    for i in range(r2):
        for j in range(c2):
            print(mat2[i][j], end=" ")
        print()

    #Result
    for r in range(r1):
        u = []
        for s in range(c2):
            u.append(int(0))
        result.append(u)
    for r in range(r1):
        for s in range(c2):
            result[r][s]
    print("\nResult is: \n")
    # iterate through rows of r1
    for x in range(len(mat1)):
        # iterate through columns of c2
        for y in range(len(mat2[0])):
            # iterate through rows of r2
            for z in range(len(mat2)):
                result[x][y] += mat1[x][z] * mat2[z][y]
    for r in result:
        print(r)
else:
    print("\nNot possible")