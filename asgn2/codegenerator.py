NumRegister = 7
RegDescriptor = ['' for x in range(NumRegister)]
# print RegDescriptor
variables = []
for i in range(NumInstr):
    variables.append(Instr3AC[i].input1)
    variables.append(Instr3AC[i].input2)
    variables.append(Instr3AC[i].output)

variables = set(variables)
AddDescriptor = {}
for i in variables:
    AddDescriptor[i] = ['memory']

def getreg(instrNo, symTableNo):
    if Instr3AC[i].instrType in ['Arithmetic']:
        y = Instr3AC[i].input1
        if (('register' in AddDescriptor[y]) and (symtables[symTableNo][y] == DEAD):
                for Regno in range(NumRegister):
                    if y == RegDescriptor[Regno]:
                        return Regno

        for Regno in range(NumRegister):
            if(RegDescriptor[Regno] == ''):
                return Regno

        x = Instr3AC[i].output
        if( symtables[symTableNo][x] == LIVE):
            farthestNextUse = 0
            for Var in symtables[symTableNo]:
                if (symtables[symTableNo][Var][2] > farthestNextUse):
                    farthestVar = Var
                    farthestNextUse = symtables[symTableNo][Var][2]
            for Regno in range(NumRegister):
                if farthestVar == RegDescriptor[Regno]:
                    break
            print 'Mov t%d %s'%Regno,%farthestVar
            AddDescriptor[farthestVar] = ['memory']
            return Regno

        return x

#CODE GENERATION ALGORITHM
def code_gen(initial,final):
    for i in range(initial,final+1):
        if Instr3AC[i].instrType in ['Arithmetic']:
            L = getreg(i,i-initial+1)