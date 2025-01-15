!pip install -U kogi-canvas


import random
import copy


BLACK = 1
WHITE = 2


# オセロボードの評価テーブル
# 角が高得点、辺もそれなりに評価する
SCORE_TABLE = [
    [100, -20, 10, 10, -20, 100],
    [-20, -50, -2, -2, -50, -20],
    [10, -2, 1, 1, -2, 10],
    [10, -2, 1, 1, -2, 10],
    [-20, -50, -2, -2, -50, -20],
    [100, -20, 10, 10, -20, 100],
]


def evaluate_position(board, stone):
    """
    現在のボードの評価値を計算する関数。
    board: 2次元配列のオセロボード
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    return: 評価値
    """
    score = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == stone:
                score += SCORE_TABLE[y][x]
            elif board[y][x] == 3 - stone:
                score -= SCORE_TABLE[y][x]
    return score


def simulate_move(board, stone, x, y):
    """
    石を置いた後のボードをシミュレーションする関数。
    board: 現在のボード
    stone: プレイヤーの石
    x, y: 石を置く位置
    return: 石を置いた後のボード
    """
    new_board = copy.deepcopy(board)


    new_board[y][x] = stone
    opponent = 3 - stone
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        captured = []


        while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and new_board[ny][nx] == opponent:
            captured.append((nx, ny))
            nx += dx
            ny += dy


        if captured and 0 <= nx < len(board[0]) and 0 <= ny < len(board) and new_board[ny][nx] == stone:
            for cx, cy in captured:
                new_board[cy][cx] = stone


    return new_board


def minimax(board, stone, depth, maximizing_player):
    """
    Minimaxアルゴリズムによる最適手の探索。
    board: 現在のボード
    stone: プレイヤーの石
    depth: 探索の深さ
    maximizing_player: 現在のプレイヤーが最大化プレイヤーかどうか
    return: 評価値
    """
    if depth == 0 or not can_place(board, stone):
        return evaluate_position(board, stone)


    if maximizing_player:
        max_eval = -float('inf')
        for y in range(len(board)):
            for x in range(len(board[0])):
                if can_place_x_y(board, stone, x, y):
                    new_board = simulate_move(board, stone, x, y)
                    eval = minimax(new_board, 3 - stone, depth - 1, False)
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for y in range(len(board)):
            for x in range(len(board[0])):
                if can_place_x_y(board, stone, x, y):
                    new_board = simulate_move(board, stone, x, y)
                    eval = minimax(new_board, 3 - stone, depth - 1, True)
                    min_eval = min(min_eval, eval)
        return min_eval


def best_place(board, stone):
    """
    Minimaxアルゴリズムを使用して最適な石の配置を決定する関数。
    board: 2次元配列のオセロボード
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    return: 最適な座標 (x, y)
    """
    best_score = -float('inf')
    best_move = None


    for y in range(len(board)):
        for x in range(len(board[0])):
            if can_place_x_y(board, stone, x, y):
                new_board = simulate_move(board, stone, x, y)
                score = minimax(new_board, 3 - stone, 3, False)  # 深さ3で探索
                if score > best_score:
                    best_score = score
                    best_move = (x, y)


    return best_move


class Be_good_ZoshigayaAI(object):


    def face(self):
        return "😻"  # 強い猫の絵文字


    def place(self, board, stone):
        move = best_place(board, stone)
        if move:
            return move
        else:
            raise ValueError("置ける場所がありません！")


# テスト用
if __name__ == "__main__":
    board = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 2, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]


    ai = StrongCatAI()
    stone = BLACK
    print("StrongCatAI's face:", ai.face())
    x, y = ai.place(board, stone)
    print(f"StrongCatAI places at: ({x}, {y})")
from kogi_canvas import play_othello, PandaAI


BLACK=1
WHITE=2


board = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,2,0,0],
        [0,0,2,1,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
]


play_othello(StrongCatAI())  






!rm -rf arupanda # データを消す
!git clone https://github.com/airpurin/Be_good_Zoushigaya
from Be_good_Zoushigaya.ai import StrongCatAI  # 自分のAIをインポートする
print(StrongCatAI().face())

