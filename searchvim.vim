python << eopython
import os
import sys
import vim

sys.path.append(
    os.path.join(os.path.expanduser('~'), '.vim/plugin')
)

if os.environ.has_key('VIRTUAL_ENV'):
    path = os.environ['VIRTUAL_ENV'] + '/lib/python2.6/site-packages'
    sys.path.append(path)

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
