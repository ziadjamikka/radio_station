
def main():
    close_no = input("what's the type of graph:  ")
    
    if close_no == "cycle":
        n_edges = int(input("Enter the number of edges: "))
        n_vertices = n_edges
    elif close_no == "path":
        n_edges = int(input("Enter the number of edges: "))
        n_vertices = n_edges - 1
    elif close_no == "triangular-snake":
        n = int(input("Enter Number Of Triangles: "))
        n_edges = 3 + 2 * (n - 1)
        n_vertices = n_edges

    A = [[0] * n_vertices for _ in range(n_vertices)]

    if close_no == "triangular-snake":
        for i in range(n_vertices):
            row = []
            for j in range(n_vertices):
                if i == j:
                    row.append(0)
                elif i == j + 1 or i == j - 1:
                    row.append(1)
                elif (i + 1) % 2 == 1 and (i == j + 2 or i == j - 2):
                    row.append(1)
                elif (i + 1) % 2 == 1 and (j == i + 2 or j == i - 2):
                    row.append(1)
                else:
                    row.append(0)
            A[i] = row
    else:
        for i in range(n_vertices):
            for j in range(n_vertices):
                if j == i - 1 or j == i + 1:
                    A[i][j] = 1

        if close_no == "yes":
            A[0][-1] = 1
            A[-1][0] = 1

        for i in range(1, n_vertices - 1):
            A[i][i - 1] = 1
            A[i][i + 1] = 1

    print("\nAdjacency Matrix:")
    for row in A:
        print(row)

    def calculate_distance(vertices, i, j):
        distance = 0
        while i != j:
            distance += 1
            i = (i + 1) % vertices
        return distance

    max_distance = 0
    for i in range(n_vertices):
        for j in range(n_vertices):
            if A[i][j] == 1:
                distance = calculate_distance(n_vertices, i, j)
                if distance > max_distance:
                    max_distance = distance

    diameter = max_distance + 1
    print("Diameter of the shape + 1:", diameter)

    distance_matrix = [[0] * n_vertices for _ in range(n_vertices)]

    for i in range(n_vertices):
        for j in range(n_vertices):
            if i != j:
                if A[i][j] == 1:
                    distance_matrix[i][j] = 1
                else:
                    if close_no == "yes" and (i == n_vertices - 1 and j == 0):
                        distance_matrix[i][j] = 1
                    else:
                        distance_matrix[i][j] = calculate_distance(n_vertices, i, j)
                print(f"Distance between {i} and {j}: {distance_matrix[i][j]}")

    print("\nDistance Matrix:")
    for row in distance_matrix:
        print(row)

    C0 = [[float('inf')] * n_vertices for _ in range(n_vertices)]

    for k in range(n_vertices):
        for i in range(n_vertices):
            for j in range(n_vertices):
                if i != j:
                    distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])

                    C0[i][j] = diameter - distance_matrix[i][j]

    print("\nc0 Matrix:")
    for row in C0:
        print(row)
    
    c0_matrix = [[float('inf')] * n_vertices for _ in range(n_vertices)]
    for i in range(n_vertices):
        for j in range(n_vertices):
            if i != j:
                distance_matrix[i][j] = diameter - calculate_distance(n_vertices, i, j)
                c0_matrix[i][j] = distance_matrix[i][j]

    print("\nc0 Matrix:")
    for row in c0_matrix:
        print(row)
    
    X = []

    mini = min(C0[0])
    X.append(mini)
    Index = C0[0].index(mini)
    R_Index = 0
    F_Index = [Index]

    for i in range(1, n_vertices):
        for j in range(n_vertices):
            C0[Index][j] += mini
            if C0[Index][j] > C0[R_Index][j]:
                C0[Index][j] = C0[Index][j]
            elif C0[R_Index][j] > C0[Index][j]:
                C0[Index][j] = C0[R_Index][j]
        print(f"C{i} = \n")
        for k in C0:
            print(k)
        print("\n")

        mini = min(C0[Index])
        X.append(mini)
        R_Index = Index
        Index = C0[Index].index(mini) 
        F_Index.append(Index)
    F_Index.remove(F_Index[-1])
    X.remove(X[-1])

    print(f"X{1} = {0}")
    for l, ver in enumerate(F_Index):
        print(f"X{ver+1} = {X[l]}")

    print(f"Radio Number Of {close_no} Graph For {n_vertices} Vertices -> X{F_Index[-1]+1} = {max(X)}")

if __name__ == "__main__":
    main()