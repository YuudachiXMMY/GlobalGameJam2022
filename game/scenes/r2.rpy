screen r2_1(stage=0):
    zorder 100
    use overlay()

    add "bg1"

    add 'r2_bed' align(.1, .9)

    add "r2_deak2"
    add "scene1_1_phone_bottom"
    if stage < 5:
        add "scene1_1_phone_top"

    if stage >= 0:
        imagebutton:
            align(.15, .2)
            idle 'r2_pic0'
            if stage == 0:
                action Play('sound', 'audio/Wood_dig1.ogg'), Show('r2_1', stage=1)
            else:
                action Play('sound', 'audio/Wood_dig1.ogg'), NullAction()
    if stage >= 1:
        imagebutton:
            align(.33, .2)
            idle 'r2_pic1'
            if stage == 1:
                action Play('sound', 'audio/Wood_dig1.ogg'), Show('r2_1', stage=2)
            else:
                action Play('sound', 'audio/Wood_dig1.ogg'), NullAction()
    if stage >= 2:
        imagebutton:
            align(.45, .2)
            idle 'r2_pic2'
            if stage == 2:
                action Play('sound', 'audio/Wood_dig1.ogg'), Show('r2_1', stage=3)
            else:
                action Play('sound', 'audio/Wood_dig1.ogg'), NullAction()
    if stage >= 3:
        imagebutton:
            align(.6, .2)
            idle 'r2_pic3'
            if stage == 3:
                action Play('sound', 'audio/Wood_dig1.ogg'), Show('r2_1', stage=4)
            else:
                action Play('sound', 'audio/Wood_dig1.ogg'), NullAction()
    if stage >= 4:
        imagebutton:
            align(.86, .2)
            idle 'r2_pic4'
            if stage == 4:
                action Play('sound', 'audio/Wood_dig1.ogg'), Show('r2_1', stage=5)
            else:
                action Play('sound', 'audio/Wood_dig1.ogg'), NullAction()

    if stage >= 5:
        add "scene1_1_phone_bottom"
        imagebutton:
            idle "scene1_1_phone_top_animated"
            action Hide("r2_1", dissolve), Return()