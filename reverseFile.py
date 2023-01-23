from stacksQueues import Stack



# A function that reverses the lines of a file

def reverseFile(filename):
    S = Stack()

    infile = open(filename, 'r')
    for line in infile:
        S.push(line.rstrip())
    infile.close()

    outfile = open(filename, 'w')
    while not S.isEmpty():
        outfile.write(S.pop() + "\n")
    outfile.close()

