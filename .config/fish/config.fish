if status is-interactive
    # Commands to run in interactive sessions can go here
end

set fish_greeting "Welcome deVOID"

# ENV
export PATH="$HOME/.cargo/bin:$HOME/.emacs.d/bin:$PATH"
export TERM="alacritty"

# XBPS alias
alias xinstall="sudo xbps-install -S"
alias xupdate="sudo xbps-install -Syu"
alias xremove="sudo xbps-remove"
alias xremoveR="sudo xbps-remove -R"
alias xfind="sudo xbps-query -s"
alias xcfg="sudo xbps-reconfigure"
alias xalt="sudo xbps-alternatives"
alias xpkg="sudo xbps-pkgdb"
alias xindx="sudo xbps-rindex"
alias xpkghold="sudo xbps-pkgdb -m hold"
alias xpkgunhold="sudo xbps-pkgdb -m unhold"

# GIT alias
alias gclone="git clone"
alias gadd="git add"
alias gitaddall="git add -A"
alias ginit="git init"
alias gpush="git push origin"
alias gpull="git pull origin"
alias gremotea="git remote add origin"

# CARGO alias
alias cari="cargo init"
alias carr="cargo run"
alias carb="cargo build"
alias cart="cargo test"

# PROXYCHAINS alias
alias xproxy="proxychains4"

# RUNIT alias
function sysadd
    ln -s "/etc/sv/$argv" "/var/service/"
end

function sysrm
	rm "/var/service/$argv"
end

export TERM=alacritty

# PROMPT
starship init fish | source
