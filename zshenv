SAVEHIST=1000000
HISTFILE=~/.zsh_history

local WORDCHARS='*?_[]~=&;!#$%^(){}<>'

[[ -s ~/.aliases ]] && source ~/.aliases

setopt share_history
setopt hist_expire_dups_first
setopt hist_find_no_dups

export HISTSIZE=100000
export HISTFILESIZE=100000
export PATH=$HOME/bin:/usr/local/bin:$PATH
export PATH="/usr/local/bin:$PATH"
export PATH="/usr/local/sbin:$PATH"
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
export EDITOR="/usr/local/bin/nvim"
export VISUAL="/usr/local/bin/nvim"
export DJANGO_SETTINGS_MODULE=settings
export PYTHONPATH=.
export sde_admin_repo_path='/Users/jhaine/dev/sde-admin/'
export sde_build_repo_path='/Users/jhaine/dev/sde-build/'
export CSC_LINK=/Volumes/JHaine_EncryptedDisk1/SecurityCompass/comodo-csc-2018.p12

export LDFLAGS="-L/usr/local/opt/readline/lib"
export CPPFLAGS="-I/usr/local/opt/readline/include"

export HOMEBREW_NO_ANALYTICS=1
export DOTNET_CLI_TELEMETRY_OPTOUT=true
export PATH="$PATH:/Users/jhaine/.dotnet/tools"
export PATH="/usr/local/opt/openssl/bin:$PATH"

export GITLAB_TOKEN=%NOPE%
export CSC_KEY_PASSWORD=%NOPE%
