# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def characterFrequencyCount(text, character):
    counter = 0
    for x in text:
        if(x == character):
            counter += 1
    print(character ,counter)
    return counter;

def substitutionMethod(text, input, substitution):
    counter = 0
    text = text.replace(input, substitution)
    return text;
textInput = """
                lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi 
                jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr 
                jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj 
                rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj 
                yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt
                wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
                iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
                vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
                wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx
                rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
                ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
                mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
                bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
                wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
                riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb    
            """
print(textInput)

"""
characterFrequencyCount(textInput, 'x')
characterFrequencyCount(textInput, 'l')
characterFrequencyCount(textInput, 'r')
characterFrequencyCount(textInput, 'v')
characterFrequencyCount(textInput, 'n')
characterFrequencyCount(textInput, 'm')
characterFrequencyCount(textInput, 'i')
characterFrequencyCount(textInput, 'b')
characterFrequencyCount(textInput, 'p')
characterFrequencyCount(textInput, 's')
characterFrequencyCount(textInput, 'u')
characterFrequencyCount(textInput, 'j')
characterFrequencyCount(textInput, 'w')
characterFrequencyCount(textInput, 'y')
characterFrequencyCount(textInput, 'q')
characterFrequencyCount(textInput, 'h')
characterFrequencyCount(textInput, 'd')

characterFrequencyCount(textInput, 't')
"""

#textInput = substitutionMethod(textInput,'b', 'T')
#textInput = substitutionMethod(textInput,'p', 'H')
#textInput = substitutionMethod(textInput,'r', 'E')


textInput = substitutionMethod(textInput,'b', 'T')
textInput = substitutionMethod(textInput,'p', 'H')
textInput = substitutionMethod(textInput,'r', 'E')
textInput = substitutionMethod(textInput,'j', 'O')
textInput = substitutionMethod(textInput,'w', 'I')
textInput = substitutionMethod(textInput,'y', 'M')
textInput = substitutionMethod(textInput,'x', 'F')


textInput = substitutionMethod(textInput,'l', 'B')
textInput = substitutionMethod(textInput,'v', 'C')#------
textInput = substitutionMethod(textInput,'i', 'S') #------
textInput = substitutionMethod(textInput,'t', 'Y')
textInput = substitutionMethod(textInput,'s', 'P')
textInput = substitutionMethod(textInput,'n', 'U')
textInput = substitutionMethod(textInput,'k', 'N')
textInput = substitutionMethod(textInput,'u', 'R')
textInput = substitutionMethod(textInput,'c', 'W')


textInput = substitutionMethod(textInput,'d', 'D')
textInput = substitutionMethod(textInput,'m', 'A')
textInput = substitutionMethod(textInput,'q', 'K')

textInput = substitutionMethod(textInput,'e', 'V')

textInput = substitutionMethod(textInput,'h', 'L')

textInput = substitutionMethod(textInput,'t', '*')

textInput = substitutionMethod(textInput,'a', 'X')
textInput = substitutionMethod(textInput,'o', 'G')
textInput = substitutionMethod(textInput,'g', 'Z')









print(textInput)

