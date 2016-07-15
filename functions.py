import os, commands

def checkPath(path):
    try:
        if os.path.isdir(path):
            if os.listdir(path) == 0:
                return True
            else:
                print 'path is not empty!'
                return False
        else:
            print 'path is not exists!'
            return False
    except Exception, e:
        print e
        return False


def writeFile(path, content):
    try:
        fileName = os.path.join(path, 'oplog.index')
        f = open(fileName, 'a+')
        f.write(content)
        return True
    except Exception, e:
        print e
        return False


def getCommandLine(dictionary):
    command_line = ''
    for key in dictionary.keys():
        command_line += ' --' + key + ' ' + str(dictionary[key]) + ' '
    return command_line

def dump(command_line, other):
    commands.getstatusoutput('mongodump' + command_line + other)
