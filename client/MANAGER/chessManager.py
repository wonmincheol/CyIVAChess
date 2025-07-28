from ..UTILS.lib import chess, math
import chess
import chess.engine

def turnover(board):
    '''
    턴을 넘길때 마다 호출되는 함수
    0 : 무승부
    -1 : 승패갈림
    1 : 이상없음
    
    '''
    check_s = check(board)
    if check_s:
        return -1
    draw_s = is_draw(board)
    if draw_s:
        return 0
    gameover_s = gameover(board)
    if gameover_s:
        return -1
    return 1

def gameover(board):
    board.is_game_over()


def is_draw(board):
    '''
    이 함수는 현재 보드 상태가 무승부 조건 중 하나에 해당하는지 판단합니다.
    args:
        board : chess.Board
    return:
        bool : 무승부이면 True
    '''
    if board.is_stalemate():
        print("스테일메이트")
    if board.is_insufficient_material():
        print("체크메이트 불가능한 기물 구성")
    # if board.can_claim_fifty_moves():
    #     print("50회 진행 무승부")
    # if board.can_claim_threefold_repetition():
    #     print("3회 반복 무승부")
    if board.is_seventyfive_moves():
        print("75수 반복 무승부")
    if board.is_fivefold_repetition():
        print("5회 반복 무승부")

    return (
        board.is_stalemate() 
        or board.is_insufficient_material() 
        # or board.can_claim_fifty_moves() 
        # or board.can_claim_threefold_repetition() 
        or board.is_seventyfive_moves() 
        or board.is_fivefold_repetition()
    )

def check(board):
    # 게임 오버 체크
    if board.is_checkmate():
        print(f"{'BLACK' if board.turn else 'WHITE'} checkmate")
        return True
    if board.is_stalemate():
        print(f"{'BLACK' if board.turn else 'WHITE'} stalemate")
        return True
    if board.is_check():
        print(f"{'BLACK' if board.turn else 'WHITE'} check")
        return False
    return False


def normalize_score(score_cp, cap=1000):
    '''
    Stockfish centipawn 점수를 0 ~ 1 사이로 정규화합니다.
    args:
        score_cp : int, centipawn 점수 (양수: 백 우위, 음수: 흑 우위)
        cap : int, 점수 제한을 위한 절댓값 최대값 (default=1000)
    return:
        float : 0.0 ~ 1.0 사이의 값 (0: 흑 우위, 1: 백 우위)
    '''
    score_cp = max(-cap, min(score_cp, cap))  # 점수 클리핑
    return (score_cp + cap) / (2 * cap)


def evaluate_position(stockfish_path, board):
    '''
    현재 체스 보드 상태를 stockfish로 평가해 점수를 반환
    args:
        stockfish_path : str, Stockfish 실행 파일 경로
        board : chess.Board, 평가할 보드
    return:
        score : int or str, 평가 점수(+ : 백 우세, - : 흑 우새)
    '''
    with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
        # 0.1초 또는 depth=12 정도의 평가
        info = engine.analyse(board, chess.engine.Limit(depth=12))
        score = info["score"]
        if score.is_mate():
            return f"Mate in {score.mate()}"
        print(f"stockfish score : {score.white()}")
        return score.white().score()
