from pygame import mixer

DAMAGE_SOUND = "invasao-alien/sounds/damage.mp3"
SHOT_SOUND = "invasao-alien/sounds/shot.mp3"

def tocar_som(caminho):
    som = mixer.Sound(caminho)
    som.play()