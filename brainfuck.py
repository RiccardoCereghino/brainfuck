#!/usr/bin/env python
class Brainfuck:
    def __init__(self, code, input): 
        self.instructions = {}
        self.code = code
        self.input = input
        self.data = []
        self.data_pointer = 0

    def execute_instruction(self, instruction):
        failed = False
        if instruction == '>':
            failed = self.dp_incr()
        if instruction == '<':
            failed = self.dp_decr()
        if instruction == '+':
            failed = self.incr()
        if instruction == '-':
            failed = self.decr()
        if instruction == '.':
            failed = self.out()
        if instruction == ',':
            failed = self.inp()
        if instruction == '[':
            failed = self.jf()
        if instruction == ']':
            failed = self.jb()
        return failed
    
    def dp_incr(self):
        print(">")
        return True

    def dp_decr(self):
        print("<")
        return True

    def incr(self):
        print("+")
        return True

    def decr(self):
        print("-")
        return True

    def out(self):
        print(".")
        return True

    def inp(self):
        print(",")
        return True

    def jf(self):
        print("[")
        return True

    def jb(self):
        print("]")
        return True

    def get_instruction(self):
        instruction = self.code[0]
        self.code = self.code[1:]
        return instruction

    def execute(self):
        print("Fucked")
        while len(self.code) > 0:
            instruction = self.get_instruction()
            if not self.execute_instruction(instruction):
                break


def brain_luck(code, input):
    b = Brainfuck(code, input)

    return b.execute()

brain_luck(',+[-.,+]', 'Codewars' + chr(255))
