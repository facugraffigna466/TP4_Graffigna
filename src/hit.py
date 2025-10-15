#hit.py

import glm

class Hit:
    def __init__(self, get_model_matrix, hittable = True):
        self.__model_matrix = get_model_matrix
        self.hittable = hittable

    @property
    def model_matrix(self):
        return self.__model_matrix()

    @property
    def position(self):
        m = self.model_matrix
        return glm.vec3(m[3].x, m[3].y, m[3].z)

    @property
    def scale(self):
        m = self.model_matrix
        return glm.vec3(glm.length(glm.vec3(m[0])),
                        glm.length(glm.vec3(m[1])),
                        glm.length(glm.vec3(m[2])))

    def check_hit(self, origin, direction):
        raise NotImplementedError("Subclasses should implement this method.")

# aca probe usar la de obb , le pedi al chat que me adapte esa funcion (HitboxOBB) y anduvo 

class HitBox(Hit):    
    def __init__(self, get_model_matrix, hittable = True):
        super().__init__(get_model_matrix, hittable)

    def check_hit(self, origin, direction):
        if not self.hittable:
            return False

       
        inv_model = glm.inverse(self.model_matrix)
        local_origin = inv_model * glm.vec4(origin, 1.0)
        local_dir = inv_model * glm.vec4(direction, 0.0)

       
        min_bound = glm.vec3(-1, -1, -1)
        max_bound = glm.vec3(1, 1, 1)

       
        t_min = (min_bound - glm.vec3(local_origin)) / glm.vec3(local_dir)
        t_max = (max_bound - glm.vec3(local_origin)) / glm.vec3(local_dir)

        t1 = glm.min(t_min, t_max)
        t2 = glm.max(t_min, t_max)

        t_near = max(t1.x, t1.y, t1.z)
        t_far = min(t2.x, t2.y, t2.z)

        if t_far < 0:          
            return False
        if t_near > t_far:     
            return False

        return True             

