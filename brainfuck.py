#!/usr/bin/env python
class Brainfuck:
    def __init__(self, code, input): 
        self.instructions = {}
        self.code = code
        self.input = input

    def init_instructions(self): 
        self.instructions = {
            '>' : self.dp_incr(),
            '<' : self.dp_decr(),
            '+' : self.incr(),
            '-' : self.decr(),
            '.' : self.out(),
            ',' : self.inp(),
            '[' : self.jf(),
            ']' : self.jb(),
            }
    
    def dp_incr(self):
        print(">")

    def dp_decr(self):
        print("<")

    def incr(self):
        print("+")

    def decr(self):
        print("-")

    def out(self):
        print(".")

    def inp(self):
        print(",")

    def jf(self):
        print("[")

    def jb(self):
        print("]")

    def get_instruction():
        instruction = self.code[0]
        self.code = self.code[1:]
        return instruction

    def execute(self):
        print("Fucked")
        self.init_instructions()
        while len(self.code) > 0:
            instruction = get_instruction()
            self.instructions[instruction]()


def brain_luck(code, input):
    b = Brainfuck(code, input)

    return b.execute()

brain_luck(',+[-.,+]', 'Codewars' + chr(255))
