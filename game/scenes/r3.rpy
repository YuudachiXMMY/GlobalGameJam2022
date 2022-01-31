screen r3_1(zoom=None):
    zorder 100
    use overlay('r3_1', 'r3_2')

    if zoom is None:
        add "r3_1"

        imagebutton:
            align(.88, .9)
            idle 'r3_bear_broken'
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('r3_1', dissolve), Show('r3_1', zoom=1)

        imagebutton:
            align(.28, .223)
            idle 'r3_pic_broken'
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('r3_1', dissolve), Show('r3_1', zoom=2)

    elif zoom == 1:
        add "r3_1" align(1.0, 1.0) zoom 2

        imagebutton:
            align(.7, .75)
            at transform:
                zoom 2.0
            idle "r3_bear_broken"
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('r3_1', dissolve), Show('r3_1')

    elif zoom == 2:
        add "r3_1" align(.14, .18) zoom 2

        imagebutton:
            align(.5, .5)
            at transform:
                zoom 2.0
            idle "r3_pic_broken"
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('r3_1', dissolve), Show('r3_1')

screen r3_2(zoom=None):
    zorder 100
    use overlay('r3_1', 'r3_2')

    if zoom is None:

        add "scene4_1_dirtywall"

        imagebutton:
            align(.8, .1)
            idle "scene3_1_pics"
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('r3_2', dissolve), Show('r3_2', zoom=1)

        imagebutton:
            align(.9, .9)
            idle 'r3_emptybox'
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('r3_2', dissolve), Show('r3_2', zoom=2)

        imagebutton:
            align(.15, .95)
            idle 'r3_bear_broken2'
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('r3_2', dissolve), Show('r3_2', zoom=3)

        imagebutton:
            align(.4, .5)
            idle 'scene4_1_door'
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('r3_2', dissolve), Return()
    elif zoom == 1:
        add "scene4_1_dirtywall" xalign 0.85 zoom 2

        imagebutton:
            align(.5, .5)
            at transform:
                zoom 2.0
            idle "scene3_1_pics"
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('r3_2', dissolve), Show('r3_2')
    elif zoom == 2:
        add "scene4_1_dirtywall" align(1.0, .9) zoom 2

        imagebutton:
            align(.5, .5)
            at transform:
                zoom 2.0
            idle "r3_emptybox"
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('r3_2', dissolve), Show('r3_2')
    elif zoom == 3:
        add "scene4_1_dirtywall" align(.1, 1.0) zoom 2

        imagebutton:
            align(.4, .8)
            at transform:
                zoom 2.0
            idle "r3_bear_broken2"
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('r3_2', dissolve), Show('r3_2')