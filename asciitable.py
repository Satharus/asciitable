#!/usr/bin/env python3
import sys
import os
import string

asciitable = {}
class colours:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    WHITE  = '\033[97m'
    BLACK  = '\033[90m'
    tableColour = BLUE
    textColour = GREEN

def enableWindowsCMDColor():
    if os.name == 'nt':
            os.system('COLOR') # Magical command that makes colors work in windows cmd.exe

def printCharacterInfo(char):
     print(colours.textColour + str(asciitable[char]["dec"]) + "\t" + str(asciitable[char]["hex"]) + "\t" + str(asciitable[char]["oct"]) + "\t" + str(asciitable[char]["char"]))

def isHexString(num):
    if len(num) == 0:
        return False
    for a in num:
        if a not in string.hexdigits:
            return False
    return True

def isOctalString(num):
    if len(num) == 0:
        return False
    for a in num:
        if a not in string.octdigits:
            return False
    return True

# Function takes a number string (x12, 67, o73) and returns the value based on its base
def parseIntFromString(num):
    if num.find('x') != -1 and isHexString(num[1::]):     #if hex
        return int(num[1::], 16)
    elif num.find('o') != -1 and isOctalString(num[1::]):   #if octal
        return int(num[1::], 8)
    elif num.isnumeric(): #if decimal
        return int(num, 10)
    else:
        return -1

def printRanges(arg):
    printHeader()
    ranges = arg.split(',')
    for a in ranges:
        if a.find('-') == -1: #if a single number
            val = parseIntFromString(a)
            if val == -1:
                print(colours.RED + "Invalid range(s): {} Pass -h for help".format(a))
                exit(1)
            elif 0 <= val <= 127:
                printCharacterInfo(val)
            else:
                print(colours.RED + "Invalid range(s): {} Pass -h for help".format(a))
                exit(1)
        elif a.find('-') != -1: #if a range
            values = a.split('-')
            lval = parseIntFromString(values[0])
            rval = parseIntFromString(values[1])
            if lval > rval or (lval > 127 or 0 > lval) or (rval > 127 or 0 > rval):
                print(colours.RED + "Invalid range(s): {}-{} Pass -h for help".format(values[0], values[1]))
                exit(1)
            for i in range(lval, rval+1):
                printCharacterInfo(i)
    exit(0)

def matchColours(arg):
    arg = arg.lower()
    if arg == "magenta":
        return colours.MAGENTA
    elif arg == "blue":
        return colours.BLUE
    elif arg == "green":
        return colours.GREEN
    elif arg == "yellow":
        return colours.YELLOW
    elif arg == "red":
        return colours.RED
    elif arg == "black":
        return colours.BLACK
    elif arg == "white":
        return colours.WHITE
    elif arg == "cyan":
        return colours.CYAN
    else:
        return "";

def help():
    a = os.path.basename(sys.argv[0])
    print("""{} - ASCII Table Printer\n
            Usage: {} [options]

                Prints the standard ASCII table from (0-127).

            Options:
            \t-h/--help - Print this help

            \t-q/--query [type] [value]
            \t   Used to query on rows and ranges from the ascii table.
            \t   type can be c/char for characters or n/number for numbers.
            \t   value is the value you  are making the query for.
            \t   values can be comma separated or ranges seperated by a '-'
            \t   use x for hex, o for octal, and insert characters as is.
            \t   Examples:
            \t\t{} -q c @\t\t\t"querying for the character @"
            \t\t{} -q c A-F,~\t\t"querying for ranges A to F and ~"
            \t\t{} -q n x15\t\t\t"querying for hex 15"
            \t\t{} -q n o7\t\t\t"querying for oct 7"
            \t\t{} -q n 17\t\t\t"querying for 17"
            \t\t{} -q n 20,x50-x54,o22\t"querying for 20 decimal, ranges 50-54 hex, and octal 22"\n

            \t-nc/--no-colour - Disable Colours

            \t-c/--colours [tablecolour] [textcolour]
            \t\tChoose the colours for the table. (Default: blue green)
            \t\t(magenta, blue, green, yellow, red, cyan, black, white)
            \t""".format(a,a,a,a,a,a,a,a,a,a))
    exit(1)

def checkForArguments():
    indexOfOption = 0
    if len(sys.argv) > 1:
        if "-h" in sys.argv or "--help" in sys.argv:
            help()
        if "-c" in sys.argv or "--colours" in sys.argv:
            if len(sys.argv) > 3:
                indexOfOption=sys.argv.index("-c" if "-c" in sys.argv else "--colours")
                colours.tableColour = matchColours(sys.argv[indexOfOption+1])
                colours.textColour = matchColours(sys.argv[indexOfOption+2])
            else:
                help()

        if "-nc" in sys.argv or "--no-colour" in sys.argv:
            indexOfOption=sys.argv.index("-nc" if "-nc" in sys.argv else "--no-colour" )
            colours.tableColour = ''
            colours.textColour = ''

        if "-q" in sys.argv or "--query" in sys.argv:
            indexOfOption=sys.argv.index("-q" if "-q" in sys.argv else "--query")
            queryType = sys.argv[indexOfOption+1]
            queryValue = sys.argv[indexOfOption+2]
            queryType = queryType.lower()
            if queryType == "c" or queryType == "char":
                queryAscii(queryValue, queryType="char")
            elif queryType == "n" or queryType == "number":
                printRanges(queryValue)
            else:
                print(colours.RED+"Invalid query type. Query types are c for chars or n for numbers")
            exit(0)

