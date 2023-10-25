

def printMat(a, r, c): 
	for i in range(r): 
		for j in range(c): 
			print(a[i][j], end = " ") 
		print() 
	print() 


def printt(display, matrix, start_row, start_column, end_row,end_column): 
	print(display + " =>\n")
	for i in range(start_row, end_row+1): 
		for j in range(start_column, end_column+1): 
			print(matrix[i][j], end=" ") 
		print() 
	print() 

#Function to add two matrices
def add_matrix(matrix_A, matrix_B, matrix_C, split_index): 
	for i in range(split_index): 
		for j in range(split_index): 
			matrix_C[i][j] = matrix_A[i][j] + matrix_B[i][j] 

#Function to initialize matrix with zeros
def initWithZeros(a, r, c): 
	for i in range(r): 
		for j in range(c): 
			a[i][j] = 0

#Function to multiply two matrices
def multiply_matrix(matrix_A, matrix_B): 
	col_1 = len(matrix_A[0]) 
	row_1 = len(matrix_A) 
	col_2 = len(matrix_B[0]) 
	row_2 = len(matrix_B) 

	if (col_1 != row_2): 
		print("\nError: The number of columns in Matrix A must be equal to the number of rows in Matrix B\n") 
		return 0

	result_matrix_row = [0] * col_2
	result_matrix = [[0 for x in range(col_2)] for y in range(row_1)] 

	if (col_1 == 1): 
		result_matrix[0][0] = matrix_A[0][0] * matrix_B[0][0] 

	else: 
		split_index = col_1 // 2

		row_vector = [0] * split_index 
		result_matrix_00 = [[0 for x in range(split_index)] for y in range(split_index)] 
		result_matrix_01 = [[0 for x in range(split_index)] for y in range(split_index)] 
		result_matrix_10 = [[0 for x in range(split_index)] for y in range(split_index)] 
		result_matrix_11 = [[0 for x in range(split_index)] for y in range(split_index)] 
		a00 = [[0 for x in range(split_index)] for y in range(split_index)] 
		a01 = [[0 for x in range(split_index)] for y in range(split_index)] 
		a10 = [[0 for x in range(split_index)] for y in range(split_index)] 
		a11 = [[0 for x in range(split_index)] for y in range(split_index)] 
		b00 = [[0 for x in range(split_index)] for y in range(split_index)] 
		b01 = [[0 for x in range(split_index)] for y in range(split_index)] 
		b10 = [[0 for x in range(split_index)] for y in range(split_index)] 
		b11 = [[0 for x in range(split_index)] for y in range(split_index)] 

		for i in range(split_index): 
			for j in range(split_index): 
				a00[i][j] = matrix_A[i][j] 
				a01[i][j] = matrix_A[i][j + split_index] 
				a10[i][j] = matrix_A[split_index + i][j] 
				a11[i][j] = matrix_A[i + split_index][j + split_index] 
				b00[i][j] = matrix_B[i][j] 
				b01[i][j] = matrix_B[i][j + split_index] 
				b10[i][j] = matrix_B[split_index + i][j] 
				b11[i][j] = matrix_B[i + split_index][j + split_index] 

		add_matrix(multiply_matrix(a00, b00),multiply_matrix(a01, b10),result_matrix_00, split_index)
		add_matrix(multiply_matrix(a00, b01),multiply_matrix(a01, b11),result_matrix_01, split_index)
		add_matrix(multiply_matrix(a10, b00),multiply_matrix(a11, b10),result_matrix_10, split_index)
		add_matrix(multiply_matrix(a10, b01),multiply_matrix(a11, b11),result_matrix_11, split_index)

		for i in range(split_index): 
			for j in range(split_index): 
				result_matrix[i][j] = result_matrix_00[i][j] 
				result_matrix[i][j + split_index] = result_matrix_01[i][j] 
				result_matrix[split_index + i][j] = result_matrix_10[i][j] 
				result_matrix[i + split_index][j + split_index] = result_matrix_11[i][j] 

	return result_matrix 



# Function to take input for a matrix
def inputMatrix(matrix, rows, cols):
    print("\nEnter the elements of the matrix:")
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("\nInvalid input. Please provide", cols, "elements for each row.")
            return False
        matrix.append(row)
    return True

# Function to take input for matrix dimensions
def inputDimensions():
    sz = int(input("\n Enter the size of Matrix: "))
    rows = sz
    cols = sz
    return rows, cols

def standardMatrixMultiply(matrix_A, matrix_B):
    rows_A = len(matrix_A)
    cols_A = len(matrix_A[0])
    rows_B = len(matrix_B)
    cols_B = len(matrix_B[0])

    if cols_A != rows_B:
        print("\nError: The number of columns in Matrix A must be equal to the number of rows in Matrix B")
        return None

    result_matrix = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result_matrix[i][j] += matrix_A[i][k] * matrix_B[k][j]

    return result_matrix

# Driver Code
print("\n Enter details for Matrix A:")
rows_A, cols_A = inputDimensions()
matrix_A = []
if not inputMatrix(matrix_A, rows_A, cols_A):
    exit(1)

print("\n Enter details for Matrix B:")
rows_B, cols_B = inputDimensions()
matrix_B = []
if not inputMatrix(matrix_B, rows_B, cols_B):
    exit(1)

result_matrix_standard = standardMatrixMultiply(matrix_A, matrix_B)
result_matrix_strassen = multiply_matrix(matrix_A, matrix_B)

print("\nMatrix A:")
printMat(matrix_A, rows_A, cols_A)

print("Matrix B:")
printMat(matrix_B, rows_B, cols_B)

print("Result Matrix (Standard Method):")
printMat(result_matrix_standard, rows_A, cols_B)

print("Result Matrix (Strassen Algorithm):")
printMat(result_matrix_strassen, rows_A, cols_B)