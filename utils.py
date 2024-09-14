# ターミナル上でのカーソル洗濯操作用のライブラリ
# cursesライブラリを使用
# 完成しだい、別ファイルで使用する予定

import curses

def menu(stdscr):
    # 選択肢リスト
    choices = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Exit']
    current_row = 0

    # 選択肢を表示するための関数
    def print_menu(stdscr, current_row):
        stdscr.clear()
        for idx, row in enumerate(choices):
            if idx == current_row:
                stdscr.addstr(idx, 0, row, curses.color_pair(1))  # ハイライト
            else:
                stdscr.addstr(idx, 0, row)
        stdscr.refresh()

    # カラー設定（ハイライト用）
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    while True:
        print_menu(stdscr, current_row)

        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_row = (current_row - 1) % len(choices)  # 上に移動
        elif key == curses.KEY_DOWN:
            current_row = (current_row + 1) % len(choices)  # 下に移動
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # エンターキーで選択
            if current_row == len(choices) - 1:  # "Exit"が選択された場合
                break
            stdscr.addstr(len(choices), 0, f"You selected '{choices[current_row]}'")
            stdscr.refresh()
            stdscr.getch()  # エンターキーが押されるまで待機
        stdscr.clear()

# curses.wrapperを使ってメニューを実行
curses.wrapper(menu)
