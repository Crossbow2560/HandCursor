import keyboard
import time
import mouse

scroll_stat = 0
center = [1280, 800]
def click(distance, click_stat):
    click_previous = click_stat
    click_stat = 0
    if distance < 3 and click_stat == 0:
        click_stat = 1
        keyboard.press('space')
        time.sleep(1)
        keyboard.release('space')
    if click_previous != click_stat:
        time.sleep(1)
    print(click_stat)

def cursor(posx, posy, distance, home, distance_scroll):
    global scroll_stat, scrollchange, initial_pos
    x = posx/650*2560 - 300
    y = posy/450*1600 - 500
    print(x, y)
    mouse.move(x, y)
    if distance < 3.5:
        mouse.click('left')
        time.sleep(0.2)
    try:
        if distance_scroll < 4:
            scroll_stat = True
        if distance_scroll > 4:
            scroll_stat = False
        if scroll_stat:
            if initial_pos - posy > 0 and scroll_stat:
                mouse.drag(x, y, x, y + 100, absolute=True)
    except:
        pass

