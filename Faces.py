"""
Created on 9/18/23
@author: christiankirby
"""
"""
Christian Kirby cdk37
"""
import random

def faces_fixed():
    """group of 3 faces doesn't change each time"""
    glasses_face()
    suprised_face()
    smiling_face()

    return

def faces_selfie():
    """prints 3 faces with selfie band"""
    for i in range(3):
        hairfunc(1)
        print(selfie_band())
        eyefunc(4)
        nosefunc(1)
        mouthfunc(3)
    return
def faces_random():
    for i in range(3):
        face_random()
def face_random():
    """
    Returns a random face everytime based on numbers provided by the random
    function
    """
    x = random.randint(1,5)
    if x == 1:
        print(face_with_glasses())
    elif x == 2:
        print(face_with_spikyhair())
    elif x == 3:
        print(face_with_leftnose())
    elif x == 4:
        print(face_with_linemouth(mouthfunc))
    else:
        print(face_with_openmouth())

    face_with_mouth(part_mouth_open)
    return
def suprised_face():
    "Returns a string of a surprised face"
    hairfunc(1)
    eyefunc(4)
    nosefunc(3)
    mouthfunc(1)
    return

def glasses_face():
    "Returns a string of a face with glasses"
    hairfunc(2)
    eyefunc(2)
    nosefunc(2)
    mouthfunc(3)
    return
def smiling_face():
    "Returns a string if a face that is smiling"
    hairfunc(2)
    eyefunc(3)
    nosefunc(1)
    mouthfunc(3)
    return
def hairfunc(x):
    "A functiion that will return a string of a hair type"
    if x == 1:
        print(part_hair_spikey())
    elif x == 2:
        print(part_hair_curly())
    elif x == 3:
        print(part_hair_straight())
    return
def eyefunc(x):
    "A function that will return a string of an eye tyoe"
    if x == 1:
        print(part_eye_lookleft())
    elif x == 2:
        print(part_eye_glassses())
    elif x == 3:
        print(part_eye_withbrows())
    elif x == 4:
        print(part_eye_suprised())
    return
def mouthfunc(x):
    "A function that will return a string of a mouth type"
    if x == 1:
        print(part_mouth_open())
    elif x == 2:
        print(part_mouth_line())
    elif x == 3:
        print(part_mouth_smile())
    return
def nosefunc(x):
    "A function that will return a string of a nose type"
    if x == 1:
        print(part_nose_pointyleft())
    elif x == 2:
        print(part_nose_pointyright())
    elif x == 3:
        print(part_nose_up())
    elif x == 4:
        print(part_nose_down())
    return
def part_hair_spikey():
    "A function that will return a string of spiky hair"
    a1  = '012345678901234567'
    a2  = ' /\/\/\/\/\/\/\/\ ' + "\n"
    a2 += ' /\/\/\/\/\/\/\/\ '
    return a2
def part_hair_curly():
    "A function that will return a string of curly hair"
    b1 = '012345678901234567'
    b2 = ' ???????????????? '
    return b2
def part_hair_straight():
    "A function that will return a string of straight hair"
    c1  =  r'012345678901234567'
    c2  =  r' |||||||||||||||| ' + "\n"
    c2  += r' |||||||||||||||| '
    return c2
def part_eye_glassses():
    "A function that will return a string of glasses"
    d1  = '012345678901234567'
    d2  = r" |  ___   ___   | " + "\n"
    d2 += r" | / / \_/ / \  | " + "\n"
    d2 += r" || /   _ /   | | " + "\n"
    d2 += r" | \___/ \___/  | "
    return d2
def part_eye_lookleft():
    "A function that will return a string of eyes looking left"
    e1  = r'012345678901234567'
    e2  = r" |  ___    ___  | " + "\n"
    e2 += r" | /   \  /   \ | " + "\n"
    e2 += r" || 0   || 0   || " + "\n"
    e2 += r" | \___/  \___/ | "

    return e2
def part_eye_withbrows():
    "A functon that will return a string of eyes with eyebrows"
    f1  = r"012345678901234567"
    f2  = r" |  ___    ___  | " + "\n"
    f2 += r" |  ___    ___  | " + "\n"
    f2 += r" | /  0\  /  0\ | " + "\n"
    f2 += r" | \___/  \___/ | "
    return f2
