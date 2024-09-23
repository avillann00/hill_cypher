"""
*============================================================================
| Assignment: pa01 - Encrypting a plaintext file using the Hill cipher
|
| Author: Your name here
| Language: c, c++, Java, go, python
| To Compile: javac pa01.java
| gcc -o pa01 pa01.c
| g++ -o pa01 pa01.cpp
| go build pa01.go
| rustc pa01.rs
| To Execute: java -> java pa01 kX.txt pX.txt
| or c++ -> ./pa01 kX.txt pX.txt
| or c -> ./pa01 kX.txt pX.txt
| or go -> ./pa01 kX.txt pX.txt
| or rust -> ./pa01 kX.txt pX.txt
| or python -> python3 pa01.py kX.txt pX.txt
| where kX.txt is the keytext file
| and pX.txt is plaintext file
| Note:
| All input files are simple 8 bit ASCII input
| All execute commands above have been tested on Eustis
|
| Class: <class> - Security in Computing - Summer 2024
| Instructor: <professor>
| Due Date: per assignment
+===========================================================================*/
"""
# import required modules
import sys
import numpy as np

# helper function to convert a number to a letter
def to_letter(num):
    return chr(num + ord('a'))

# helper function to convert a letter to a number
def to_number(letter):
    return (ord(letter) - ord('a'))

# main encryption function
def encrypt():
    # get the command line arguments
    keyfile = sys.argv[1]
    plaintextfile = sys.argv[2]

    # extract the key
    with open(keyfile, 'r') as kf:
        key_content = kf.read().strip().split()
        n = int(key_content[0])
        key_list = [int(k) for k in key_content[1:] if k.isdigit()]    

    # convert the key into a matrix
    if len(key_list) != n * n:
        print('length wrong')
    key_matrix = np.array(key_list).reshape(n, n)

    # extract the plaintext
    with open(plaintextfile, 'r') as pf:
        plaintext = ''.join(line.strip() for line in pf)

    # process the plaintext by converting it to numbers
    cleaned = []
    print_output = ''
    for c in plaintext:
        if c.isalpha():
            print_output += c.lower()
            cleaned.append(to_number(c.lower()))

    # pad if necessary 
    if len(cleaned) % n != 0:
        missing = n - (len(cleaned) % n)
        cleaned.extend([23] * missing)
        print_output += ('x' * missing)

    # convert cleaned plaintext to a numpy matrix and perform matrix multiplication
    plain_matrix = np.array(cleaned).reshape(-1, n).T
    result = np.dot(key_matrix, plain_matrix) % 26
    result = result.T.flatten().astype(int)

    # turn the numbers back into letters
    encrypted = ''
    for c in result:
        encrypted += to_letter(int(c))

    # print the key matrix
    print('Key matrix:')
    for row in key_matrix:
        print('   ' + '   '.join(f'{num:>4}' for num in row))
    print()

    # print the plaintext
    print('Plaintext:')
    for i in range(len(print_output)):
        print(print_output[i], end='')
        if (i + 1) % 80 == 0:
            print()
    print()
    print()

    # print the ciphertext
    print('Ciphertext:')
    for i in range(len(encrypted)):
        print(encrypted[i], end='')
        if (i + 1) % 80 == 0:
            print()
    print()

# execute encrypt if this file is called
if __name__ == '__main__':
    encrypt()

"""
/*=============================================================================
| I <name> <nid> affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+=============================================================================*/
"""
