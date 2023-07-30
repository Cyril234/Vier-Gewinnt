import pygame


class Player():
    """
    importiert alle Variablen
    """
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.pos_spielsteine = [0, 0, 0, 0, 0, 0, 0,  # Eine Liste zur Verfolgung der Positionen der Spielsteine
                                0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0]
        self.pos_anzeiger = 75
        self.pos_input = [False, False, False, False, False, False, False]
        self.geklickt = False
        self.wer_dran = 1

    """
    detektiert input Maus
    
    input: Mausinput (linke Maustaste)
    
    output: self.pos_anzeiger, self.pos_input
    """
    def input_zeiger(self):
        pos = pygame.mouse.get_pos()

        # Setzt die Position des Zeigers basierend auf der Mausposition
        if pygame.Rect(30, 30, 700, 600).collidepoint(pos):
            if pos[0] < 130:
                self.pos_anzeiger = 75
            elif pos[0] < 230:
                self.pos_anzeiger = 175
            elif pos[0] < 330:
                self.pos_anzeiger = 275
            elif pos[0] < 430:
                self.pos_anzeiger = 375
            elif pos[0] < 530:
                self.pos_anzeiger = 475
            elif pos[0] < 630:
                self.pos_anzeiger = 575
            elif pos[0] < 730:
                self.pos_anzeiger = 675

            # Aktiviert die Eingabe für den Spielstein
            if pygame.mouse.get_pressed()[0]:
                if pos[0] < 130:
                    self.pos_input[0] = True
                elif pos[0] < 230:
                    self.pos_input[1] = True
                elif pos[0] < 330:
                    self.pos_input[2] = True
                elif pos[0] < 430:
                    self.pos_input[3] = True
                elif pos[0] < 530:
                    self.pos_input[4] = True
                elif pos[0] < 630:
                    self.pos_input[5] = True
                elif pos[0] < 730:
                    self.pos_input[6] = True

            # Deaktiviert die Eingabe für alle Spielsteine, wenn die linke Maustaste nicht gedrückt ist
            else:
                self.pos_input[0] = False
                self.pos_input[1] = False
                self.pos_input[2] = False
                self.pos_input[3] = False
                self.pos_input[4] = False
                self.pos_input[5] = False
                self.pos_input[6] = False

    """
    konvertiert self.pos_input zu zal in self.pos_spielsteine
    
    input self.pos_input, self.wer_dran, self.geklickt, self.pos_spielsteine
    
    output: self.pos_spielsteine
    """
    def output(self):
        if self.geklickt == False:

            # Geht alle Kombinationen durch
            for horizontal_number in range(7):
                if self.pos_input[horizontal_number]:
                    spielstein_am_boden = True
                    for vertical_number in range(0, 42, 7):

                        # Überpüft, ob auf der oberen Achse kein Spielstein ist und auf der unteren Achse einer ist
                        if self.pos_spielsteine[horizontal_number + vertical_number] != 0 and \
                                self.pos_spielsteine[horizontal_number + vertical_number - 7] == 0:
                            self.pos_spielsteine[horizontal_number + vertical_number - 7] = self.wer_dran
                            spielstein_am_boden = False
                            self.pos_input[horizontal_number] = False
                            self.geklickt = True

                            # Ändert den Spieler, der an der Reihe ist
                            if self.wer_dran == 1:
                                self.wer_dran = 2
                            else:
                                self.wer_dran = 1
                            break

                        elif self.pos_spielsteine[horizontal_number + vertical_number] != 0 and \
                                self.pos_spielsteine[horizontal_number + vertical_number - 7] != 0:
                            break

                    # Wenn der Spielstein auf der untersten Achse gelandet ist
                    if spielstein_am_boden:
                        if self.pos_spielsteine[horizontal_number + 35] == 0:
                            self.pos_spielsteine[horizontal_number + 35] = self.wer_dran
                            self.pos_input[horizontal_number] = False
                            self.geklickt = True

                            # Ändert den Spieler, der an der Reihe ist
                            if self.wer_dran == 1:
                                self.wer_dran = 2
                            else:
                                self.wer_dran = 1

                    # Setzt Eingabe zurück
                    self.pos_input[horizontal_number] = False

        elif not pygame.mouse.get_pressed()[0]:
            self.geklickt = False

    """
    update class
    """
    def update(self):
        pygame.draw.rect(self.display_surface, (110, 0, 0), pygame.Rect(self.pos_anzeiger, 5, 20, 20))
        self.input_zeiger()
        self.output()