def part_eye_suprised():
    "A function that will return a string with surprised eyes"
    g1  = r"012345678901234567"
    g2  = r" |  ___    ___  | " + "\n"
    g2 += r" | /   \  /   \ | " + "\n"
    g2 += r" ||  0  ||  0  || " + "\n"
    g2 += r" | \___/  \___/ | "

    return g2
def part_mouth_open():
    "A function that will return a string with an open mouth"
    h1  = r"012345678901234567"
    h2  = r" |    ______    | " + "\n"
    h2 += r" |   /      \   | " + "\n"
    h2 += r" |  |        |  | " + "\n"
    h2 += r" |   \______/   | " + "\n"
    h2 += r" +--------------+ "
    return h2
def part_mouth_smile():
    "A functon that will return a string with of a smiling mouth"
    i1   = r"012345678901234567"
    i2   = r" |              | " + "\n"
    i2  += r" |   \______/   | " + "\n"
    i2  += r" +--------------+ "
    return i2
def part_mouth_line():
    "A function that will return a string with a straight line"
    j1  = r"012345678901234567"
    j2  = r" |              | " + "\n"
    j2 += r" |    ______    | " + "\n"
    j2 += r" +--------------+ "
    return j2
def part_nose_pointyleft():
    "A function that will return a string with a left pointing nose"
    k1  = r"012345678901234567"
    k2  = r" |      /       | " + "\n"
    k2 += r" |     /        | " + "\n"
    k2 += r" |    /____     | "
    return k2
def part_nose_pointyright():
    "A function that will return a string with a right pointing nose"
    l1  = r"012345678901234567"
    l2  = r" |      \       | " + "\n"
    l2 += r" |       \      | " + "\n"
    l2 += r" |    ____\     | "
    return l2
def part_nose_up():
    "A function that will return a string with a nose pointing up"
    m1  = r"012345678901234567"
    m2  = r" |      /\      | " + "\n"
    m2 += r" |     /  \     | " + "\n"
    m2 += r" |    /    \    | "
    return m2
def part_nose_down():
    "A function that will return a string with a nose pointing down"
    n1  = r"012345678901234567"
    n2  = r" |    \    /    | " + "\n"
    n2 += r" |     \  /     | " + "\n"
    n2 += r" |      \/      | "
    return n2

def selfie_band():
    m1  = r"012345678901234567"
    m2  = r" +--------------+ " + "\n"
    m2 += r" |cdk37    cdk37| " + "\n"
    m2 += r" +--------------+ "
    return m2

def face_with_spikyhair():
    hairfunc(1)
    eyefunc(1)
    nosefunc(1)
    mouthfunc(3)
def face_with_glasses():
    hairfunc(2)
    eyefunc(2)
    nosefunc(1)
    mouthfunc(3)
def face_with_leftnose():
    hairfunc(2)
    eyefunc(2)
    nosefunc(1)
    mouthfunc(3)
def face_with_openmouth():
    hairfunc(1)
    eyefunc(2)
    nosefunc(1)
    mouthfunc(1)
def face_with_linemouth(mouthfunc):
    hairfunc(3)
    eyefunc(2)
    nosefunc(1)
    print(mouthfunc(2))
def face_with_surprisedeyes(eyefunc):
    hairfunc(1)
    print(part_mouth_open())
    nosefunc(1)
    mouthfunc(1)
def face_with_mouth(part_mouth_open):
    hairfunc(1)
    eyefunc(1)
    nosefunc(1)
    print(part_mouth_open())

def face_with_hair(hairfunc):
    hairfunc()
    part_eye_suprised()
    part_nose_up()
    part_mouth_open()
def faces_random():
    "A function that will return a string of a nose type"
    x= random.randint(1,3)
    hairfunc = part_hair_spikey
    if x == 1:
        hairfunc = part_hair_spikey
    elif x == 2:
        hairfunc = part_hair_curly
    elif x == 3:
        hairfunc = part_hair_straight
    face_random()
    face_with_hair(hairfunc)
    return

if __name__ == '__main__':
    print(faces_fixed())
    print(faces_selfie())
    print(faces_random())

