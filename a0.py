# a0.py

# Starter code for assignment 0 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME: Julia Qianran Bi
# EMAIL: qianranb@uci.edu
# STUDENT ID: 16903084


def downward_diagonal_pattern(n):
    for i in range(n+1):
        # Print indentation
        for j in range(i):
            print('', end='')

        if i == 0:
            print('+-+')
            print('| |', end="\n")
        elif i == n:
            print("+-+")
        else:
            print('+-+-+')
            # Print the vertical bar on the next line with the same indentation
            for k in range(i):
                print('  ', end='')
            print('| |')
            for l in range(i):
                print('  ', end='')


n = int(input())

# Check if the input is within the valid range
if 0 < n <= 999:
    downward_diagonal_pattern(n)
else:
    print("Input must be a positive integer between 1 and 999.")

