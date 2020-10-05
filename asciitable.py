#!/usr/bin/env python3
import sys
import os


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
    print("""{} - ASCII Table Printer\n
            \t-h/--help - Print this help
            \t-nc/--no-colour - Disable Colours
            \t-c/--colours [tablecolour] [textcolour]
            \t\tChoose the colours for the table. (Default: blue green)
            \t\t(magenta, blue, green, yellow, red, cyan, black, white)""".format(sys.argv[0][2::]))
    exit(1)

def checkForArguments():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            help()
        elif sys.argv[1] == "-c" or sys.argv[1] == "--colours":
            if len(sys.argv) > 3:
                colours.tableColour = matchColours(sys.argv[2])
                colours.textColour = matchColours(sys.argv[3])
            else:
                help()

        elif sys.argv[1] == "-nc" or sys.argv[1] == "--no-colour":
            colours.tableColour = ''
            colours.textColour = ''
        else:
            help()
            exit(1)


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


def main():
    checkForArguments()
    prepareTable()
    enableWindowsCMDColor()
    printTable()
    exit(0)

if __name__ == "__main__":
    main()
