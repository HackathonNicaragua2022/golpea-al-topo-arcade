def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    simplified.move_to_random_hole_on_grid(myMole)
    music.ba_ding.play()
    animation.run_image_animation(myHammer,
        assets.animation("""
            hammerAnimation
        """),
        50,
        False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

myHammer: Sprite = None
myMole: Sprite = None
game.show_long_text("Bienvenido al juego de Hackathon Nicaragua 2023",
    DialogLayout.BOTTOM)
game.show_long_text("Inicia tu aventura en la jungla donde deberás vencer a un temible topo",
    DialogLayout.BOTTOM)
scene.set_background_image(assets.image("""
    grid
"""))
myMole = sprites.create(assets.image("""
    mole
"""), SpriteKind.enemy)
myHammer = sprites.create(assets.image("""
    hammer
"""), SpriteKind.player)
simplified.move_only_onscreen_with_arrows(myHammer, simplified.Speeds.FAST)
carnival.start_countdown_game(15, carnival.WinTypes.SCORE)
carnival.add_label_to("Golopea al Topo", carnival.Areas.BOTTOM)

def on_update_interval():
    simplified.move_to_random_hole_on_grid(myMole)
game.on_update_interval(1000, on_update_interval)

def on_update_interval2():
    pass
game.on_update_interval(500, on_update_interval2)
