import numpy as np
import glm

class Pyramid:
    def __init__(self, position=(0,0,0), rotation=(0,0,0), scale=(1,1,1), name="pyramid"):
        self.name = name
        self.position = glm.vec3(*position)
        self.rotation = glm.vec3(*rotation)
        self.scale = glm.vec3(*scale)

        # vértices (x,y,z,r,g,b)
        self.vertices = np.array([
            # base
            -0.5, 0.0, -0.5,  1.0, 0.0, 0.0,  # V0 rojo
             0.5, 0.0, -0.5,  0.0, 1.0, 0.0,  # V1 verde
             0.5, 0.0,  0.5,  0.0, 0.0, 1.0,  # V2 azul
            -0.5, 0.0,  0.5,  1.0, 1.0, 0.0,  # V3 amarillo

            # ápice
             0.0, 1.0,  0.0,  1.0, 0.0, 1.0   # V4 magenta
        ], dtype=np.float32)

        # índices → base (dos triángulos) + caras laterales
        self.indices = np.array([
            # base (cuadrado)
            0, 1, 2,
            0, 2, 3,

            # lados (4 triángulos)
            0, 1, 4,
            1, 2, 4,
            2, 3, 4,
            3, 0, 4
        ], dtype=np.uint32)

    def get_model_matrix(self):
        model = glm.mat4(1)
        model = glm.translate(model, self.position)
        model = glm.rotate(model, glm.radians(self.rotation.x), glm.vec3(1, 0, 0))
        model = glm.rotate(model, glm.radians(self.rotation.y), glm.vec3(0, 1, 0))
        model = glm.rotate(model, glm.radians(self.rotation.z), glm.vec3(0, 0, 1))
        model = glm.scale(model, self.scale)
        return model