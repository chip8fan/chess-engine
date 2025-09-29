import pygame
import sys
import chess
import engine
import chess.engine
font_size = 16
time_limit = 10
screen_size = 512, 512+(font_size*2)
piece_size = (64, 64)
pygame.init()
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Chess Engine Match")
board = chess.Board()
files = list("ABCDEFGH")
chess_board = pygame.transform.scale(pygame.image.load("svg/board.png"), (512, 512))
white_pawn = pygame.transform.scale(pygame.image.load("svg/wP.svg"), piece_size)
white_knight = pygame.transform.scale(pygame.image.load("svg/wN.svg"), piece_size)
white_bishop = pygame.transform.scale(pygame.image.load("svg/wB.svg"), piece_size)
white_rook = pygame.transform.scale(pygame.image.load("svg/wR.svg"), piece_size)
white_queen = pygame.transform.scale(pygame.image.load("svg/wQ.svg"), piece_size)
white_king = pygame.transform.scale(pygame.image.load("svg/wK.svg"), piece_size)
black_pawn = pygame.transform.scale(pygame.image.load("svg/bP.svg"), piece_size)
black_knight = pygame.transform.scale(pygame.image.load("svg/bN.svg"), piece_size)
black_bishop = pygame.transform.scale(pygame.image.load("svg/bB.svg"), piece_size)
black_rook = pygame.transform.scale(pygame.image.load("svg/bR.svg"), piece_size)
black_queen = pygame.transform.scale(pygame.image.load("svg/bQ.svg"), piece_size)
black_king = pygame.transform.scale(pygame.image.load("svg/bK.svg"), piece_size)
font = pygame.font.SysFont('Arial', font_size)
running = True
chess_engine = engine.Engine()
stockfish = chess.engine.SimpleEngine.popen_uci("/opt/homebrew/bin/stockfish")
elo = 1350
stockfish.configure({'UCI_Elo': elo})
while running:
    screen.fill("white")
    screen.blit(font.render(f'Stockfish {elo}', True, 'black'), (0, 0))
    screen.blit(font.render('Selfmade Engine', True, 'black'), (0, font_size+512))
    screen.blit(chess_board, (0, font_size))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            stockfish.quit()
            pygame.quit()
    for _ in range(len(files)):
        for rank in range(8):
            square = eval(f"chess.{files[_]+str(rank+1)}")
            coordinate = eval(f"({(_%8)*64}, {512-((rank+1)*64)+font_size})")
            if board.piece_at(square) == chess.Piece.from_symbol("p"):
                screen.blit(black_pawn, coordinate)
            elif board.piece_at(square) == chess.Piece.from_symbol("n"):
                screen.blit(black_knight, coordinate)
            elif board.piece_at(square) == chess.Piece.from_symbol("b"):
                screen.blit(black_bishop, coordinate)
            elif board.piece_at(square) == chess.Piece.from_symbol("r"):
                screen.blit(black_rook, coordinate)
            elif board.piece_at(square) == chess.Piece.from_symbol("q"):
                screen.blit(black_queen, coordinate)
            elif board.piece_at(square) == chess.Piece.from_symbol("k"):
                screen.blit(black_king, coordinate)
            elif board.piece_at(square) == chess.Piece.from_symbol("P"):
                screen.blit(white_pawn, coordinate)
            elif board.piece_at(square) == chess.Piece.from_symbol("N"):
                screen.blit(white_knight, coordinate)
            elif board.piece_at(square) == chess.Piece.from_symbol("B"):
                screen.blit(white_bishop, coordinate)
            elif board.piece_at(square) == chess.Piece.from_symbol("R"):
                screen.blit(white_rook, coordinate)
            elif board.piece_at(square) == chess.Piece.from_symbol("Q"):
                screen.blit(white_queen, coordinate)
            elif board.piece_at(square) == chess.Piece.from_symbol("K"):
                screen.blit(white_king, coordinate)
    pygame.display.flip()
    if board.is_game_over() == False and board.can_claim_draw() == False:
        if board.turn == chess.WHITE:
            board.push_uci(chess_engine.search(board, time_limit))
        elif board.turn == chess.BLACK:
            board.push(stockfish.play(board, chess.engine.Limit(time=time_limit)).move)
    else:
        if board.result() == "1-0":
            elo += 50
            board = chess.Board()
            stockfish.configure({'UCI_Elo': elo})
    clock.tick(60)
print(elo)
sys.exit()