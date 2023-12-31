import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.transform.flip(pg.image.load("ex01/fig/3.png"), True, False)
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 5, 1.0), pg.transform.rotozoom(kk_img, 10, 1.0), 
               pg.transform.rotozoom(kk_img, 5, 1.0), pg.transform.rotozoom(kk_img, 0, 1.0)]
    tmr = 0
    x = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = (tmr - x) % 1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [1600-x, 0])
        
        screen.blit(kk_imgs[tmr%5], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(500)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()