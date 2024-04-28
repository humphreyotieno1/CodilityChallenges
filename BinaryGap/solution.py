# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Convert the integer to a binary string
    binary_string = bin(N)[2:]

    # initializing variables
    maxGap = 0
    currentGap = 0

    # iterate the binary string
    isInGap = False
    for bit in binary_string:
        if bit == '0':
            if not isInGap:
                isInGap = True
                currentGap = 0
            currentGap += 1
        else:  # when bit is 1
            if isInGap:
                isInGap = False
                maxGap = max(maxGap, currentGap)

    return maxGap
