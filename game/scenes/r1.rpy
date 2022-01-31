screen r1_1(stage=1):
    zorder 100
    use overlay()

    add "bg1"

    if stage == 1:
        imagebutton:
            align(.5, .9)
            idle 'toy_bear'
            action Play('sound', 'audio/Wood_dig1.ogg'), Show('r1_mv1'), Show('r1_1', stage=2)
    elif stage == 2:
        imagebutton:
            align(.5, .9)
            idle 'toy_bear2'
            action Play('sound', 'audio/Wood_dig1.ogg'), Show('r1_mv2'), Show('r1_1', stage=3)
    elif stage == 3:
        imagebutton:
            align(.5, .85)
            idle 'cage'
            action Play('sound', 'audio/Wood_dig1.ogg'), Show('r1_mv3'), Show('r1_1', stage=4)
    elif stage == 4:
        imagebutton:
            align(.5, .9)
            idle 'toy_bear'
            action Play('sound', 'audio/Wood_dig1.ogg'), Show('r1_mv4'), Show('r1_1', stage=5)
    elif stage == 5:
        imagebutton:
            align(.5, .9)
            idle 'toy_bear2'
            action Play('sound', 'audio/Wood_dig1.ogg'), Show('r1_mv5'), Show('r1_1', stage=6)
    else:
        imagebutton:
            align(.5, .9)
            idle 'r3_bear_broken2'
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('r1_1', dissolve), Return()

