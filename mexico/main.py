"""Main game file for Mexico."""

import sys
import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCALE_FACTOR = 8
FPS = 60


def run_game() -> None:
    """Run the main game loop."""

    # Setup the game clock
    clock = pygame.time.Clock()

    # Setup the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mexico")

    # Load, convert and scale images
    dice_sheet_image = pygame.image.load("graphics/pngs/dice-sheet.png").convert_alpha()
    dice_sheet_scaled = pygame.transform.scale_by(dice_sheet_image, SCALE_FACTOR)

    # Initialize game variables
    is_dice_rolled = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        return
                    case pygame.K_SPACE:
                        is_dice_rolled = True

        # Game logic goes here
        screen.fill((100, 100, 100))
        if is_dice_rolled:
            screen.blit(dice_sheet_scaled, (SCREEN_WIDTH / 6, SCREEN_HEIGHT / 4))

        pygame.display.update()  # TODO: check pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    pygame.init()
    try:
        run_game()
    except Exception as e:
        print(f"An error occurred while running the game: {e}")
        raise
    finally:
        pygame.quit()
        sys.exit()
