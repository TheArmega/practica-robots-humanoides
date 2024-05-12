# practica-robots-humanoides

## Avance en el plano **sagital**
Para simular el avance del robot en el plano sagital he usado el archivo **limp2d_frontal**.
Dentro de este archivo se han modificado las siguientes sentencias para simular de manera correcta el balanceo:
```python
# linea 18 
HEIGHT = 0.2 * len("santillan")

# linea 29
ax.set_ylim(-0.1, 2)

# linea 41
self.zmp_y = [100, 300, 100, 300, 100, 300, 100, 300, 100]

# linea 42
k = 5

# linea 43
self.zmp_time_change = [
    24,
    29,
    31 + k,
    31 + k * 2,
    31 + k * 3,
    31 + k * 4,
    31 + k * 5,
    31 + k * 6,
    31 + k * 7,
]
```

Modificando estas sentencias conseguimos el siguiente resultado:

