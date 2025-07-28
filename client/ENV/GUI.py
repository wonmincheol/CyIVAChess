from client.UTILS.lib import os, pygame, chess

# Pygame 기본 설정
WIDTH, HEIGHT = 660, 640
SQ_SIZE = (WIDTH-20) // 8
# 색상 정의
WHITE = (240, 217, 181)
BROWN = (181, 136, 99)

# 기물 이미지 매핑 (파일명은 "wp.png", "bk.png" 등으로 저장돼야 함)
PIECE_IMAGES = {}


PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 10,
    chess.KING: 0
}


def load_piece_images(folder_path):
    '''
    기물 이미지 로드
    args:
        folder_path : str, 이미지 파일이 들어있는 경로
    '''
    pieces = ['p', 'n', 'b', 'r', 'q', 'k']
    colors = ['w', 'b']
    for color in colors:
        for piece in pieces:
            filename = f"{color}{piece}.png"
            path = os.path.join(folder_path, filename)
            image = pygame.image.load(path)
            PIECE_IMAGES[f"{color}{piece}"] = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))



def evaluate_material_ratio(board):
    white_score, black_score = 0, 0 # 스코어 초기화
    for square in chess.SQUARES: # 모든 사각형 탐색
        piece = board.piece_at(square) # 사각형위에 피스를 가져옴
        if piece: # 피스가 있을 경우
            value = PIECE_VALUES[piece.piece_type] # 피스의 가치를 가져옴
            if piece.color == chess.WHITE: # 피스의 색을 구분
                white_score += value # 피스 가치 합
            else:
                black_score += value #피스 가치합
    total = white_score + black_score
    return (black_score / total, white_score / total) if total > 0 else (0.5, 0.5)

def draw_score_bar(screen, board, stockfish_score):
    '''
    좌측에 흑(상단)/백(하단) 기물 점수 비율 막대 출력
    args:
        screen : pygame의 UI
        board : 체스보드
        stockfish_score : stockfish 평가 점수
    '''
    bar_x = 0
    bar_width = 20
    # black_ratio, white_ratio = evaluate_material_ratio(board)
    black_ratio = (1000-stockfish_score)/2000
    
    '''
    점수 계산을 어떻게 해야할까?
    
    입력 : stockfish점수(centipawn, -1000~+1000) or 메이트까지 남은 수

    

    출력 : -10~+10
    
    '''

    black_height = int(HEIGHT * black_ratio)
    white_height = HEIGHT - black_height

    # 검은색 상단
    pygame.draw.rect(screen, (0, 0, 0), (bar_x, 0, bar_width, black_height))
    # 흰색 하단
    pygame.draw.rect(screen, (255, 255, 255), (bar_x, black_height, bar_width, white_height))



def draw_board(screen, board, stockfish_score):
    """
    체스 보드를 출력
    args:
        \nscreen : pygame 스크린
        \nboard : chess라이브러리의 board
        \nstockfish_score : stockfish 평가 점수
    """
    draw_score_bar(screen, board, stockfish_score)
    font = pygame.font.SysFont('Arial', 16)

    for rank in range(8):
        for file in range(8):
            square = chess.square(file, 7 - rank)
            color = WHITE if (rank + file) % 2 == 0 else BROWN
            x = file * SQ_SIZE + 20  # 보드 왼쪽에 점수 막대가 있어서 +20
            y = rank * SQ_SIZE
            pygame.draw.rect(screen, color, pygame.Rect(x, y, SQ_SIZE, SQ_SIZE))

            piece = board.piece_at(square)
            if piece:
                color = 'w' if piece.color == chess.WHITE else 'b'
                symbol = piece.symbol().lower()
                image = PIECE_IMAGES[f"{color}{symbol}"]
                screen.blit(image, (x, y))
        # 왼쪽 숫자 좌표 (8~1)
        label = font.render(str(8 - rank), True, (0, 0, 0))
        screen.blit(label, (22, rank * SQ_SIZE + 5))
    # 아래쪽 알파벳 좌표 (a~h)
    for file in range(8):
        label = font.render(chr(ord('a') + file), True, (0, 0, 0))
        screen.blit(label, (file * SQ_SIZE + 25, HEIGHT - 20))  # x좌표는 +20 보정됨

def get_square_under_mouse(pos):
    x, y = pos
    if x < 20:  # 점수 막대 클릭 무시
        return None
    file = (x - 20) // SQ_SIZE
    rank = 7 - (y // SQ_SIZE)
    return chess.square(file, rank)