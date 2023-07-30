import pygame

class Play():
    """
    importiert alle Variablen
    """
    def __init__(self, display_surface):
        self.display_surface = display_surface

        self.play = True

    """
    generiert play button
    
    input: xpaider_pixel_explosion_02.ttf, self.display_surface
    
    output: self.display_surface, self.play
    """
    def play_button(self):

        # generiert button
        font1 = pygame.font.Font("grafik/xpaider_pixel_explosion_02.ttf", 60)
        text_surf1 = font1.render("Play", True, (0, 0, 0))
        text_rect1 = text_surf1.get_rect(center=(880, 200))
        self.display_surface.blit(text_surf1, text_rect1)

        # Logik + Ausführung button
        pos = pygame.mouse.get_pos()
        if text_rect1.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.play = False

    """
    update class

    output: self.play_button
    """
    def update(self):
        self.play_button()