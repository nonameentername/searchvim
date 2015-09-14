let s:path = expand('<sfile>:p:h')

python << eopython
import os
import site
import sys
import vim

sys.path.append(vim.eval('s:path'))

if os.environ.has_key('PYENV_ROOT'):
    path = os.path.join(os.environ['PYENV_ROOT'],
        'versions/default/lib/python2.7/site-packages')
    site.addsitedir(path)

from searchvim.searchfile import searchfile
from searchvim.searchbuffer import searchbuffer
from searchvim.searchtags import searchtags
from searchvim.searchgrep import searchgrep
from searchvim.config import ins
eopython

nmap<silent><leader>f :py sf = searchfile()<cr>
nmap<silent><leader>b :py sb = searchbuffer()<cr>
nmap<silent><leader>t :py st = searchtags()<cr>
nmap<silent><leader>s :py sg = searchgrep()<cr>
