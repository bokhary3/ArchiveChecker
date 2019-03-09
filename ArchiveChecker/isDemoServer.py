with open('/Users/elsayedhussein/Documents/iOS Development/Projects/ArchiveChecker/ArchiveChecker/Configurations.swift','r') as f:
    i = 0
    for line in f:
        i += 1
        if 'var' in line:
            words =  line.rstrip('\n').split(" ")
            if words[1] == 'isDemoServer' and words[3] == 'true':
                print(f.name + ':' + str(i) + ': error: Can\'t archive, your are on demo server!!!!! 😱')
                exit(1)
