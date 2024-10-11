import math

import mouse
import keyboard

global pos
pos = [0, 0]
def cursor(posx, posy, imx, imy):
    # x = posx/imx*2560
    # y = posy/imy*1600
    x = ((posx / 650) * 2560 * 2) - 2560 - 300
    y = ((posy/450) * 1600 * 2) - 1600 - 200
    dist = math.sqrt(abs(((posx - pos[0]) ^ 2) - ((posy - pos[1]) ^ 2)))
    if dist < math.sqrt(2):
        pass
    else:
        mouse.move(x, y - 500)
    pos.clear()
    pos.append(posx)
    pos.append(posy)

def click(dist_i_t):
    if dist_i_t < 4:
        mouse.click('left')
        time.sleep(0.2)

def scroll(dist_m_t):
    if dist_m_t <= 4:
        mouse.press('left')
    if dist_m_t > 4:
        mouse.release('left')