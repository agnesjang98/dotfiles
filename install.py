import os

# Linux - create "Default (Linux).sublime-mousemap" in ~/.config/sublime-text-3/Packages/User
# Mac - create "Default (OSX).sublime-mousemap" in ~/Library/Application Support/Sublime Text 3/Packages/User
# Win - create "Default (Windows).sublime-mousemap" in %appdata%\Sublime Text 3\Packages\User

include = {
    # Editors
    'init.vim': '$HOME/.config/nvim/init.vim',
    'vimrc': '$HOME/.vimrc',

    # coc.nvim
    'coc-settings.json': ['$HOME/.config/nvim/coc-settings.json', '$HOME/.vim/coc-settings.json'],

    # pdb
    'pdbrc': '$HOME/.pdbrc',

    # pdb++
    'pdbrc.py': '$HOME/.pdbrc.py'

    # Terminal
    'kitty.conf': '$HOME/.config/kitty/kitty.conf',

    # Shell
    'bashrc': '$HOME/.bashrc',
    'aliases': '$HOME/.aliases',
    'zshenv': '$HOME/.zshenv',
    'zshrc': '$HOME/.zshrc',
    'plugins.txt': '$HOME/.plugins.txt',
}

# home = os.path.expanduser('~')
here = os.path.abspath('.')

cmds = []
for f, install_path in include.iteritems():
    local_file = "%s/%s" % (here, f)

    if isinstance(install_path, list):
        for path in install_path:
            cmds.append('ln -sf %s %s' % (local_file, path))
    else:
        cmds.append('ln -sf %s %s' % (local_file, install_path))

for cmd in cmds:
    print cmd
    os.system(cmd)
