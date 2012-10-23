from docopt import docopt
import fileinput
import sys

# Docopt configuration string. See Docopt.org.
doc ="""
Usage: 
    head1.py [-c <N>| -n <N>] [-q | -v] [FILENAME...]
    head1.py [FILENAME...]

Options:
    -c <N>, --bytes=N    print the first N bytes of each file
    -n <N>, --lines=N
    -q, --quiet
    -v, --verbose
"""
args = docopt(doc, argv=sys.argv[1:], help=True, version=None)

class LineObject(object):
    # A class to handle input files where the lines will be read
    def __init__(self,N,filename):
        self.length = abs(int(N)) # number of lines
        self.filename = filename # Name of file
        self.data_to_print = "" # initialise an output string
        self.source = open(filename, 'r') # open the file
        if int(N) > 0: # read first N lines
            for line in range(0,self.length):
                self.data_to_print = self.data_to_print + self.source.readline()
        else: # read all but last N lines
            data = self.source.read().split('\n') # create a list of the lines in the file
            for element in data[:(len(data)-self.length)]:
                self.data_to_print = self.data_to_print + element + '\n'
        
class ByteObject(object):
    # A class to handle input files where bytes are read
    def __init__(self,N,filename):
        self.length = abs(int(N)) # Same as Line Object
        self.filename = filename
        self.data_to_print = ""
        self.source  = open(filename, 'r')
        if int(N) > 0: # read first N bytes
            self.data_to_print = self.source.read(self.length)
        else: # read all but last N bytes
            data = self.source.read()
            self.data_to_print = data[:(len(data)-self.length)]           

    
    
def decorate_verbose(data, filename):
    # tag on file name if -v option is specified.
    header = "==>%s<==\n" % filename
    modified_data_to_print = "" + header + data
    return modified_data_to_print  
    
    
def main():
    # Main loop.
    if args['--bytes'] == None and args['--lines'] == None and not args['FILENAME']:
        for i in range(0,10): # read first 10 lines from stdin
            data = raw_input()
            print data
    elif args['--bytes'] != None and not args['FILENAME']: # read N bytes of stdin
        data = sys.stdin.read(int(args['--bytes']))
        print data
    elif args['--lines'] != None and not args['FILENAME']: # read N lines of stdin
        for i in range(1,int(args['--lines'])):
            data = raw_input()
            print data
    else:
        outputs = [] # store the output information. May be inefficient with big files or large amounts of files.
        for File in args['FILENAME']: # loop over filenames passed in command line
            if args['--bytes']: # if -c option was passed
                outputs.append(ByteObject(args['--bytes'],File))
            elif args['--lines']: # if -b option was passed
                outputs.append(LineObject(args['--lines'],File))
            else:
                outputs.append(LineObject('10',File)) # read in 10 lines of each file by default
        if args['--verbose']: # call verbose decorator on each item if specified and print
            for item in outputs:
                print decorate_verbose(item.data_to_print, item.filename)
        else:
            for item in outputs: # Just print
                print item.data_to_print    
                
                 

        
if __name__ == "__main__":
    main()
    


    
    
    
    
        


