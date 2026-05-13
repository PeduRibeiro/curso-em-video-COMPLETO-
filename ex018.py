import math
angulo = float(input('Digite um angulo: '))
sin = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('Sendo {}° o seu angulo, temos como seno {:.2f}°, cosseno{:.2f}°, tangente{:.2f}°,' .format(angulo, sin, cos, tan))