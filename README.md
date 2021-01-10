# FingerPrintz
Taking a list of urls and making appending it to a file to make unique domain/arguments/directories list, the script also checks for duplicates in the output file and will not append if there is.

Usage:

-i inputfile -o outputfile -m mode

there are currently 3 modes:
u - extracting domains
a - extracting arguments
d - extracting directories
all - extracting domains, arguments and directories

The choosed mode will extract the output and append it into the ouputfile if its not existed already.
