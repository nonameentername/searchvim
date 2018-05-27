import os
import re
import time
import vim
from subprocess import *
from .config import ins

class searchvim:

    def __init__(self):
        self.name = self.__class__.__name__

        try:
            self.start = time.time()
            self.lines = self.getlines()
        except Exception as e:
            print (e)
            vim.command('silent!bd! %s' % self.name)
            return

        if hasattr(self, 'ignorelist'):
            self.lines = self.ignore(self.lines)

        if not hasattr(self, 'delete'):
            self.delete = True

        self.searchname = ''
        ins[self.name] = self

        vim.command('e %s' % self.name)
        self.w = vim.current.window
        self.b = vim.current.buffer

        vim.command('setlocal buftype=nofile')
        vim.command('setlocal bufhidden=hide')
        vim.command('setlocal noswapfile')

        vim.command('nmap <silent><buffer><C-k> :py3 ins["%s"].up()<cr>' % self.name)
        vim.command('nmap <silent><buffer><C-j> :py3 ins["%s"].down()<cr>' % self.name)
        vim.command('nmap <silent><buffer><BS> :py3 ins["%s"].backspace()<cr>' % self.name)
        vim.command('nmap <silent><buffer><Enter> :py3 ins["%s"].enter()<cr>' % self.name)
        vim.command('nmap <silent><buffer><Esc> :py3 ins["%s"].exit()<cr>' % self.name)

        for char in '*._-^$':
            vim.command('nmap <silent><buffer>%s :py3 ins["%s"].keydown("%s")<cr>' % (char, self.name, char))

        for num in range(0,10):
            vim.command('nmap <silent><buffer>%s :py3 ins["%s"].keydown("%s")<cr>' % (num, self.name, num))

        for num in range(97,123):
            vim.command('nmap <silent><buffer>%s :py3 ins["%s"].keydown("%s")<cr>' % (chr(num), self.name, chr(num)))

        for num in range(97,123):
            vim.command('nmap <silent><buffer><S-%s> :py3 ins["%s"].keydown("%s".upper())<cr>' % (chr(num), self.name, chr(num)))

        self.update()

    def up(self):
        if self.w.cursor[0] > 1:
            self.w.cursor = self.w.cursor[0]-1, self.w.cursor[1],

    def down(self):
        if self.w.cursor[0] < len(self.b):
            self.w.cursor = self.w.cursor[0]+1, self.w.cursor[1],

    def exit(self):
        vim.command('silent!bd! %s' % self.name)

    def enter(self):
        if len(self.b) > 1:
            if self.w.cursor[0] == 1:
                self.handleselect(self.b[1])
                if self.delete:
                    vim.command('silent!bd! %s' % self.name)
            elif self.w.cursor[0] > 1 or self.b[0] == self.b[1]:
                self.handleselect(self.b[self.w.cursor[0]-1])
                if self.delete:
                    vim.command('silent!bd! %s' % self.name)

    def backspace(self):
        self.searchname = self.searchname[:-1]
        self.update()

    def keydown(self, char):
        self.searchname += char
        self.update()

    def update(self):
        self.b[:] = None
        self.b[0] = self.searchname

        def validate(reg, line):
            try:
                if reg.islower():
                    return re.search(reg, line, re.IGNORECASE)
                else:
                    return re.search(reg, line)
            except:
                return False

        [self.b.append(line) for line in sorted(self.lines) if validate(self.searchname, line)]
        if len(self.b) == 2:
            self.b[0] = self.b[1]
        self.w.cursor = (1, len(self.searchname))

    def _check_timeout(self):
        if time.time() - self.start > 1:
            raise Exception("Timed out!")

    def adddict(self, d, key, value):
        self._check_timeout()

        if key in d:
            i = 1
            while '%s [%s]' % (key,i) in d:
                i+=1
            d['%s [%s]' % (key,i)] = value
        else:
            d[key] = value

    def ignore(self, lines):
        result = {}

        for line in lines:
            for item in self.ignorelist:
                if re.match(item, line):
                    break
            else:
                result[line] = lines[line]

        return result

    def getlines(self):
        pass

    def handleselect(self, lineindex):
        pass
