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
    
    def __init__(self,N,filename):
        self.length = abs(int(N))
        self.filename = filename
        self.data_to_print = ""
        self.source = open(filename, 'r')
        if int(N) > 0:
            for line in range(0,self.length):
                self.data_to_print = self.data_to_print + self.source.readline()
        else:
            data = self.source.read().split('\n') # create a list of the lines in the file
            for element in data[:(len(data)-self.length)]:
                self.data_to_print = self.data_to_print + element + '\n'
        
class ByteObject(object):
    
    def __init__(self,N,filename):
        self.length = abs(int(N))
        self.filename = filename
        self.data_to_print = ""
        self.source  = open(filename, 'r')
        if int(N) > 0:
            self.data_to_print = self.source.read(self.length)
        else:
            data = self.source.read()
            self.data_to_print = data[:(len(data)-self.length)]           
        

    
    
def decorate_verbose(data, filename):
    header = "==>%s<==\n" % filename
    modified_data_to_print = "" + header + data
    return modified_data_to_print  
    
    
def main():
    
    if args['--bytes'] == None and args['--lines'] == None and not args['FILENAME']:
        for i in range(0,10):
            data = raw_input()
            print data
    elif args['--bytes'] != None and not args['FILENAME']:
        data = sys.stdin.read(int(args['--bytes']))
        print data
    elif args['--lines'] != None and not args['FILENAME']:
        for i in range(1,int(args['--lines'])):
            data = raw_input()
            print data
    else:
        outputs = []
        for File in args['FILENAME']:
            if args['--bytes']:
                outputs.append(ByteObject(args['--bytes'],File))
            elif args['--lines']:
                outputs.append(LineObject(args['--lines'],File))
            else:
                outputs.append(LineObject('10',File))
        if args['--verbose']:
            for item in outputs:
                print decorate_verbose(item.data_to_print, item.filename)
        else:
            for item in outputs:
                print item.data_to_print    
                
                 

        
if __name__ == "__main__":
    main()
    


    
    
    
    
        


