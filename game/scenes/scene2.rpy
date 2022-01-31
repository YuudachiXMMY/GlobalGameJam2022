screen scene2_1(zoom=None):
    zorder 100
    use overlay('scene2_1', 'scene2_2')

    if zoom is None:
        add "bg1"

        imagebutton:
            align(.8, .1)
            idle "scene2_1_pics"
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('scene2_1', dissolve), Show('scene2_1', zoom=2.0)

        imagebutton:
            align(0.17, 0.98)
            idle "scene2_1_bed"
            action Play('sound', 'audio/Wood_dig1.ogg')
    else:
        add "bg1" xalign 0.85 zoom 2

        imagebutton:
            align(.5, .5)
            at transform:
                zoom 2.0
            idle "scene2_1_pics"
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('scene2_1', dissolve), Show('scene2_1')


screen scene2_2(stage=1, wstage=0):
    zorder 100
    use overlay('scene2_1', 'scene2_2')

    if wstage >= 3 and stage == 1:
        imagebutton:
            idle 'scene2_1_desk'
            action Play('sound', 'audio/Wood_dig1.ogg'), Show('scene2_2', stage=2, wstage=4)
    elif wstage >= 4 and stage == 2:
        imagebutton:
            idle 'scene2_1_desk_open'
            action Play('sound', 'audio/Wood_dig1.ogg'), Show('scene2_2', stage=3, wstage=4)
    elif wstage >= 4 and stage == 3:
        add 'scene2_1_desk_focus'
        imagebutton:
            align(.5, .7)
            idle 'scene2_1_paper'
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('scene2_2', dissolve), Return()

    if wstage < 3:
        imagebutton:
            idle 'scene2_1_desk'
            action Play('sound', 'audio/Wood_dig1.ogg'), Show('scene2_2', wstage=wstage+1)
    if wstage >= 1 and stage != 3:
        add 'scene2_2_words1' align(1.0, .93)
    if wstage >= 2 and stage != 3:
        add 'scene2_2_words2' align(.87, .72)
    if wstage >= 3 and stage != 3:
        add 'scene2_2_words3' align(.38, .85)