dotfiles
--------

# clone
git clone --bare git@github.com:georgewhewell/dotfiles.git $HOME/.dotfiles

# checkout
git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME checkout

# pull submodules
git --git-dir=$HOME/.dotfiles --work-tree=$HOME submodule update --init
--recursive
