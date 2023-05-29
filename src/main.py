#Author: Ritchie Yapp
#LCCL Coding Academy PY2
import sys
import rich
#TODO: it doesnt print if repeating words are on the same line

if len(sys.argv) == 1:
    print("Command line argument omitted, quitting")
    exit()
else:
    result = ""
    try:
        f = open(sys.argv[1])
        #2d array, each element is a list of words split with spaces and stripped of newlines
        read = [[word for word in line.strip().split(" ")] for line in f.readlines()]
        f.close()
    except FileNotFoundError:
        print(f"File {sys.argv[1]} not found, quitting")
        exit()

unique = ""
repeatingIndexes = {0: [0]}
for (lineNum, line) in enumerate(read):
    for (wordInd, word) in enumerate(line):
        if word == unique:
            try: 
                repeatingIndexes[lineNum].append(wordInd)
            except KeyError: 
                repeatingIndexes[lineNum] = [wordInd]
        else:
            if len(repeatingIndexes) != 1 and len(list(repeatingIndexes.values())[0]) != 1:
                print()
                for lineIndex in repeatingIndexes:
                    print(f"{lineIndex+1}: ", end=" ")
                    for (i, word) in enumerate(read[lineIndex]):
                        if i in repeatingIndexes[lineIndex]:
                            rich.print(f"[bright_red]{word}[/bright_red]", end=" ")
                        else:
                            print(word, end=" ")
                    print()
                #fill normal words, normal words is line stopping at index (first occurence of repeated word)
                # for word in read[baseLine][:repeatingIndexes[0][1]]:
                #     print(word)
                # for [i, j] in repeatingIndexes:
                #     rich.print("[bright_red]" + read[i][j] + "[/bright_red]", end=" ")
            unique = word
            repeatingIndexes = {lineNum: [wordInd]}