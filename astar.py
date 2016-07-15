# coding: utf-8
import heapq
import itertools
import curses
import time


def astar(init_pos, goal):
    passed_list = [init_pos]
    init_score = distance(passed_list) + heuristic(init_pos)
    checked = {init_pos: init_score}
    searching_heap = []
    heapq.heappush(searching_heap, (init_score, passed_list))
    while len(searching_heap) > 0:
        score, passed_list = heapq.heappop(searching_heap)
        last_passed_pos = passed_list[-1]
        if last_passed_pos == goal:
            print(passed_list)
            return passed_list
        for pos in nexts(last_passed_pos):
            new_passed_list = passed_list + [pos]
            pos_score = distance(new_passed_list) + heuristic(pos)
            if pos in checked and checked[pos] <= pos_score:
                continue
            checked[pos] = pos_score
            heapq.heappush(searching_heap, (pos_score, new_passed_list))
    return []

if __name__ == "__main__":
    dungeon = [
    '------------------------------------',
    '|< |    |     |         |          |',
    '|  | |  |  |  |         |  ---    >|',
    '|    |     |  --------- |  |  -----|',
    '|-------------   |      |  |       |',
    '|                |  |              |',
    '|        ---     |  |     ---------|',
    '|   |    |    ----  |     |        |',
    '|   |    |          |     |  |  ---|',
    '|   |    | ----     |---     |     |',
    '|        |          |        |     |',
    '------------------------------------',
#        '-------',
#        '|<|  >|',
#        '| |   |',
#        '|   | |',
#        '-------',
        ]

    def find_ch(ch):
        for i, l in enumerate(dungeon):
            for j, c in enumerate(l):
                if c == ch:
                    return (i, j)

    init = find_ch("<")
    goal = find_ch(">")

    def nexts(pos):
        for a, b in itertools.product(['+1', '-1', ''], repeat=2):
            if a or b:
                chk=dungeon[eval('pos[0]' + a)][eval('pos[1]' + b)]
                if  (chk!="|" and chk!="-"):
                    yield (eval('pos[0]' + a), eval('pos[1]' + b))

    def heuristic(pos):
        return ((pos[0] - goal[0]) ** 2 + (pos[1] - goal[1]) ** 2) * 0.5

    def distance(path):
        return len(path)

    path = astar(init, goal)

    def render_path(self):
        while True:
            w= curses.initscr()
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
            i=0
            for l in dungeon:
                w.addstr(i,0,l)
                i=i+1
            for pos in path[1:-1]:
                w.addstr(pos[0],pos[1] ,"*", curses.color_pair(1))
                w.refresh()
                time.sleep(0.4)
    curses.wrapper(render_path)