import sys

# is the number being stored in the register from the ALU or
# the keyboard? These values come from the MUX above the ROM
keyboard = 1
alu = 0

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

#These map register names to the register's number
regNums = { # refer to language spec for definitions
	'$0': 0,
	'$1': 1,
	'$2': 2,
	'$3': 3,
	'$4': 4,
	'$5': 5,
	'$6': 6,
	'$7': 7,
	'$8': 8,
	'$9': 9,
	'$10': 10,
	'$11': 11,
	'$12': 12,
	'$ramAdd': 12,
	'$13': 13,
	'$ram': 13,
	'$14': 14,
	'$tty': 14,
	'$lit': 14,
	'$15': 15,
	'$pc': 15
}

# instructions that have the same arity are treated the same way
arityOne = {'negate', 'pt', 'invert'}
arityTwo = {'add', 'minus', 'and', 'or', 'gt', 'e', 'lt'}
jumpInsts = {'jgt', 'je', 'jlt'}

def DoTheThing():
	file = open(sys.argv[1])
	program = Program()
	
	for line in file:
		line = removeComments(line)
		tokens = line.split()
		inst = Inst()
		
		if tokens[0] == 'lk': # lk <destReg>
			inst.aluOrKeyboard = keyboard
			inst.destReg = regNums[tokens[1]]
			
		elif tokens[0] in arityOne: # <inst> <opA> <destReg> <optional literal>
			inst.aluOrKeyboard = alu
			inst.opAReg = regNums[tokens[1]]
			inst.destReg = regNums[tokens[2]]
			inst.aluFunct = aluOps[tokens[0]]
			if(len(tokens) == 4):
				inst.literal = tokens[3]

		elif tokens[0] in arityTwo: # <inst> <opA> <opB> <destReg> <optional literal>
			inst.aluOrKeyboard = alu
			inst.opAReg = regNums[tokens[1]]
			inst.opBReg = regNums[tokens[2]]
			inst.destReg = regNums[tokens[3]]
			inst.aluFunct = aluOps[tokens[0]]
			if(len(tokens) == 5):
				inst.literal = tokens[4]
			
		elif tokens[0] in jumpInsts: # <inst> <opA> <opB> <opC> <destReg> <optional literal>
			inst.aluOrKeyboard = alu
			inst.opAReg = regNums[tokens[1]]
			inst.opBReg = regNums[tokens[2]]
			inst.opCReg = regNums[tokens[3]]
			inst.destReg = regNums[tokens[4]]
			inst.aluFunct = aluOps[tokens[0]]
			if(len(tokens) == 6):
				inst.literal = tokens[5]
				
		else:
			print("No matching command found: " + line)
			
		program.addLine(inst.getLine())
	
	program.printProgram()

class Inst:
	def __init__(self):
		self.aluOrKeyboard = 0
		self.destReg = 0
		self.literal = 0
		self.opAReg = 0
		self.opBReg = 0
		self.opCReg = 0
		self.aluFunct = 0
		
	def getLine(self):
		bin = 	intToPaddedBinString(self.aluOrKeyboard, 1) + \
				intToPaddedBinString(self.aluFunct, 4) + \
				intToPaddedBinString(self.opAReg, 4) + \
				intToPaddedBinString(self.opBReg, 4) + \
				intToPaddedBinString(self.opCReg, 4) + \
				intToPaddedBinString(self.destReg, 4) + \
				intToPaddedBinString(self.literal, 8)
		
		return hex(int(bin, 2))[2:]
		
		
def intToPaddedBinString(intNum, width):
	return bin(int(intNum))[2:].zfill(width)

def removeComments(line):
	try:
		poundIndex = line.index('#')
		return line[:poundIndex]
	except:
		return line
		
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