def prepareTable():
    for a in range(128):
        asciitable[a] = {}
        asciitable[a]["dec"] = a
        asciitable[a]["hex"] = hex(a)
        if a < 8:
            asciitable[a]["oct"] = "00" + str(oct(a))[2::]
        else:
            asciitable[a]["oct"] = "0" + str(oct(a))[2::]

        asciitable[a]["char"] = str(chr(a))

# Manual entries for the unprintable
    asciitable[0]["char"] = "NULL\t\t"
    asciitable[1]["char"] = "SOH (Start of Heading)"
    asciitable[2]["char"] = "STX (Start of Text)"
    asciitable[3]["char"] = "ETX (End of Text)"
    asciitable[4]["char"] = "EOT (End of Transm.)"
    asciitable[5]["char"] = "ENQ (Enquiry)\t"
    asciitable[6]["char"] = "ACK (Acknowledge)"
    asciitable[7]["char"] = "BEL (Bell)\t"
    asciitable[8]["char"] = "\\b (Backspace)\t"
    asciitable[9]["char"] = "\\t (Horizontal Tab)"
    asciitable[10]["char"] = "\\n (New line/LF)"
    asciitable[11]["char"] = "VT (Vertical Tab)"
    asciitable[12]["char"] = "FF (NP Form Feed)"
    asciitable[13]["char"] = "CR (Carriage Return)"
    asciitable[14]["char"] = "S0 (Shift Out)\t"
    asciitable[15]["char"] = "S1 (Shift In)\t"
    asciitable[16]["char"] = "DLE (Data Link Escape)"
    asciitable[17]["char"] = "DC1 (Device Control 1)"
    asciitable[18]["char"] = "DC2 (Device Control 2)"
    asciitable[19]["char"] = "DC3 (Device Control 3)"
    asciitable[20]["char"] = "DC4 (Device Control 4)"
    asciitable[21]["char"] = "NAK (Neg. Acknowledge)"
    asciitable[22]["char"] = "SYN (Synchronous Idle)"
    asciitable[23]["char"] = "ETB (End Trans Block)"
    asciitable[24]["char"] = "CAN (Cancel)\t"
    asciitable[25]["char"] = "EM (End of Medium)"
    asciitable[26]["char"] = "SUB (Substitute)"
    asciitable[27]["char"] = "ESC (Escape)\t"
    asciitable[28]["char"] = "FS (File Seperator)"
    asciitable[29]["char"] = "GS (Group Seperator)"
    asciitable[30]["char"] = "RS (Record Seperator)"
    asciitable[31]["char"] = "US (Unit Seperator)"
    asciitable[32]["char"] = "SPACE"
    asciitable[127]["char"] = "DEL"


def printTable():
    for a in range(3):
        if a == 0:
            print(colours.tableColour + "Dec\tHex\tOct\tChar\t", end ='\t\t|\t')
        print("Dec\tHex\tOct\tChar\t", end = '|\t')

    print("")

    for i in range(32):
        for j in range(4):
            a = asciitable[i+(j*32)]
            print(colours.textColour + str(a["dec"]) + "\t" + str(a["hex"]) + "\t" + str(a["oct"]) + "\t" + str(a["char"]) + "\t",
                    end=colours.tableColour + '|\t')
        print("")

def printHeader():
    print(colours.tableColour + "Dec\tHex\tOct\tChar")


def queryAscii(query, queryType="dec"):
    printHeader()
    if query == "," or ",,," in query or ",," in query:
        printCharacterInfo(ord(','))
    characters = query.split(',')
    if len(characters) == 1:
        a = characters[0]
        if len(a) == 1:
            printCharacterInfo(ord(a))
            return

    for a in characters:
        if len(a) == 0:
            continue
        elif len(a) == 1:
            printCharacterInfo(ord(a))
        elif len(a) == 3 and "-" in a:
            values= a.split('-')
            lval = ord(values[0])
            rval = ord(values[1])
            if lval > rval or (lval > 127 or 0 > lval) or (rval > 127 or 0 > rval):
                print(colours.RED + "Invalid range(s): {}-{} Pass -h for help".format(values[0], values[1]))
                exit(1)
            for i in range(lval, rval+1):
                printCharacterInfo(i)
        else:
            print(colours.RED + f"Invalid query: {a} is not a valid {queryType} or range.")




def main():
    prepareTable()
    enableWindowsCMDColor()
    checkForArguments()
    printTable()
    exit(0)

if __name__ == "__main__":
    main()
