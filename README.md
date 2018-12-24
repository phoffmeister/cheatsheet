# Cheatsheet
This program generates cheatsheets. For now only nvim and tmux is supported.
## Getting Started
You will need to have python installed. [Download](https://www.python.org/downloads/)
### Prerequisits
You will have to prepare your config files to generate the cheatsheet.
### nvim
You have to put commments in your config file starting with `"cheat` followed by what the following line is doing, then a separator `|` and finally the key combo.
E.g. annotate your `~/.config/nvim/init.vim` file like this:
```
...
"cheat go to first char | H
noremap H ^

"cheat go to last char | L
nnoremap L g_
...
```
### tmux
You have to put commments in your config file starting with `#cheat` followed by what the following line is doing, then a separator `|` and finally the key combo.
E.g. annotate your `.tmux.conf` file like this:
```
...
#cheat split horizontal | prefix |
bind | split-window -h

#cheat split vertical | prefix -
bind - split-window -v
...
```
### Usage
```
python cheater.py --nvim --tmux
```
This will generate a cheatsheet.html file.
### Authors
* **Pierre Hoffmeister** - *Initial work* [pierre87](https://github.com/pierre87)

