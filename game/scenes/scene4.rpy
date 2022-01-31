screen scene4_1(zoom=None):
    zorder 100
    use overlay()

    if zoom is None:

        add "scene4_1_dirtywall"

        imagebutton:
            align(.8, .1)
            idle "scene3_1_pics"
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('scene4_1', dissolve), Show('scene4_1', zoom=1)

        imagebutton:
            align(.9, .9)
            idle 'scene3_1_girltoy'
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('scene4_1', dissolve), Show('scene4_1', zoom=2)

        imagebutton:
            align(.3, .5)
            idle 'scene4_1_door'
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('scene4_1', dissolve), Return()
    elif zoom == 1:
        add "scene4_1_dirtywall" xalign 0.85 zoom 2

        imagebutton:
            align(.5, .5)
            at transform:
                zoom 2.0
            idle "scene3_1_pics"
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('scene4_1', dissolve), Show('scene4_1')
    elif zoom == 2:
        add "scene4_1_dirtywall" align(1.0, .9) zoom 2

        imagebutton:
            align(.5, .5)
            at transform:
                zoom 2.0
            idle "scene3_1_girltoy"
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('scene4_1', dissolve), Show('scene4_1')
