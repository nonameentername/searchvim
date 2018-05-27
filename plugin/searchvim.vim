if !has('python3')
    finish
endif

let s:path = expand('<sfile>:p:h')

python3 << eopython
import os
import site
import sys
import vim

sys.path.append(vim.eval('s:path'))

if 'PYENV_ROOT' in os.environ:
    path = os.path.join(os.environ['PYENV_ROOT'],
        'versions/default/lib/python3.6/site-packages')
    site.addsitedir(path)

from searchvim.searchfile import searchfile
from searchvim.searchbuffer import searchbuffer
from searchvim.searchtags import searchtags
from searchvim.searchgrep import searchgrep
from searchvim.config import ins
eopython

nmap<silent><leader>f :py3 sf = searchfile()<cr>
nmap<silent><leader>b :py3 sb = searchbuffer()<cr>
nmap<silent><leader>t :py3 st = searchtags()<cr>
nmap<silent><leader>s :py3 sg = searchgrep()<cr>
