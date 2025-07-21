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