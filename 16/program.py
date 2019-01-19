import sys

reg = {}

# Addition:
def addr(A, B, C):
    """ (add register) stores into register C the result of adding register A and register B."""
    reg[C] = reg[A] + reg[B]
def addi(A, B, C):
    """ (add immediate) stores into register C the result of adding register A and value B."""
    reg[C] = reg[A] + B

# Multiplication:
def mulr(A, B, C):
    """  (multiply register) stores into register C the result of multiplying register A and register B."""
    reg[C] = reg[A] * reg[B]
def muli(A, B, C):
    """  (multiply immediate) stores into register C the result of multiplying register A and value B."""
    reg[C] = reg[A] * B

# Bitwise AND:
def banr(A, B, C):
    """  (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B."""
    reg[C] = reg[A] & reg[B]
def bani(A, B, C):
    """  (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B."""
    reg[C] = reg[A] & B

# Bitwise OR:
def borr(A, B, C):
    """  (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B."""
    reg[C] = reg[A] | reg[B]
def bori(A, B, C):
    """  (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B."""
    reg[C] = reg[A] | B

# Assignment:
def setr(A, B, C):
    """  (set register) copies the contents of register A into register C. (Input B is ignored.)"""
    reg[C] = reg[A]
def seti(A, B, C):
    """  (set immediate) stores value A into register C. (Input B is ignored.)"""
    reg[C] = A

# Greater-than testing:
def gtir(A, B, C):
    """  (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0."""
    if A > reg[B]:
        reg[C] = 1
    else:
        reg[C] = 0
def gtri(A, B, C):
    """  (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0."""
    if reg[A] > B:
        reg[C] = 1
    else:
        reg[C] = 0
def gtrr(A, B, C):
    """  (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0."""
    if reg[A] > reg[B]:
        reg[C] = 1
    else:
        reg[C] = 0

# Equality testing:
def eqir(A, B, C):
    """  (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0."""
    if A == reg[B]:
        reg[C] = 1
    else:
        reg[C] = 0
def eqri(A, B, C):
    """  (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0."""
    if reg[A] == B:
        reg[C] = 1
    else:
        reg[C] = 0
def eqrr(A, B, C):
    """  (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0."""
    if reg[A] == reg[B]:
        reg[C] = 1
    else:
        reg[C] = 0

def tests():

    reg[0] = 3
    reg[1] = 7
    reg[2] = 0
    reg[3] = 0

    addr(0, 1, 2)
    assert reg[2] == 10

    addi(0, 7, 2)
    assert reg[2] == 10

tests()

instructions = [
    addr,
    addi,
    mulr,
    muli,
    banr,
    bani,
    borr,
    bori,
    setr,
    seti,
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr,
]

f = open("input_1.txt", "r")
lines = f.readlines()
f.close()

class Example:
    before = []
    data = []
    after = []

examples = []

example = Example()

# Before: [2, 3, 2, 2]
# 0 3 3 0
# After:  [0, 3, 2, 2]

for line in lines:
    if "Before: " in line:
        example.before = list(map(int, (line.strip("Before: [").strip("]\n").split(", "))))
    elif "After: " in line:
        example.after = list(map(int, (line.strip("After:  [").strip("]\n").split(", "))))
        examples.append(example)
        example = Example()
    elif line.strip() != "":
        example.data = list(map(int, (line.strip().split(" "))))

possible_ops = {}

behaves_like_three = 0

for example in examples:

    possible_for_this = []

    for instr_i, instruction in enumerate(instructions):
        for i in range(4):
            reg[i] = example.before[i]
        instruction(example.data[1], example.data[2], example.data[3])
        is_possible = True
        for i in range(4):
            if reg[i] != example.after[i]:
                is_possible = False
        if is_possible:
            possible_for_this.append(instr_i)

    if len(possible_for_this) > 2:
        behaves_like_three += 1

    opcode = example.data[0]

    if opcode in possible_ops:
        previous = possible_ops[opcode]
        new_possible_for_this = []
        for possible in possible_for_this:
            if possible in previous:
                new_possible_for_this.append(possible)
        possible_for_this = new_possible_for_this

    possible_ops[opcode] = possible_for_this

print(behaves_like_three)
print(len(examples))
print(possible_ops)
