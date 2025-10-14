#version 330

// inputs desde el vao 

in vec3 in_pos; 
in vec3 in_color;

// Output, esto recibe lo del fragment shader (se encarga de acomodar los pixeles) 
out vec3 v_color;

// esta varia es global, que recibe para aplicar transformaciones al objeto 
uniform mat4 Mvp;

void main( ){
    gl_Position =   Mvp * vec4(in_pos,1.0);
    v_color = in_color;
}

