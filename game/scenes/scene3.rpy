default s3_b_car = False
default s3_b_game = False

screen scene3_1(zoom=None):
    zorder 100
    use overlay('scene3_1', 'scene3_2')

    if zoom is None:
        add "bg1"

        imagebutton:
            align(.8, .1)
            idle "scene3_1_pics"
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('scene3_1', dissolve), Show('scene3_1', zoom=1)

        imagebutton:
            align(.1, .9)
            idle 'scene3_1_girltoy'
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('scene3_1', dissolve), Show('scene3_1', zoom=2)

        imagebutton:
            if not s3_b_car:
                align(.8, .95)
                idle 'scene3_1_car'
                action Play('sound', 'audio/Wood_dig1.ogg'), SetVariable('s3_b_car', True), Hide('scene3_1', dissolve), Show('scene3_1')
            else:
                align(.6, .95)
                idle 'scene3_1_car_b'
                action Play('sound', 'audio/Wood_dig1.ogg')

        imagebutton:
            if not s3_b_game:
                align(.8, .98)
                idle 'scene3_1_game'
                action Play('sound', 'audio/Wood_dig1.ogg'), SetVariable('s3_b_game', True), Hide('scene3_1', dissolve), Show('scene3_1')
            else:
                align(.85, .98)
                idle 'scene3_1_game_b'
                action Play('sound', 'audio/Wood_dig1.ogg')

    elif zoom == 1:
        add "bg1" xalign 0.85 zoom 2

        imagebutton:
            align(.5, .5)
            at transform:
                zoom 2.0
            idle "scene3_1_pics"
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('scene3_1', dissolve), Show('scene3_1')
    elif zoom == 2:
        add "bg1" align(0, .9) zoom 2

        imagebutton:
            align(.5, .5)
            at transform:
                zoom 2.0
            idle "scene3_1_girltoy"
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('scene3_1', dissolve), Show('scene3_1')



screen scene3_2(stage=0):
    zorder 100
    use overlay('scene3_1', 'scene3_2')

    add "bg2" zoom 1.5 align(.5,.5)

    if stage == 0:
        add "bg2"
        imagebutton:
            align(.5, .4)
            idle 'scene3_1_w'+str(stage)
            action Play('sound', 'audio/Wood_dig1.ogg'), Show('scene3_2', stage=1)
    elif stage == 1:
        imagebutton:
            align(.5, .4)
            idle 'scene3_1_w'+str(stage)
            action Play('sound', 'audio/Wood_dig1.ogg'), Show('scene3_2', stage=2)
    elif stage == 2:
        imagebutton:
            align(.5, .4)
            idle 'scene3_1_w'+str(stage)
            action Play('sound', 'audio/Wood_dig1.ogg'), Show('scene3_2', stage=3)
    elif stage == 3:
        imagebutton:
            align(.5, .4)
            idle 'scene3_1_w'+str(stage)
            action Play('sound', 'audio/Wood_dig1.ogg'), Show('scene3_2', stage=4)
    elif stage == 4:
        imagebutton:
            align(.5, .4)
            idle 'scene3_1_w'+str(stage)
            action Play('sound', 'audio/Wood_dig1.ogg'), Show('scene3_2', stage=5)
    else:
        imagebutton:
            align(.5, .4)
            idle 'scene3_1_w'+str(stage)
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('scene3_2', dissolve), Return()