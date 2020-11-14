'''Code by Colter
'''
import argparse
import os
import sys

def makeFolders():
    newFileDirectory = os.path.dirname(os.path.realpath(__file__))
    for i in range(len(foldersToMake)):

        newFileDirectory = os.path.join(newFileDirectory, foldersToMake[i] + "\\")
        try:
            os.mkdir(newFileDirectory)
        except:
            pass
        print(newFileDirectory)
    return newFileDirectory

parser = argparse.ArgumentParser(
    description=
    "generates the template files for competing in coding contests,\
     specifically google code jam")
group = parser.add_mutually_exclusive_group()
parser.add_argument("-c", "--codeForcesNum", default=0)
parser.add_argument("-p", "--problemCount", default=4)
parser.add_argument("folderName",nargs='*', default="noNameGiven")

args = parser.parse_args()

# print(args.codeForcesNum)
# sys.exit(0)
if not args.codeForcesNum:
    foldersToMake = args.folderName.split("\\")
    newFileDirectory = makeFolders(foldersToMake)
    #remove extra \ 
    os.chdir(newFileDirectory[0:-1])
else:
    roundNum = "Round" + args.codeForcesNum
    print("making codeforces", roundNum)
    os.chdir("CodeForces")
    os.mkdir(roundNum)
    os.chdir(roundNum)


template = '''cases = int(input())
for t in range(cases):
    
    
    
    print("Case #", t+1, ": ",end="", sep="")
'''

for i in range(1, int(args.problemCount)+1):
    with open("problem" + str(i) + ".py", 'w') as f:
        f.write(template)
    with open("input"+str(i)+".txt", 'w') as f:
        pass

