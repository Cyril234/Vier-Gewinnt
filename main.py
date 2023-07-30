import pygame
from winning import *
from player import *
from play import *

# Standard Bildschirmeinstellungen
pygame.init()
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
display_surface = pygame.display.set_mode((1000, 660), pygame.RESIZABLE)
pygame.display.set_caption("Vier gewinnt")

# Erstellt die Objekte
winning = Winning(display_surface)
player = Player(display_surface)
play = Play(display_surface)

wer_dran = 1

pos = [0, 0, 0, 0, 0, 0, 0,  # Eine Liste zur Verfolgung der Positionen der Spielsteine
       0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0,]

"""
zeichnet Spielsteine

input: pos, display_surface

output: display_surface
"""
def draw_circle():
    circle_pos_y = 0
    for horizontal_number in range(0, 42, 7): # Abfrage horizontale Linie
        if not horizontal_number == 0:
            circle_pos_y += 100

        circle_pos_x = 0
        for vertical_number in range(7): # Abfrage vertikale Linie
            if not vertical_number == 0:
                circle_pos_x += 100
            if pos[horizontal_number + vertical_number] != 0:
                if pos[horizontal_number + vertical_number] == 1:
                    pygame.draw.circle(display_surface, (0, 0, 0), (80 + circle_pos_x, 80 + circle_pos_y), 40)
                else:
                    pygame.draw.circle(display_surface, (140, 31, 11), (80 + circle_pos_x, 80 + circle_pos_y), 40)

"""
Main loop: Alle Logik dieses ganzen Games läuft in diesem loop zusammen.
Ausser die loops vom Start und nachdem man gestorben ist: Diese laufen in ihren jeweiligen classes ab.
"""
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill((245, 241, 225))

    pygame.draw.rect(display_surface, (66, 57, 19), pygame.Rect(30, 30, 700, 600))  # Zeichnet das Spielbrett

    # Aktiviert classes und tauscht Variablen zwischen den classes aus
    if not play.play:
        player.update()
        pos = player.pos_spielsteine
        winning.wer_dran = player.wer_dran
        winning.pos = pos
        winning.update()
        pos = winning.pos
        player.pos_spielsteine = pos
        player.wer_dran = winning.wer_dran
    else:
        play.update()

    # Zeichnet leere Kreise als Platzhalter für Spielsteine
    circle_pos_y = 0
    for horizontal_number in range(0, 42, 7):
        if not horizontal_number == 0:
            circle_pos_y += 100

        circle_pos_x = 0
        for vertical_number in range(7):
            if not vertical_number == 0:
                circle_pos_x += 100
            pygame.draw.circle(display_surface, (245, 241, 225), (80 + circle_pos_x, 80 + circle_pos_y), 40)

    draw_circle()

    pygame.display.update()