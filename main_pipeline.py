from client.UTILS.lib import pygame, chess
from client.UTILS.controller import *


from stockfish import Stockfish

stockfish=Stockfish("./Stockfish/stockfish-windows-x86-64-avx2.exe",
                   parameters={
            #"Write Debug Log": "false",
            "Contempt": 0,
            "Min Split Depth": 0,
            "Threads": 8,
            "Ponder": "false",
            "Hash": 16,
            "MultiPV": 1,
            "Skill Level": 20,
            "Move Overhead": 30,
            "Minimum Thinking Time": 20,
            "Slow Mover": 80,
            "UCI_Chess960": "false",
            "UCI_LimitStrength": "false",
            "UCI_Elo": 1350,
        })
stockfish.set_depth(20)
stockfish.set_skill_level(20)
#stockfish.set_thread(8)
stockfish.get_parameters()



def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("체스 GUI (기물 점수 막대 포함)")
    board = chess.Board()
    load_piece_images("./client/PIECES")

    selected_square = None
    running = True
    clock = pygame.time.Clock()

    # 게임 실행
    while running:
        draw_board(screen, board)
        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get(): # 이벤트가 발생했을때 
            if event.type == pygame.QUIT: # 종료 이벤트가 발생
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN: # 클릭 이벤트
                clicked_square = get_square_under_mouse(pygame.mouse.get_pos()) # 클릭한 위치의 사각형을 가져옴
                if clicked_square is None:  # 클릭한 사각형이 비어있을 경우 스킵
                    continue
                if selected_square is None: # 이전에 클릭한 기물이 없을 경우
                    #  지금 클릭한 기물이 있고              지금 클릭한 기물의 색이 턴에 맞는지 체크
                    if board.piece_at(clicked_square) and board.piece_at(clicked_square).color == board.turn:
                        selected_square = clicked_square # 클릭한 기물을 저장
                else: # 이전에 클릭한 기물이 있을 경우
                    move = chess.Move(selected_square, clicked_square) # 기물의 이동을 시도
                    if move in board.legal_moves: # 기물 이동이 정상적인 이동인가?
                        board.push(move) # 정상이라면 수행
                    selected_square = None #초기화
        
        
        
        # 게임 오버 체크
        if board.is_checkmate():
            print(f"{'BLACK' if board.turn else 'WHITE'} checkmate")
            break
        if board.is_stalemate():
            print(f"{'BLACK' if board.turn else 'WHITE'} stalemate")
            break
        if board.is_check():
            print(f"{'BLACK' if board.turn else 'WHITE'} check")
            

        
    pygame.quit()

if __name__ == "__main__":
    main()