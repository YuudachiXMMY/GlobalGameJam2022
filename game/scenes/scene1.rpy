define bird_actions = ['scene1_1_bird', 'scene1_1_bird_sing', 'scene1_1_bird_move']
default touch_times = 0
default accounting_re = 10

screen scene1_1(re=False, touched=False, bird_rand= renpy.random.randint(1, 3)):
    zorder 100
    use overlay

    add "scene1_1_bg"
    add "scene1_1_phone_bottom"

    if not re and touch_times > 5:
        add "scene1_1_phone_top"
        timer 0.5 action Show("ringTone", message="............", time=20)
    elif bird_rand == 1:
        imagebutton:
            idle "scene1_1_phone_top_animated"
            action Play('sound', 'audio/Wood_dig1.ogg'), Show("ringTone", message="Play with the Bird......")
    elif bird_rand == 2:
        imagebutton:
            idle "scene1_1_phone_top_animated"
            action Play('sound', 'audio/Wood_dig1.ogg'), Show("ringTone", message="This Bird looks Fun...")
    else:
        imagebutton:
            idle "scene1_1_phone_top_animated"
            action Play('sound', 'audio/Wood_dig1.ogg'), Show("ringTone", message="Tweet, tweet, tweet...")

    if not re and touch_times > 5:
        imagebutton:
            align(.22, .3)
            idle 'scene1_1_bird_deads'
            action Play('sound', 'audio/Wood_dig1.ogg'), Hide('scene1_1', dissolve), Return()
    else:
        imagebutton:
            align(.22, .3)
            if not touched:
                idle str(bird_actions[0])
            else:
                idle str(bird_actions[renpy.random.randint(1, 2)])
            if not re and touch_times >= 5:
                action Play('sound', 'audio/mice.ogg'), SetVariable("touch_times", touch_times+1), Hide('scene1_1'), Show('scene1_1', touched=True)
            else:
                action Play('sound', 'audio/bird.ogg'), SetVariable("touch_times", touch_times+1), Hide('scene1_1'), Show('scene1_1',re=re, touched=True)
    # add "scene1_1_phone_top_animated"
    if re:
        timer 3 action Hide('scene1'), Show('final_screen')

screen final_screen():
    zorder 900
    modal True
    add "black"
    add "final":
        anchor(0, 0) pos(-5, -5) zoom 1.0
        at transform:
            linear 10 pos(0, 0) zoom 0.486
            linear 30 ypos -3720

screen ringTone(message='', time=7):
    zorder 201
    if renpy.get_screen('scene1_1'):
        add "scene1_1_phone_text_bg":
            align(.55, .2)
            yzoom .5
            at transform:
                alpha 0.5
                linear time*0.8/3 alpha 1.0
                linear time*0.2/3 alpha 0.5
                repeat

        text str(message):
            align(.65, .2)
            size 36
            font '经典中圆简.ttf'
            color '#101010'
            bold True
            if time < 10:
                at transform:
                    alpha 0.5
                    linear time*0.8/3 alpha 1.0
                    linear time*0.2/3 alpha 0.5
                    repeat
            else:
                at transform:
                    alpha 0.5
                    linear time*0.8/8 alpha 1.0
                    linear time*0.2/8 alpha 0.5
                    repeat

        timer time action Play('sound', 'audio/Wood_dig1.ogg'), Hide('ringTone', dissolve)

# Not Used
screen scene1_2():
    zorder 100
    use overlay

    # add "bg2"