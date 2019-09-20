#!/usr/bin/env python
class Brainfuck:
    def __init__(self, code, input): 
        self.options = {}
        self.code = code
        self.input = input

    def options(): 
        self.options = {
            '>' : dp_incr(),
            '<' : dp_decr(),
            '+' : incr(),
            '-' : decr(),
            '.' : out(),
            ',' : inp(),
            '[' : jf(),
            ']' : jb(),
            }
    
    def dp_incr():
        print(">")

    def dp_decr():
        print("<")

    def incr():
        print("+")

    def decr():
        print("-")

    def out():
        print(".")

    def inp():
        print(",")

    def jf():
        print("[")

    def jb():
        print("]")

    def get_instruction():
        instruction = self.code[0]
        self.code = self.code[1:]
        return instruction

    def execute(self):
        print("Fucked")
        while len(self.code) > 0
            instruction = get_instruction()


def brain_luck(code, input):
    b = Brainfuck(code, input)

    return b.execute()

brain_luck(',+[-.,+]', 'Codewars' + chr(255))
