// Fragment shader

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_LIGHT_SHADER

uniform float cx;
uniform float cy;

// These values come from the vertex shader
varying vec4 vertColor;
varying vec3 vertNormal;
varying vec3 vertLightDir;
varying vec4 vertTexCoord;

void main() { 

  vec2 c = vec2(cx, cy);
  float zx = (vertTexCoord.x * 6.28) - 3.14;
  float zy = (vertTexCoord.y * 6.28) - 3.14;
  vec2 z = vec2(zx, zy);

  vec4 diffuse_color = vec4 (1.0, 0.0, 0.0, 1.0);
  float diffuse = clamp(dot (vertNormal, vertLightDir),0.0,1.0);
  
  for(int i = 0; i < 20; i++){
    vec2 complexSine = vec2(sin(z.x) * cosh(z.y), cos(z.x)* sinh(z.y));
    //z_1 = c * sin(z_0)
    z = vec2(((c.x * complexSine.x) - (c.y * complexSine.y)), ((c.x * complexSine.y) + (c.y * complexSine.x)));
  }
  vec4 redColor = vec4(1, 0, 0, 1);
  vec4 whiteColor = vec4(1, 1, 1, 1);
  diffuse_color = redColor;
  if((z.x * z.x) + (z.y * z.y) < (50 * 50)) {
    diffuse_color = whiteColor;
  }
  gl_FragColor = vec4(diffuse * diffuse_color.rgb, 1.0);

}