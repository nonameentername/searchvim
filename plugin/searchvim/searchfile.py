import os
import re
import sys
import vim
from subprocess import *
from .searchvim import searchvim

class searchfile(searchvim):

    def __init__(self):
        self.ignorelist = ['.*pyc$', '.*class$']
        searchvim.__init__(self)

    def handleselect(self, line):
        vim.command('silent!edit %s' % self.lines[line])

    def getlines(self):
        result = {}

        for root, dirs, files in os.walk('.'):
            for name in files:
                self.adddict(result, '%s (%s)' % (name, root[2:]), os.path.join(root[2:],name))

            for name in dirs:
                if name.startswith('.'):
                    dirs.remove(name)

        return result
