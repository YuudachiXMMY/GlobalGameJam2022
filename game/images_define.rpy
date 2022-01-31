image bg1:
    'images/bg2.png'

image bg2:
    'images/bg1.png'

image black:
    'gui/black.png'

image toy_bear:
    'images/bear.png'

image toy_bear2:
    'images/bear2.png'

image cage:
    'images/cage.png'

image final:
    'images/final.png'

image logo:
    'gui/logo.png'

######################################################
# GUIs
image settings_btn_idle:
    'gui/settings/settings_btn_idle.png'

image settings_btn_hover:
    'gui/settings/settings_btn_hover.png'

image right_btn_idle:
    'gui/settings/right_btn_idle.png'

image right_btn_hover:
    'gui/settings/right_btn_hover.png'

image left_btn_idle:
    xzoom -1.0
    'right_btn_idle'

image left_btn_hover:
    xzoom -1.0
    'right_btn_hover'


######################################################
# Scene 1
image scene1_1_bg:
    'images/scene1_1/scene1_1.png'

# Bird
image scene1_1_bird_deads:
    'images/scene1_1/dead.png'

image scene1_1_bird:
    'images/scene1_1/bird_sing/1.png'

image scene1_1_bird_sing:
    'images/scene1_1/bird_sing/1.png'
    pause .2
    'images/scene1_1/bird_sing/2.png'
    pause .2
    'images/scene1_1/bird_sing/3.png'
    pause .2
    'images/scene1_1/bird_sing/4.png'
    pause .2
    'images/scene1_1/bird_sing/5.png'
    pause .2
    'images/scene1_1/bird_sing/4.png'
    pause .2
    'images/scene1_1/bird_sing/5.png'
    pause .2
    'images/scene1_1/bird_sing/4.png'
    pause .2
    'images/scene1_1/bird_sing/5.png'
    pause .2
    'images/scene1_1/bird_sing/4.png'
    pause .2
    'images/scene1_1/bird_sing/3.png'
    pause .2
    'images/scene1_1/bird_sing/2.png'
    pause .2
    'images/scene1_1/bird_sing/1.png'

image scene1_1_bird_move:
    'images/scene1_1/bird_o/0.png'
    pause 0.2
    'images/scene1_1/bird_o/1.png'
    pause 0.2
    'images/scene1_1/bird_o/2.png'
    pause 0.2
    'images/scene1_1/bird_o/3.png'
    pause 0.2
    'images/scene1_1/bird_o/2.png'
    pause 0.2
    'images/scene1_1/bird_o/1.png'
    pause 0.2
    'images/scene1_1/bird_o/0.png'
    pause 0.2
    'images/scene1_1/bird_o/0.png'
    pause 0.2
    'images/scene1_1/bird_o/1.png'
    pause 0.2
    'images/scene1_1/bird_o/2.png'
    pause 0.2
    'images/scene1_1/bird_o/3.png'
    pause 0.2
    'images/scene1_1/bird_o/2.png'
    pause 0.2
    'images/scene1_1/bird_o/1.png'
    pause 0.2
    'images/scene1_1/bird_o/0.png'
    pause 0.2


# Phone
image scene1_1_phone_bottom:
    'images/scene1_1/phone_bottom.png'

image scene1_1_phone_text_bg:
    'images/scene1_1/phone_text_bg.png'

image scene1_1_phone_top:
    'images/scene1_1/phone_top_1.png'

image scene1_1_phone_top_animated:
    'images/scene1_1/phone_top_1.png'
    pause 0.1
    'images/scene1_1/phone_top_0.9.png'
    pause 0.1
    'images/scene1_1/phone_top_0.8.png'
    pause 0.1
    'images/scene1_1/phone_top_0.9.png'
    pause 0.1
    'images/scene1_1/phone_top_1.1.png'
    pause 0.1
    'images/scene1_1/phone_top_1.1.png'
    pause 0.1
    'images/scene1_1/phone_top_1.2.png'
    pause 0.1
    'images/scene1_1/phone_top_1.1.png'
    pause 0.1
    repeat


######################################################
# Scene 2
image scene2_1_pics:
    'images/scene2_1/pics.png'

image scene2_1_paper:
    'images/scene2_1/paper.png'

