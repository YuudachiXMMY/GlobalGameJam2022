define narrator = Character(None, kind=nvl)


label start:

    $ touch_times = 0
    $ stage = 1
    $ wstage = 1
    $ accounting_re = 10

    $ s3_b_car = False
    $ s3_b_game = False

    # Scene 1
    play music 'audio/pre.ogg'
    queue music 'audio/body.ogg'

    show screen overlay()
    call screen scene1_1() with dissolve
    hide screen overlay

    scene black with dissolve
    narrator 'IS IT ...'
    nvl clear
    'DEAD {w}?'

    # Scene 2
    show screen overlay('scene2_1', 'scene2_2') with dissolve
    call screen scene2_1() with dissolve
    hide screen overlay

    nvl clear
    scene black with dissolve
    narrator 'EVERYTHING{p}WILL BE ...{p}GOOD{w}, RIGHT?'

    # Scene 3
    show screen overlay('scene3_1', 'scene3_2')
    call screen scene3_1() with dissolve
    hide screen overlay

    nvl clear
    scene black with dissolve
    narrator 'IS HE ...'

    # Scene 4
    play music 'audio/body_under.ogg'
    show screen overlay()
    call screen scene4_1() with dissolve
    hide screen overlay

    nvl clear
    scene black with Dissolve(3)
    narrator 'I HAVE TO{p}LEAVE.'
    nvl clear
    scene black with Dissolve(3)
    narrator '......'

    # Scene R1
    show screen overlay()
    call screen r1_1() with dissolve
    hide screen overlay

    nvl clear
    scene black with Dissolve(3)
    narrator 'WHERE\nIS\nTHIS PLACE?'
    nvl clear
    scene black with Dissolve(3)
    narrator 'IT LOOKS LIKE ...{p}ANOTHER{p}ME{w}?'
    nvl clear
    scene black with Dissolve(3)
    narrator 'THE {w}REAL {w}ME{w} ?'

    # Scene R2
    show screen overlay
    call screen r2_1() with dissolve
    hide screen overlay

    nvl clear
    scene black with Dissolve(3)
    narrator '......'
    nvl clear
    scene black with Dissolve(3)
    narrator 'THAT WAS{p}MY BROTHER {w}?'

    # Scene R3
    queue music 'audio/body.ogg'
    show screen overlay('r3_1', 'r3_2')
    call screen r3_1() with dissolve
    hide screen overlay

    nvl clear
    scene black with Dissolve(3)
    narrator 'THAT WAS{p}MY MOTHER {w}?'
    nvl clear
    scene black with Dissolve(3)
    narrator '......'
    nvl clear
    scene black with Dissolve(3)
    narrator 'THIS{w} WAS{w} ALSO{p}MY LIFE{w} ?'
    nvl clear
    scene black with Dissolve(3)
    narrator '......'
    nvl clear
    scene black with Dissolve(3)
    narrator 'MAYBE{p}I NEED TO{p}GO BACK{p}HOME{w} ?'

    scene black with Dissolve(3)
    call screen scene1_1(re=True) with dissolve

    return
