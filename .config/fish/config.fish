if status is-interactive
    # Commands to run in interactive sessions can go here
end
if status is-interactive
    # Commands to run in interactive sessions can go here
end

set fish_greeting "Welcome deVOID"

# ENV
export PATH="$HOME/.cargo/bin:$HOME/.emacs.d/bin:$PATH"
export EDITOR="nano"
export GTK_THEME="Adwaita:dark"
# CARGO alias
alias cari="cargo init"
alias carr="cargo run"
alias carb="cargo build"
alias cart="cargo test"

# GIT alias
alias gclone="git clone"
alias gadd="git add"
alias gitaddall="git add -A"
alias ginit="git init"
alias gpush="git push origin"
alias gpull="git pull origin"
alias gremotea="git remote add origin"

# PACMAN alias
alias paci="sudo pacman -S"
alias pacr="sudo pacman -R"
alias pacu="sudo pacman -Syu"

# PROMPT
starship init fish | source
