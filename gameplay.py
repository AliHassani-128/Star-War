import pygame
import test


def game(w, h):

    bullets = []
    enemys = []
    pygame.init()
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Star Wars')
    background = pygame.image.load('pictures/background.png')
    ship = test.Spaceship(screen)
    gameover = False
    for i in range(9):
        bullet = test.Bullet(screen, ship)
        bullet.bullet_y += i*60
        bullets.append(bullet)
        enemy = test.Enemy(screen)
        enemy.enemy_y -= i*100
        enemys.append(enemy)
    score = 0
    while True:
        screen.blit(background, (0, 0))
        ship.move(bullets[0])
        ship.show()
        for i in range(len(bullets)):
            bullets[i].move(ship)
            bullets[i].show()
            enemys[i].move()
            enemys[i].show()
            for enemy in enemys:
                bullets[i].crash(enemy)
                if enemy.crash == True:
                    score = enemy.score(score)
        #test.show_text(screen, "Score:"+str(score), (0, 0))
        pygame.display.update()


game(600, 600)
