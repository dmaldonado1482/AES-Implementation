## Put your names here in this comment.

## HINTS:
## You can specify an integer using hexadecimal in Python in the same
## way as in Java, C, C++.  Specifically, start with 0x.  For example 0x2A
## is 42 in hexadecimal.
##
## The bit wise operators are mostly the same as Java, C, C++.  Specifically,
## x & y computes the result of anding the bots of x with the bits of y.
## Similarly, | is bitwise or, ^ is bitwise XOR.
## x << k shifts the bits of x to the left k places.
## x >> k is likewise a right-shift with sign extension.
## Sign extension means that if the integer is positive, the new bits on the right
## are 0 and 1 for negatives.
##
## BEWARE: Python does not have an unsigned right-shift.  I don't think this will be
## an issue for you.  The reason is that Python uses arbitrary length integers
## rather than fixed-length like the int, long, byte, and short types in Java.
## So a negative integer value can be thought of in Python to have an infinite
## number of 1-bits on the left.  This shouldn't be an issue with this assignment
## in Python.  Since because Python has no bit length limit on integer values,
## any values you manipulate in this assignment will be positive (unless you really
## do something weird). 

sbox = [ 0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79, 0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16 ]

def byte_substitution(state) :
    """Computes the byte substitution step of AES.

    Keyword arguments:
    state - The current state matrix as a 2D list (list of lists).
    This function modifies
    this matrix by replacing each element with the corresponding
    output of the AES Sbox.
    """
    ## HINT: I'd recommend hardcoding a Python list with the AES Sbox
    ## see the hints in the equivalent of this in the Java version for how to do this.



    # sub_matrix = []
    # if(isinstance(state[0], list)):
    #     for i in range(len(state)):
    #         for j in range(len(state[i])):  #potential errors for key_expansion lookup
    #             sub_matrix[i][j].append(hex(sbox[int(state[i][j], 16)]))
    
    # if(isinstance(state[0], str)):
    #     for i in range(len(state)):
    #         sub_matrix[i].append(hex(sbox[int(state[i], 16)]))

    for i in range(len(state)):
        for j in range(len(state[i])):  #potential errors for key_expansion lookup
            state[i][j] = hex(sbox[int(state[i][j], 16)])

    for i in state:
        print(i)

    return state



def shift_rows(state) :
    """Computes the shift rows step of AES.

    Keyword arguments:
    state - The current state matrix as a 2D list (list of lists).
    This function modifies
    this matrix according to the shift rows step of AES.
    """
    
    pass



def mix_columns(state) :
    """Computes the mix columns step of AES.

    Keyword arguments:
    state - The current state matrix as a 2D list (list of lists).
    This function modifies
    this matrix according to the mix columns step of AES.
    """

    ## See the hints in the Java version.  Some of those hints apply directly here as well.
    ## since the bitwise operators are the same.
    
    pass



def generate_key_matrix_from_key(keyAsInteger) :
    """Generates and returns a key matrix with 4 rows and 4 columns
    from the key passed as parameter.  Use a list of lists for the matrix.
    The bytes of the key get filled down the columns.

    Keyword arguments:
    keyAsInteger - An integer value with the key.  Assumed small enough to
    require no more than 128 bits.
    """
    x = keyAsInteger.replace(" ", "")
    y = [x[i : i+2] for i in range(0, len(x), 2)]

    matrix = [[0] * 4 for i in range(4)]
    counter = 0
    for i in range(4):
        for j in range(4):
            matrix[j][i] = y[counter]
            counter += 1
    
    #Testing XOR
    # hex1 = int(matrix[0][0], 16)
    # hex2 = int(matrix[0][1], 16)
    # print(hex(hex1 ^ hex2).replace("0x", ""))
    # for i in matrix:
    #     print(i)

    # bytes(hex(int(y[counter], base=16)).encode("utf-8"))

    return matrix



def key_expansion(keyMatrix) :
    """Generates and returns the expanded key matrix as a list of lists
    with 4 rows and 44 columns.  First 4 columns are the columns of keyMatrix.
    The rest are according to the AES key expansion rules.

    Keyword arguments:
    keyMatrix - list of lists with 4 rows and 4 columns.
    """
    counter = 4
    while(counter <= 44):
        # For words that are divisible by 4
        if(counter % 4 == 0):
            word = []
            word_counter = 0
            while(word_counter < 4):
                word.append(keyMatrix[word_counter][counter-1])
                word_counter += 1
            
            #Shifts the previous word to prepare for s-box
            word[0], word[1], word[2], word[3] = sbox[int(word[1], 16)], sbox[int(word[2], 16)], sbox[int(word[3], 16)], sbox[int(word[0], 16)]
            for i in range(len(word)):
                word[i] = hex(word[i])




        
        keyMatrix[0].append(hex(int(keyMatrix[0][counter-4], 16) ^ int(keyMatrix[0][counter-1], 16)).replace("0x", ""))
        keyMatrix[1].append(hex(int(keyMatrix[1][counter-4], 16) ^ int(keyMatrix[1][counter-1], 16)).replace("0x", ""))
        keyMatrix[2].append(hex(int(keyMatrix[2][counter-4], 16) ^ int(keyMatrix[2][counter-1], 16)).replace("0x", ""))
        keyMatrix[3].append(hex(int(keyMatrix[3][counter-4], 16) ^ int(keyMatrix[3][counter-1], 16)).replace("0x", ""))

        counter += 1

    for i in range(4):
        print(keyMatrix[i][0], keyMatrix[i][1], keyMatrix[i][2], keyMatrix[i][3])
    

    pass



if __name__ == "__main__" :
    ## Write some code here to test your functions.
    ## You might consider using homework problems as a source of test
    ## cases since you can compare output to what you worked through by hand.

    ## You can produce output in hexadecimal with the following:
    ## Suppose value0, value1, value2, etc are integer values and you want to
    ## output them separated by spaces on one line.  Do the following:
    ## print("{0:02x} {1:02x} {2:02x} {3:02x}".format(value0, value1, value2, value3))
    ## In the string, the {0:02x} means that you want to format the 0th parameter
    ## (number before the colon) of format using 2 digits padding with a 0 if necessary
    ## (this is what the 02 means) and in hexadecimal (the x).

    key = "1a005012be1000c 00120403407100001"
    key_matrix = generate_key_matrix_from_key(key)
    key_expansion(key_matrix)
    
    #Byte_Substitution Test
    # key = "08 32 64 46 10 a1 00 e1 35 74 25 35 a6 40 10 13"
    # key_matrix = generate_key_matrix_from_key(key)
    # sbox_matrix = byte_substitution(key_matrix)
    pass
    
