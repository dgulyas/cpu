import sys

# is the number being stored in the register from the ALU or
# a literal? These values come from the MUX above the ROM
alu = 1
literal = 0

# These map the instruction names to the ALU operation number
aluOps = { # refer to language spec for definitions
	'add': 0,
	'minus': 1,
	'negate': 2,
	'pt': 3,
	'and': 4,
	'or': 5,
	'invert': 6,
	'gt': 7,
	'e': 8,
	'lt': 9,
	'jgt': 10,
	'je': 11,
	'jlt': 12
}

# instructions that have the same arity are treated the same way
arityOne = {'negate', 'pt', 'invert'}
arityTwo = {'add', 'minus', 'and', 'or', 'gt', 'e', 'lt'}
jumpInsts = {'jgt', 'je', 'jlt'}

def DoTheThing():
	file = open(sys.argv[1])
	program = Program()
	
	for line in file:
		tokens = line.replace('\t', ' ').split(' ')
		inst = Inst()
		
		if tokens[0] == 'l': # l <literal> <destReg>
			inst.aluOrLiteral = literal
			inst.destReg = tokens[2]
			inst.literal = tokens[1]
			
		if tokens[0] in arityOne: # <inst> <opA> <destReg>
			inst.aluOrLiteral = alu
			inst.opAReg = tokens[1]
			inst.destReg = tokens[2]
			inst.aluFunct = aluOps[tokens[0]]

		if tokens[0] in arityTwo: # <inst> <opA> <opB> <destReg>
			inst.aluOrLiteral = alu
			inst.opAReg = tokens[1]
			inst.opBReg = tokens[2]
			inst.destReg = tokens[3]
			inst.aluFunct = aluOps[tokens[0]]
			
		if tokens[0] in jumpInsts: # <inst> <opA> <opB> <opC> <destReg>
			inst.aluOrLiteral = alu
			inst.opAReg = tokens[1]
			inst.opBReg = tokens[2]
			inst.opCReg = tokens[3]
			inst.destReg = tokens[4]
			inst.aluFunct = aluOps[tokens[0]]
			
		program.addLine(inst.getLine())
		
	program.printProgram()

class Inst:
	def __init__(self):
		self.aluOrLiteral = 0
		self.destReg = 0
		self.literal = 0
		self.opAReg = 0
		self.opBReg = 0
		self.opCReg = 0
		self.aluFunct = 0
		
	def getLine(self):
		bin = 	intToPaddedBinString(self.aluFunct, 4) + \
				intToPaddedBinString(self.opCReg, 3) + \
				intToPaddedBinString(self.opBReg, 3) + \
				intToPaddedBinString(self.opAReg, 3) + \
				intToPaddedBinString(self.literal, 8) + \
				intToPaddedBinString(self.destReg, 3) + \
				intToPaddedBinString(self.aluOrLiteral, 1)
		
		return hex(int(bin, 2))[2:]
		
		
def intToPaddedBinString(intNum, width):
	return bin(int(intNum))[2:].zfill(width)

		
class Program:
	def __init__(self):
		self.data = 'v2.0 raw\n'
		
	def addLine(self, line):
		self.data += line
		self.data += '\n'
		
	def printProgram(self):
		print(self.data)

if __name__ == "__main__":
	DoTheThing()