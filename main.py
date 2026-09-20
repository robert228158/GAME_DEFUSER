HEIGHT=450
WIDTH=450
defuse_flag=False
flag_hint=False
flag_hint2=False
mode='scene1'
numbers={'0':(220,370),'1':(181,332),'2':(218,328),'3':(254,326),'4':(179,293),'5':(217,290),'6':(252,289),'7':(178,257),'8':(213,254),'9':(247,252),'#':(255,365),'+':(182,372)}
numbers_Actors=[]
for n in '0123456789#+':
    numbers_Actors.append(Actor(f'num{n}',topleft=numbers[n]))
wires={'red':(199,211),'yellow':(194,268),'black':(253,282),'purple':(262,254)}
wires_Actors=[]
for key in wires.keys():
    wires_Actors.append(Actor(key,topleft=wires[key]))
cross_wires={'cross_red':(201,213),'cross_yellow':(193,267),'cross_black':(252,281),'cross_purple':(263,250)}
cross_wires_Actors=[]
cross_wires_Actors_draw=[]
for key in cross_wires.keys():
    cross_wires_Actors.append(Actor(key,topleft=cross_wires[key]))
scene=Actor(mode)
bomb=Actor('c4')
bomb2=Actor('c4_1',topleft=(194,282))
code=''
red_button=Actor('red_button',topleft=(77,188))
red_cross_button=Actor('red_cross_button',topleft=(48,91)) 
hint=Actor('hint',topleft=(85,30))
hint2=Actor('hint2',topleft=(85,15))
# defuse={'5':(78,85),'4':(78,85),'2':(78,85),'1':(78,85),'0':(78,85)}
# defuse_Actors=[]
# for d in '54210':
#     numbers_Actors.append(Actor(f'def{d}',topleft=numbers[n]))
defuse=Actor('defuse5',topleft=(78,85))

def draw():
    scene.draw()
    #bomb.draw()
    if mode=='scene1':
        bomb2.draw()
    if mode=='scene2':
        for n in numbers_Actors:
            n.draw()
        screen.draw.text(str(code),topleft=(151,183),fontsize=34,color='#000000',angle=3)
        red_button.draw()
        if flag_hint:
            hint.draw()
        if defuse_flag:
            defuse.draw()

    if mode=='scene3':
        red_cross_button.draw()
        if flag_hint2:
            hint2.draw()
        for w in wires_Actors:
            w.draw()
        for cw in cross_wires_Actors_draw:
            cw.draw()
    if mode=='scene_win':
        scene.draw()



def on_mouse_down(button,pos):
    global mode,code,flag_hint,defuse_flag,flag_hint2
    if mode=='scene1':
        if bomb2.collidepoint(pos):
            mode='scene2'
            scene.image=mode 
    if mode=='scene2':
        for i,num in enumerate(numbers_Actors):
            if num.collidepoint(pos):
                flag_hint=False
                if i==10:
                    code=''
                elif i==11:
                    if defuse_flag==False:
                        flag_hint=True
                    else:
                        defuse_flag=False
                        flag_hint=True
                else:
                    if len(code)<16:
                        code+=str(i)+' '
        if red_button.collidepoint(pos):
            if code=='1 2 3 4 5 6 7 8 ':
                flag_hint=False
                defuse_flag=True
                mode='scene3'
                scene.image='scene3'

    if mode=='scene3':
        if red_cross_button.collidepoint(pos):
            flag_hint2=True
        for w,wires in enumerate(wires_Actors):
            if wires.collidepoint(pos):
                flag_hint2=False
                if (cross_wires_Actors[w]) not in cross_wires_Actors_draw:
                    cross_wires_Actors_draw.append(cross_wires_Actors[w])
        if len(cross_wires_Actors_draw)==4:
            if [x.image for x in cross_wires_Actors_draw]==['cross_yellow', 'cross_black', 'cross_purple', 'cross_red']:
                scene.image='scene_win'
                mode='scene_win'
            else:
                scene.image='scene_lose'
                mode='scene_win'



