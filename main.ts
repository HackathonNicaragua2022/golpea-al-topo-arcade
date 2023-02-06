sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    info.changeScoreBy(1)
    simplified.moveToRandomHoleOnGrid(myMole)
    music.baDing.play()
    animation.runImageAnimation(myHammer, assets.animation`
            hammerAnimation
        `, 50, false)
})
let myHammer : Sprite = null
let myMole : Sprite = null
game.showLongText("Bienvenido al juego de Hackathon Nicaragua 2023", DialogLayout.Bottom)
game.showLongText("Inicia tu aventura en la jungla donde deberás vencer a un temible topo", DialogLayout.Bottom)
scene.setBackgroundImage(assets.image`
    grid
`)
myMole = sprites.create(assets.image`
    mole
`, SpriteKind.Enemy)
myHammer = sprites.create(assets.image`
    hammer
`, SpriteKind.Player)
simplified.moveOnlyOnscreenWithArrows(myHammer, simplified.Speeds.Fast)
carnival.startCountdownGame(15, carnival.WinTypes.Score)
carnival.addLabelTo("Golopea al Topo", carnival.Areas.Bottom)
game.onUpdateInterval(1000, function on_update_interval() {
    simplified.moveToRandomHoleOnGrid(myMole)
})
game.onUpdateInterval(500, function on_update_interval2() {
    
})
