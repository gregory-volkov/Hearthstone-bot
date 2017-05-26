import win32api, win32gui, win32con, math, time
from Classes import *
from random import randint


def GetCursorPosition():
    flags, hcursor, (x, y) = win32gui.GetCursorInfo()
    return Point(x, y)


def SetCursorPos(p):
    win32api.SetCursorPos(((int(round(p.x))), int(round(p.y))))
    return


def LinearSmoothMove(newPosition, steps):
    start = GetCursorPosition()
    iterPoint = start

    # Find the slope of the line segment defined by start and newPosition
    slope = Point(newPosition.x - start.x, newPosition.y - start.y)

    # Divide by the number of steps
    slope.x = slope.x / steps
    slope.y = slope.y / steps

    # Move the mouse to each iterative point.
    for i in range(steps):
        iterPoint = Point(iterPoint.x + slope.x, iterPoint.y + slope.y)
        SetCursorPos(iterPoint)
        time.sleep(0.02)

    # Move the mouse to the final destination.
    SetCursorPos(newPosition)
    return


def SendClick():
    p = GetCursorPosition()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, p.x, p.y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, p.x, p.y, 0, 0)


def GetHSRect():
    def enumHandler(hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd):
            if 'Hearthstone' == win32gui.GetWindowText(hwnd):
                global t
                t = win32gui.GetWindowRect(hwnd)

    win32gui.EnumWindows(enumHandler, None)
    return Rect(t)


def MoveTo(X, Y):
    rectHS = GetHSRect()
    windowWidth = rectHS.right - rectHS.left
    uiHeight = rectHS.bottom - rectHS.top
    uiWidth = ((uiHeight) / 3) * 4

    xOffset = (windowWidth - uiWidth) / 2  # ' The space on the side of the game UI

    endX = (X / 100.0) * uiWidth + xOffset + rectHS.left
    endY = (Y / 100.0) * uiHeight + rectHS.top + 8
    p = Point(endX, endY)
    LinearSmoothMove(p, 50) # randint(30, 150)


def ClickOn(X, Y):
    MoveTo(X, Y)
    time.sleep(randint(5, 20))
    SendClick()


def MoveToCard(hand_size, cardNum):
    handwidth = 0
    if (hand_size < 4):
        handwidth = 10 * hand_size
    else:
        handwidth = 38
    x = (((cardNum * 1.0) / (hand_size)) * handwidth) - (handwidth / 2.0) - 0.8
    y = (x * -0.16) * (x * -0.16)
    MoveTo(x + 44, y + 89)

def MoveBetweenMinions(totalMinions, minionNum):
    minionWidth = 29 / 3.0
    totalWidth = totalMinions * minionWidth
    minionX = (minionNum * minionWidth) - (minionWidth / 2)
    cursorX = 50 - (totalWidth / 2) + minionX
    MoveTo(cursorX - 4, 55)

def MoveToMinion(totalMinions, minionNum):
    if minionNum == 0:
        MoveTo(50, 76)
        return
    minionWidth = 29 / 3.0
    totalWidth = totalMinions * minionWidth
    minionX = (minionNum * minionWidth) - (minionWidth / 2)
    cursorX = 50 - (totalWidth / 2) + minionX
    MoveTo(cursorX, 55)

def MoveToOpponentMinion(totalMinions, minionNum):
    if minionNum == 0:
        MoveTo(50, 20)
        return
    minionWidth = 29 / 3.0
    totalWidth = totalMinions * minionWidth
    minionX = (minionNum * minionWidth) - (minionWidth / 2)
    cursorX = 50 - (totalWidth / 2) + minionX
    MoveTo(cursorX, 40)


def MoveToBattleField():
    MoveTo(50,50)