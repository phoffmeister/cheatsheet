import argparse
import html as html_t
from pathlib import Path


class Cheatsheet():
    std_loc = {
            'nvim': [],
            'tmux': [],
            }
    # nvim file locations
    std_loc['nvim'].append(Path.home() / '.config' / 'nvim' / 'init.vim')
    std_loc['nvim'].append(Path.home() / '.vimrc')

    # tmux file locations
    std_loc['tmux'].append(Path.home() / '.tmux.conf')

    def get_first_loc(ident):
        if ident in Cheatsheet.std_loc:
            for loc in Cheatsheet.std_loc[ident]:
                if loc.exists():
                    return loc
            return None
        else:
            return None

    def get_head():
        return """<!DOCTYPE html>
<html><head><title>CheatSheet</title><meta charset="utf-8"/>
<link rel="stylesheet" type="text/css" href="css/style.css"/>
</head>
<body><section>
"""

    def get_tail():
        return "</section></body></html>"

    def get_cheats(cheat_data):
        html = ""
        for k in cheat_data:
            html += f"<article><h2>{k}</h2>"
            html += "<table><tr><th>Command</th><th>Key Combo</th></tr>"
            for combo in cheat_data[k]:
                html += f"<tr><td>{combo[0]}</td><td>{combo[1]}</td></tr>"
            html += "</table></article>"
        return html

    def read_file(file_p, marker):
        cheats = []
        with open(file_p, "r") as f:
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
        return cheats


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

    cheats = {}
    if args.tmux:
        file_loc = Cheatsheet.get_first_loc('tmux')
        if file_loc:
            print(f'using {file_loc} for tmux')
            cheats['tmux'] = Cheatsheet.read_file(file_loc, "#cheat")

    if args.nvim:
        file_loc = Cheatsheet.get_first_loc('nvim')
        if file_loc:
            print(f'using {file_loc} for nvim')
            cheats['nvim'] = Cheatsheet.read_file(file_loc, "\"cheat")

    with open("cheatsheet.html", "w") as f:
        f.write(Cheatsheet.get_head())
        f.write(Cheatsheet.get_cheats(cheats))
        f.write(Cheatsheet.get_tail())


if __name__ == "__main__":
    main()
