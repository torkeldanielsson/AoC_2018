import sys
import math

reg = {}

for i in range(6):
    reg[i] = 0

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

instructions = {
    "addr":addr,
    "addi":addi,
    "mulr":mulr,
    "muli":muli,
    "banr":banr,
    "bani":bani,
    "borr":borr,
    "bori":bori,
    "setr":setr,
    "seti":seti,
    "gtir":gtir,
    "gtri":gtri,
    "gtrr":gtrr,
    "eqir":eqir,
    "eqri":eqri,
    "eqrr":eqrr,
}

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

class Command:
    instruction = 0
    A = 0
    B = 0
    C = 0

pp_r = 0

program = []

for line in lines:
    parts = line.split(" ")
    if "#ip" in line:
        pp_r = int(parts[1])
    if len(parts) == 4:
        command = Command()
        command.instruction = instructions[parts[0]]
        command.A = int(parts[1])
        command.B = int(parts[2])
        command.C = int(parts[3])
        program.append(command)

# for command in program:
#     print(command.instruction.__name__, command.A, command.B, command.C)

def get_regstr():
    global reg
    regstr = "["
    for i in range(5):
        regstr += str(reg[i]) + ", "
    regstr += str(reg[5]) + "]"
    return regstr

#reg[0] = 1

if False:
    while reg[pp_r] >= 0 and reg[pp_r] < len(program):
        c = program[reg[pp_r]]

        r0_pre = reg[0]

        c.instruction(c.A, c.B, c.C)
        
        # pre_regstr = get_regstr()
        # ip_bef = reg[pp_r]
        # c.instruction(c.A, c.B, c.C)
        # post_regstr = get_regstr()
        # print("ip=" + str(ip_bef), pre_regstr, c.instruction.__name__, c.A, c.B, c.C, post_regstr)
        reg[pp_r] += 1

        if reg[0] != r0_pre:
            print(get_regstr())

    print(get_regstr())

def equivalent_operation(num):
    res = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(res, int(num/i), i)
            res += int(num/i) + i
    return res

print(equivalent_operation(10551306))