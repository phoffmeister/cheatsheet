import argparse
import html as html_t
from pathlib import Path


class Cheatsheet():
    def __init__(self,
            nvim_path=None,
            nvim_marker='\" --cheat',
            nvim_separator='|',
            tmux_path=None,
            tmux_marker='# --cheat',
            tmux_separator='|',
            file_out='cheatsheet.html'):

        self.file_out=file_out
        self.cheats = dict()
        self.settings = dict()
        self.settings['nvim'] = dict()
        if not nvim_path:
            self.settings['nvim']['path'] = Path.home() / '.config' / 'nvim' / 'init.vim'
        else:
            self.settings['nvim']['path'] = nvim_path
        self.settings['nvim']['marker'] = nvim_marker
        self.settings['nvim']['separator'] = nvim_separator

        self.settings['tmux'] = dict()
        if not tmux_path:
            self.settings['tmux']['path'] = Path.home() / '.tmux.conf'
        else:
            self.settings['tmux']['path'] = tmux_path
        self.settings['tmux']['marker'] = tmux_marker
        self.settings['tmux']['separator'] = tmux_separator


    def config_exists(self, ident):
        return self.settings[ident]['path'].exists()


    def get_html_head(self):
        return """<!DOCTYPE html>
<html><head><title>CheatSheet</title><meta charset="utf-8"/>
<link rel="stylesheet" type="text/css" href="css/style.css"/>
</head>
<body><section>
"""

    def get_html_tail(self):
        return "</section></body></html>"

    def get_html_cheats(self):
        html = ""
        for ident in self.cheats:
            html += f"<article><h2>{ident}</h2>"
            html += "<table><tr><th>Command</th><th>Key Combo</th></tr>"
            for combo in self.cheats[ident]:
                html += f"<tr><td>{combo[0]}</td><td>{combo[1]}</td></tr>"
            html += "</table></article>"
        return html

    def read_cheats(self, ident):
        if ident not in self.settings:
            print( f'no settings for {ident}' )
            return

        marker = self.settings[ident]['marker']
        cheats = []
        with open(self.settings[ident]['path'], "r") as f:
            line = f.readline()
            while line:
                if line.startswith(marker):
                    line = line[len(marker):]
                    line = html_t.escape(line).replace("\\", "").rstrip()
                    ch = line.split('|', maxsplit=1)
                    cheats.append(
                            (ch[0].lstrip().rstrip(),
                                ch[1].lstrip().rstrip()))
                line = f.readline()
        self.cheats[ident] = cheats

    def write_html(self):
        with open(self.file_out, "w") as f:
            f.write(self.get_html_head())
            f.write(self.get_html_cheats())
            f.write(self.get_html_tail())


def main():
    parser = argparse.ArgumentParser(description='create a cheatsheet')
    parser.add_argument(
            '--tmux',
            help='include tmux commands',
            action='store_true')
    parser.add_argument(
            '--nvim',
            help='include nvim commands',
            action='store_true')

    args = parser.parse_args()

    cheat_sheet = Cheatsheet()
    if args.tmux:
        if cheat_sheet.config_exists('tmux'):
            print(f'using {cheat_sheet.settings["tmux"]["path"]} for tmux')
            cheat_sheet.read_cheats('tmux')

    if args.nvim:
        if cheat_sheet.config_exists('nvim'):
            print(f'using {cheat_sheet.settings["nvim"]["path"]} for nvim')
            cheat_sheet.read_cheats('nvim')

        cheat_sheet.write_html()


if __name__ == "__main__":
    main()
