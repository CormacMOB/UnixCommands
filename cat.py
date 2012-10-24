from docopt import docopt
import sys
import fileinput

doc ="""
    Usage:
        cat.py 
        cat.py [-n | -b][-svTE][FILE...]
        
    Options:
        -b, --number-nonblank       Number all non blank lines
        -E, --show-ends             Add $ to end of line
        -n, --number                Number all lines
        -s, --squeeze-blank         Squeeze all multiple empty lines to a single empty line
        -T, --show-tabs             insert ^I to denote tabs
        -v, --show-non-printing     Show non-printing characters
        --help
"""
# Note combinatory options are not implemented. I heavily consulted Lecturer example for this.
# Thanks Anthony Brew. Also see www.docopt.org
args = docopt(doc, argv=sys.argv[1:], help=True)

decorators = [] # list to hold active decorators

def decorate_squeeze(line): # more or less taken from Lecturer example.
    if last_blank == True and line.isspace()==True:
        return None
    return line
    
def decorate_numbers(line):
    if line:
        line = "%d    %s" %(line_number, line)
        return line
    
def decorate_nonblank(line): 
    if line.isspace() == False:
        line = line = "%d    %s" %(non_blank_line_number, line)
    return line
    

def decorate_show_ends(line): # find the positon of \n and place a $ before it
    line = line[:line.find('\n')] + '$' + '\n'
    return line
    
def decorate_show_tabs(line): # replace tabs with ^I
    line = line.replace('\t','^I',line.count('\t'))
    return line

def decorate_non_printing(line):# use repr string format to show non-printing chars.
    line = '%r' % line
    return line
    
decorator_dictionary = { '--number':decorate_numbers, '--number-nonblank':decorate_nonblank, '--show-ends':decorate_show_ends, '--show-tabs':decorate_show_tabs, '--show-non-printing':decorate_non_printing, '--squeeze-blank':decorate_squeeze} # dictionary to relate docopt options to methods.
# Three global variables for use in methods
line_number = 0
non_blank = 0
last_blank = False
    
    
def main():
    global decorators
    global decorator_dictionary
    global line_number
    global non_blank_line_number
    global last_blank
    
    for index,value in decorator_dictionary.items():
        if args[index]:
            decorators.append(value)
        else:
            pass
    #print decorators
    
    for line in fileinput.input(args['FILE']): # Create FileInput instance to handle files.
        line_number = fileinput.lineno()
        
        if fileinput.isfirstline() == True: # reset count of non_blank_line_number for a new file.
           non_blank_line_number = 1
        elif line.isspace() == False: # if a line is blank.
           non_blank_line_number += 1
     
        
        output_line = line
        for d in decorators: # loop to apply decorators
            output_line = d(output_line)
            
        if line.isspace()==True: # update last_blank to ensure we know if a blank just passed
            last_blank = True
        else:
            last_blank = False
        
        if output_line is not None: # if the line isnt none, print it.
            print output_line,
        
if __name__ == "__main__":
    main()
