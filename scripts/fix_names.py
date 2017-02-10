#!/usr/bin/env python 

'''
                    Space Telescope Science Institute

Synopsis:  

This routine is intended to fixup all of the names in the
data directories.  It copies a master atomicdata file to
the same name.orig and replaces .py with .dat and writes
out a set of git commands to fix up the names in the 
subdirectories


Command line usage (if any):

    usage: fix_names.py filename

Description:  

Primary routines:

    doit

Notes:
                                       
History:

170210 ksl Coding begun

'''

import sys
from astropy.io import ascii
import numpy
import shutil
import os

def remove_dups(filename='all.ls',outfile='FixAll'):
    '''
    Having run my script to generate the git
    mv commands, I need to remove the duplicate
    commands to prevent a  lot of errors
    '''

    x=open(filename)
    files=x.readlines()
    x.close()

    commands=[]
    for one in files:
        one=one.strip()
        x=open(one)
        lines=x.readlines()
        commands=commands+lines
        x.close()

    commands=numpy.array(commands)
    xcommands=numpy.unique(commands)

    x=open(outfile,'w')
    for one in xcommands:
        x.write(one)
    x.close()




def doit(filename='h10'):
    '''
    Do something magnificent

    Description:

    Notes:

    History:


    '''
    # First read the file

    try:
        f=open(filename,'r')
        xlines=f.readlines()
        f.close()
    except IOError :
        print ("The file %s does not exist" % filename)
        return 

    if os.path.isfile(filename+'.orig')==False:
        shutil.copy(filename,filename+'.orig')


    commands=[]
    new=[]
    for line in xlines:
        z=line.strip()
        if z[0]=='#':
            new.append(z)
        elif len(z)==0:
            pass
        elif z.count('.py'):
            new_name=z.replace('.py','.dat')
            one_command='git mv %s %s' % (z.replace('data/',''),new_name.replace('data/',''))
            commands.append(one_command)
            new.append(new_name)
        elif z.count('.data'):
            new_name=z.replace('.data','.dat')
            one_command='git mv %s %s' % (z.replace('data/',''),new_name.replace('data/',''))
            commands.append(one_command)
            new.append(new_name)
        else:
            new.append(z)

    if len(commands)==0:
        print('This file has already been processed')
        return

    g=open(filename,'w')
    for one in new:
        g.write('%s\n' % one)
    g.close()

    g=open('Fix_'+filename,'w')
    for one in commands:
        g.write('%s\n' % one)
    g.close()


    return


    





# Next lines permit one to run the routine from the command line
if __name__ == "__main__":
    import sys
    if len(sys.argv)>1:
        # doit(int(sys.argv[1]))
        doit(sys.argv[1])
    else:
        print ('usage: fix_names.py filename')
