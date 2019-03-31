import pygame,sys
pygame.init()
font = pygame.font.SysFont("Arial", 20)
screen=pygame.display.set_mode((640, 480))
def welcomepage():
    bx = 640
    by = 480
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (150, 150, 150)
    box = pygame.surface.Surface((bx, by)) 
    box.fill(GREY)
    pygame.draw.rect(box, WHITE, (50, 12, bx-100, 35), 0)
    pygame.draw.rect(box, WHITE, (50, by-60, bx-100, 42), 0)
    pygame.draw.rect(box, BLACK, (0, 0, bx, by), 1)
    txt_surf = font.render("WELCOME TO SAVE THE CASTLE!!!", True, BLACK)  
    txt_rect = txt_surf.get_rect(center=(bx//2, 30))
    box.blit(txt_surf, txt_rect)
    txt_surf = font.render("USE ARROW KEYS TO NAVIGATE, MOUSE TO ROTATE,", True, BLACK)  
    txt_rect = txt_surf.get_rect(center=(bx//2, 120))
    box.blit(txt_surf, txt_rect)
    txt_surf = font.render("LEFT-CLICK TO SHOOT!! KILL THE BADGERS ", True, BLACK)  
    txt_rect = txt_surf.get_rect(center=(bx//2, 150))
    box.blit(txt_surf, txt_rect)
    txt_surf = font.render("BEFORE THEY TAKE OVER THE CASTLES.", True, BLACK)  
    txt_rect = txt_surf.get_rect(center=(bx//2, 180))
    box.blit(txt_surf, txt_rect)
    txt_surf = font.render("HURRY!!!", True, BLACK)  
    txt_rect = txt_surf.get_rect(center=(bx//2, 220))
    box.blit(txt_surf, txt_rect)
    txt_surf = font.render("Press ENTER to PLAY!!!", True, BLACK)  
    txt_rect = txt_surf.get_rect(center=(bx//2, 360))
    box.blit(txt_surf, txt_rect)
    screen.blit(box, (0, 0))
    pygame.display.flip()
    while True:  # wait for user to acknowledge and return
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                return
        pygame.time.wait(20)
