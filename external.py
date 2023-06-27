from item import Planet
import pygame

def main():
    run = True
    clock = pygame.time.Clock()
    Planet.scale = 13 / Planet.AU

    sun = Planet(0, 0, 30, Planet.YELLOW, 1.98892 * 10**30)
    sun.sun = True

    jupyter = Planet(5.2 * Planet.AU, 0, 20, Planet.BROWN, 1.898 * 10**27)
    jupyter.y_vel = 13.1 * 1000


    saturn = Planet(9.53 * Planet.AU, 0, 18, Planet.GREEN, 5.69 * 10**26)
    saturn.y_vel = 9.69 * 1000


    uranus = Planet(19.1 * Planet.AU, 0, 14, Planet.BLUE, 8.7 * 10**25)
    uranus.y_vel = 6.81 * 1000


    neptune = Planet(30 * Planet.AU, 0, 14, Planet.DARK_GREY, 1.03 * 10**26)
    neptune.y_vel = 5.43 * 1000


    planets = [sun, jupyter, saturn, uranus, neptune]


    while run:
        clock.tick(60)
        Planet.WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(Planet.WIN)

        pygame.display.update()

    pygame.quit()

main()

