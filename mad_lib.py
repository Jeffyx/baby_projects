def countLibs(file_name):
    words = {
        "A":0,
        "N":0,
        "V":0
    }
    try:
        with open(file_name, 'r') as mad_lib:
            for line in mad_lib:
                for x in range(0,len(line)):
                    if line[x] == "*" and line[x+2] == "*":
                        if line[x+1] in words:
                            words[line[x+1]] += 1
    except FileNotFoundError:
        print ("File name {} does not exists".format(file_name))
    return(words["A"], words["V"], words["N"])

def askLibs(adjectiveCount, verbCount, nounCount):
    #num = []
#for i in range(1, 4):
#    num.append(input("enter your number"))
#print(num)
    adj = []
    for a in range(0,adjectiveCount):
        adj.append(input("Please enter an Adjective: "))

    ver = []
    for v in range(0,verbCount):
        ver.append(input("Please enter an Verb: "))

    nou = []
    for n in range(0,nounCount):
        nou.append(input("Please enter an Noun: "))

    return(adj, ver, nou)

def printFunny(file_name, adjectiveList, verbList, nounList):
    with open(file_name, 'r') as mad_lib:
    #only to print, eventually delete return statement
    return()

file_name = input("give a file name: ")
counts = countLibs(file_name)
print (counts)

words = askLibs(counts[0], counts[1], counts[2])

printFunny(file_name, words[0], words[1], words[2])