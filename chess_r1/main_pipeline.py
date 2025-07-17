from UTILS.lib import pygame, chess
from UTILS.controller import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("체스 GUI (기물 점수 막대 포함)")
    board = chess.Board()
    load_piece_images("./chess_r1/PIECES")

    selected_square = None
    running = True
    clock = pygame.time.Clock()

    while running:
        draw_board(screen, board)
        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked_square = get_square_under_mouse(pygame.mouse.get_pos())
                if clicked_square is None:
                    continue
                if selected_square is None:
                    if board.piece_at(clicked_square) and board.piece_at(clicked_square).color == board.turn:
                        selected_square = clicked_square
                else:
                    move = chess.Move(selected_square, clicked_square)
                    if move in board.legal_moves:
                        board.push(move)
                    selected_square = None

    pygame.quit()

if __name__ == "__main__":
    main()