image scene2_1_bed:
    'images/scene2_1/bed.png'

image scene2_1_desk:
    'images/scene2_1/desk.png'

image scene2_1_desk_open:
    'images/scene2_1/desk_open.png'

image scene2_1_desk_focus:
    'images/scene2_1/desk_focus.png'

image scene2_2_words1:
    zoom 0.05
    'images/scene2_1/s2_words/1.png'

image scene2_2_words2:
    zoom 0.05
    'images/scene2_1/s2_words/2.png'

image scene2_2_words3:
    zoom 0.05
    'images/scene2_1/s2_words/3.png'

######################################################
# Scene 3
image scene3_1_pics:
    'images/scene3_1/pics.png'

image scene3_1_window:
    'images/scene3_1/window.png'

image scene3_1_w0:
    'images/scene3_1/window/w0.png'

image scene3_1_w1:
    'images/scene3_1/window/w1.png'

image scene3_1_w2:
    'images/scene3_1/window/w2.png'

image scene3_1_w3:
    'images/scene3_1/window/w3.png'

image scene3_1_w4:
    'images/scene3_1/window/w4.png'

image scene3_1_w5:
    'images/scene3_1/window/w5.png'

image scene3_1_girltoy:
    'images/scene3_1/girltoy.png'

image scene3_1_car:
    'images/scene3_1/toys/car1.png'

image scene3_1_car_b:
    'images/scene3_1/toys/car2.png'

image scene3_1_game:
    'images/scene3_1/toys/control1.png'

image scene3_1_game_b:
    'images/scene3_1/toys/control2.png'


######################################################
# Scene 4
image scene4_1_dirtywall:
    'images/scene4_1/dirtywall.png'

image scene4_1_door:
    'images/scene4_1/door.png'


######################################################
# R 1
image r1_mv1 = Movie(play="images/r1_1/v/1.mpg", loop=False)

screen r1_mv1():
    zorder 500
    imagebutton:
        yalign 0.5
        idle "r1_mv1"
        action NullAction()

image r1_mv2 = Movie(play="images/r1_1/v/2.mpg", loop=False)

screen r1_mv2():
    zorder 500
    imagebutton:
        yalign 0.5
        idle "r1_mv2"
        action NullAction()

image r1_mv3 = Movie(play="images/r1_1/v/3.mpg", loop=False)

screen r1_mv3():
    zorder 500
    imagebutton:
        yalign 0.5
        idle "r1_mv3"
        action NullAction()

image r1_mv4 = Movie(play="images/r1_1/v/4.mpg", loop=False)

screen r1_mv4():
    zorder 500
    imagebutton:
        yalign 0.5
        idle "r1_mv4"
        action NullAction()

image r1_mv5 = Movie(play="images/r1_1/v/5.mpg", loop=False)

screen r1_mv5():
    zorder 500
    imagebutton:
        yalign 0.5
        idle "r1_mv5"
        action Hide('r1_mv1'), Hide('r1_mv2'), Hide('r1_mv3'), Hide('r1_mv4'), Hide('r1_mv5')


######################################################
# R 2
image r2_deak2:
    'images/r2_1/desk1.png'

image r2_pic0:
    zoom 0.4
    'images/r2_1/r2_0_1.png'
    pause 0.2
    'images/r2_1/r2_0_2.png'
    pause 0.2
    'images/r2_1/r2_0_3.png'
    pause 0.2
    'images/r2_1/r2_0_2.png'
    pause 0.2
    repeat

image r2_pic1:
    'images/r2_1/r2_1.png'

image r2_pic2:
    'images/r2_1/r2_2.png'

image r2_pic3:
    'images/r2_1/r2_3.png'

image r2_pic4:
    'images/r2_1/r2_4.png'

image r2_bed:
    'images/r2_1/bed_3.png'

######################################################
# R 3
image r3_1:
    'images/r3_1/blood.png'

image r3_bear_broken:
    'images/r3_1/broken_bear.png'

image r3_bear_broken2:
    xzoom -1.0
    'images/r3_1/broken_bear.png'

image r3_pic_broken:
    'images/r3_1/broken_pic.png'

image r3_emptybox:
    'images/r3_1/emptybox.png'