@namespace
class SpriteKind:
    disableed = SpriteKind.create()

def on_overlap_tile(sprite3, location3):
    scene.set_background_image(assets.image("""
        background2
    """))
    tiles.set_tilemap(tilemap("""
        level4
    """))
    animation.run_movement_animation(mySprite,
        animation.animation_presets(animation.fly_to_center),
        1000,
        False)
    mySprite.say("Level 3", 500)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        chest2
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite6, location6):
    tiles.set_wall_at(location6, True)
    tiles.set_wall_at(location6, True)
scene.on_overlap_tile(SpriteKind.projectile,
    assets.tile("""
        bounce
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite4, location4):
    scene.set_background_image(assets.image("""
        background2
    """))
    tiles.set_tilemap(tilemap("""
        level2
    """))
    animation.run_movement_animation(mySprite,
        animation.animation_presets(animation.fly_to_center),
        2000,
        False)
    mySprite.say("Level 2", 500)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        chest1
    """),
    on_overlap_tile3)

def on_a_pressed():
    simplified.gravity_jump(mySprite)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile4(sprite, location):
    tiles.set_tile_at(location, assets.tile("""
        transparency16
    """))
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        orange bauble
    """),
    on_overlap_tile4)

def on_left_pressed():
    animation.run_image_animation(mySprite, assets.animation("""
        walk left
    """), 150, True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_b_pressed():
    tiles.set_wall_at(tiles.location_in_direction(tiles.location_of_sprite(mySprite),
            CollisionDirection.BOTTOM),
        True)
    tiles.set_tile_at(tiles.location_in_direction(tiles.location_of_sprite(mySprite),
            CollisionDirection.BOTTOM),
        assets.tile("""
            bounce
        """))
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        assets.animation("""
            walk right
        """),
        150,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_overlap_tile5(sprite5, location5):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        poison pit
    """),
    on_overlap_tile5)

def on_overlap_tile6(sprite2, location2):
    tiles.set_wall_at(location2, True)
    tiles.set_wall_at(location2, True)
scene.on_overlap_tile(SpriteKind.projectile,
    assets.tile("""
        skyblock
    """),
    on_overlap_tile6)

def on_overlap_tile7(sprite7, location7):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        chest3
    """),
    on_overlap_tile7)

mySprite: Sprite = None
scene.set_background_image(assets.image("""
    background
"""))
tiles.set_tilemap(tilemap("""
    level1
"""))
mySprite = sprites.create(assets.image("""
    stand
"""), SpriteKind.player)
controller.move_sprite(mySprite, 100, 0)
mySprite.ay = 500
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.ONE),
    sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . 3 . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player))
scene.camera_follow_sprite(mySprite)
animation.run_image_animation(mySprite, assets.animation("""
    jump
"""), 100, False)