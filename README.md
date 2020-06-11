# Cheatsheet
This program generates cheatsheets. For now only nvim and tmux is supported.

## Getting Started
You will need to have python installed.
[Download](https://www.python.org/downloads/)

### Prerequisits
You will have to prepare your config files to generate the cheatsheet.

### nvim
You have to put commments in your config file starting with `" --cheat` followed
by a description of the cheat, then a separator `|` and finally the key combo.
E.g. annotate your `~/.config/nvim/init.vim` file like this:
```
...
noremap H ^
" --cheat go to first char | H

nnoremap L g_
" --cheat go to last char | L
...
```

### tmux
You have to put commments in your config file starting with `# --cheat` followed
by a description of the cheat, then a separator `|` and finally the key combo.
E.g. annotate your `.tmux.conf` file like this:
```
...
bind | split-window -h
# --cheat split horizontal | prefix |

bind - split-window -v
# --cheat split vertical | prefix -
...
```

### Usage
```
python cheater.py --nvim --tmux
```
This will generate a cheatsheet.html file.

### Authors
* **Pierre Hoffmeister** - *Initial work* 
[phoffmeister](https://github.com/phoffmeister)

