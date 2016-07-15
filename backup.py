import argparse, sys, functions

def fullBackup(dictionary):
    del dictionary['basedir']
    del dictionary['increment']
    del dictionary['full']
    command_line = functions.getCommandLine(dictionary)
    functions.dump(command_line, '')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='mongoBackupToolkit')
    parser.add_argument('--host', action='store', dest='host')
    parser.add_argument('--port', action='store', dest='port', type=int, default=0)
    parser.add_argument('--out', action='store', dest='out')
    parser.add_argument('--full', action='store_true', dest='full', default=False)
    parser.add_argument('--increment', action='store_true', dest='increment', default=False)
    parser.add_argument('--basedir', action='store', dest='basedir')
    
    args = parser.parse_args(['--host=127.0.0.1', '--port=', '--out=F:\\data\\backup', '--full'])

    if args.full == args.increment:
        print 'can not both use full and increment args!'
        sys.exit(2)

    if args.host.strip() == '':
        print 'must input host ip'
        sys.exit(2)

    if args.port == 0:
        print 'must input port!'
        sys.exit(2)

    if args.full:
        if args.basedir.strip() == 0:
            print 'must input full backup dir!'
            sys.exit(2)

    host = args.host
    port = args.port
    out = args.out
    full = args.full
    increment = args.increment
    basedir = args.basedir

    dictionary = {"host":host, "port":port, "out":out, "full":full, "increment":increment, "basedir":basedir}
    if dictionary['full']:
        fullBackup(dictionary)


