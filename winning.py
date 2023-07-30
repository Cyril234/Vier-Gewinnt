import pygame, sys

class Winning():
    """
    importiert alle Variablen
    """
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.pos = [0, 0, 0, 0, 0, 0, 0, # Position Spielsteine
                    0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0]

        self.winning = False
        self.unentschieden_winning = False
        self.unentschieden = 0

        self.display_surface = display_surface
        self.wer_dran_winning_algorithmus = 1
        self.wer_dran = 1
        self.winning_text = ""

    """
    algorithmus ob jemand gewonnen hat
    
    input: self.pos, self.wer_dran, self.wer_dran_winning_algorithmus, self.unentschieden
    
    output: self.winning, self.unentschieden_winning
    """

    def winningalgorithm(self):

        # wiederholung des ganzen Algorithmus für Rot/Schwarz
        for winning_algorithm in range(2):
            self.wer_dran_winning_algorithmus = winning_algorithm + 1

            #vertical_row
            for horizontal_number in range(0, 42, 7):
                for vertical_number in range(4):
                    if self.pos[horizontal_number + vertical_number] == self.wer_dran_winning_algorithmus and \
                            self.pos[horizontal_number + vertical_number + 1] == self.wer_dran_winning_algorithmus and \
                            self.pos[horizontal_number + vertical_number + 2] == self.wer_dran_winning_algorithmus and \
                            self.pos[horizontal_number + vertical_number + 3] == self.wer_dran_winning_algorithmus:
                        for o in range(4):
                            if self.wer_dran == 1:
                                self.pos[horizontal_number + vertical_number + o] = 3
                            else:
                                self.pos[horizontal_number + vertical_number + o] = 4
                        self.winning = True

            #horizontal_row
            for horizontal_number in range(7):
                for vertical_number in range(0, 21, 7):
                    if self.pos[horizontal_number + vertical_number] == self.wer_dran_winning_algorithmus and \
                            self.pos[horizontal_number + vertical_number + 7] == self.wer_dran_winning_algorithmus and \
                            self.pos[horizontal_number + vertical_number + 14] == self.wer_dran_winning_algorithmus and \
                            self.pos[horizontal_number + vertical_number + 21] == self.wer_dran_winning_algorithmus:
                        for o in range(0,28,7):
                            if self.wer_dran == 1:
                                self.pos[horizontal_number + vertical_number + o] = 3
                            else:
                                self.pos[horizontal_number + vertical_number + o] = 4
                        self.winning = True

            #diagonal_45°
            for horizontal_number in range(0, 21, 7):
                for vertical_number in range(4):
                    if self.pos[horizontal_number + vertical_number] == self.wer_dran_winning_algorithmus and \
                            self.pos[horizontal_number + vertical_number + 8] == self.wer_dran_winning_algorithmus and \
                            self.pos[horizontal_number + vertical_number + 16] == self.wer_dran_winning_algorithmus and \
                            self.pos[horizontal_number + vertical_number + 24] == self.wer_dran_winning_algorithmus:
                        for o in range(0, 32, 8):
                            if self.wer_dran == 1:
                                self.pos[horizontal_number + vertical_number + o] = 3
                            else:
                                self.pos[horizontal_number + vertical_number + o] = 4
                        self.winning = True

            #diagonal_135°
            for horizontal_number in range(0, 21, 7):
                for vertical_number in range(3,7):
                    if self.pos[horizontal_number + vertical_number] == self.wer_dran_winning_algorithmus and \
                            self.pos[horizontal_number + vertical_number + 6] == self.wer_dran_winning_algorithmus and \
                            self.pos[horizontal_number + vertical_number + 12] == self.wer_dran_winning_algorithmus and \
                            self.pos[horizontal_number + vertical_number + 18] == self.wer_dran_winning_algorithmus:
                        for o in range(0, 24, 6):
                            if self.wer_dran == 1:
                                self.pos[horizontal_number + vertical_number + o] = 3
                            else:
                                self.pos[horizontal_number + vertical_number + o] = 4
                        self.winning = True

            # algorithmus unentschieden
            for unentschieden_algorithmus in range(42):
                if self.pos[unentschieden_algorithmus] == 0:
                    break

                elif self.unentschieden == 42:
                    self.unentschieden_winning = True

                else:
                    self.unentschieden += 1

    """
    loop für front/backend, nachdem jemand gewonnen hat, bis restart
    
    input: font(xpaider_pixel_explosion_02.ttf), self.winning_text, self.display_surface, self.poss
    
    output: self.pos, self.winning, self.wer_dran, self.unentschieden, self.unentschieden_winning
    """

    def winning_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # generiert Text winning_text, replay
            font = pygame.font.Font("grafik/xpaider_pixel_explosion_02.ttf", 30)
            text_surf = font.render(self.winning_text, True, (0, 0, 0))
            text_rect = text_surf.get_rect(center=(880, 100))
            self.display_surface.blit(text_surf, text_rect)

            font1 = pygame.font.Font("grafik/xpaider_pixel_explosion_02.ttf", 30)
            text_surf1 = font1.render("replay", True, (0, 0, 0))
            text_rect1 = text_surf1.get_rect(center=(880, 200))
            self.display_surface.blit(text_surf1, text_rect1)

            # replay button Funktion + reset als Folge
            pos = pygame.mouse.get_pos()
            if text_rect1.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    self.pos = [0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0]
                    self.winning = False
                    self.wer_dran = 1
                    self.unentschieden = 0
                    self.unentschieden_winning = False
                    break

            # Spielfeld + Spielsteine zeichnen
            circle_pos_y = 0
            for horizontal_number in range(0, 42, 7):
                if not horizontal_number == 0:
                    circle_pos_y += 100

                circle_pos_x = 0
                for vertical_number in range(7):
                    if not vertical_number == 0:
                        circle_pos_x += 100
                    pygame.draw.circle(self.display_surface, (245, 241, 225), (80 + circle_pos_x, 80 + circle_pos_y), 40)

            circle_pos_y = 0
            for horizontal_number in range(0, 42, 7):
                if not horizontal_number == 0:
                    circle_pos_y += 100

                circle_pos_x = 0
                for vertical_number in range(7):
                    if not vertical_number == 0:
                        circle_pos_x += 100
                    if self.pos[horizontal_number + vertical_number] != 0:
                        if self.pos[horizontal_number + vertical_number] == 1:
                            pygame.draw.circle(self.display_surface, (0, 0, 0), (80 + circle_pos_x, 80 + circle_pos_y), 40)

                        elif self.pos[horizontal_number + vertical_number] == 2:
                            pygame.draw.circle(self.display_surface, (140, 31, 11), (80 + circle_pos_x, 80 + circle_pos_y), 40)

                        elif self.pos[horizontal_number + vertical_number] == 4:
                            pygame.draw.circle(self.display_surface, (0, 0, 0), (80 + circle_pos_x, 80 + circle_pos_y), 40)
                            pygame.draw.circle(self.display_surface, (38, 140, 31), (80 + circle_pos_x, 80 + circle_pos_y), 15)

                        else:
                            pygame.draw.circle(self.display_surface, (140, 31, 11), (80 + circle_pos_x, 80 + circle_pos_y), 40)
                            pygame.draw.circle(self.display_surface, (38, 140, 31), (80 + circle_pos_x, 80 + circle_pos_y), 15)

            pygame.display.update()

    """
    update class
    
    input: self.winningalgorithm, self.winning, self.unentschieden_winning, self.wer_dran
    
    output: self.winning_text, self.winning_screen, self.wer_dran_winning_algorithmus
    """
    def update(self):
        self.winningalgorithm()

        # Algorithmus, ob jemand gewonnen hat, wenn ja, wer + self.winning_screen aufrufen
        if self.winning or self.unentschieden_winning:
            if self.unentschieden_winning:
                self.winning_text = "unentschieden"
                self.winning_screen()


            else:
                if self.wer_dran == 2:
                    self.winning_text = "Black wins"
                    self.winning_screen()

                else:
                    self.winning_text = "Red wins"
                    self.winning_screen()

        self.wer_dran_winning_algorithmus = 2