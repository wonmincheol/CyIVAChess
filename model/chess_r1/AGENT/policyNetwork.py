from client.UTILS.lib import pygame, chess




def load_pgn():
    '''
    pgn 확장자에서 기보를 가져온다

    # pgn read
    https://python-chess.readthedocs.io/en/latest/pgn.html
    # chess games
    https://www.chess.com/games
    '''
    pass

def pgn_to_board(pgn):
    board = chess.Board()
    


    return board




def generate_Model():
    model = None


    return model




class policyNetwork:
    '''
    policy network
    프로 체스 선수의 기보를 지도학습하여 수의 가치를 계산
    '''

    
    def __init__(self):
        self.model = generate_Model()
        pass
    def cal(board,move):
        '''
        args:
            board : 현재 보드 상황
            move : 현재 시도한 수
        '''
        pass