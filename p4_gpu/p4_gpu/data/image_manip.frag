// Fragment shader
// The fragment shader is run once for every pixel
// It can change the color and transparency of the fragment.

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_TEXLIGHT_SHADER

// Set in Processing
uniform sampler2D my_texture;
uniform sampler2D my_mask;
uniform float blur_flag;

// These values come from the vertex shader
varying vec4 vertColor;
varying vec3 vertNormal;
varying vec3 vertLightDir;
varying vec4 vertTexCoord;

void main() { 
  
  // grab the color values from the texture and the mask
  vec4 diffuse_color = texture2D(my_texture, vertTexCoord.xy);
  vec4 mask_color = texture2D(my_mask, vertTexCoord.xy);
  vec4 blur_color  = vec4(0.0, 0.0, 0.0, 0.0); 
  int radius = 1; 

  if (blur_flag == 1.0) {
    if (mask_color.r <= 0.1) {
          radius = 10; 
    } else if (mask_color.r <= 0.5 && mask_color.r > 0.1) {
          radius = 5;
    } 
  }

  float texel_size = 1.0 / textureSize(my_texture, 0).x; 
 
  for (int i = -1 * radius; i < radius; i++) {
    for (int j = -1 * radius; j < radius; j++) {
        vec2 sampleTexture = vec2(vertTexCoord.x + (i * texel_size), vertTexCoord.y + (j * texel_size));
        vec4 sampleTexture2 = texture2D(my_texture, sampleTexture);
        blur_color += sampleTexture2;
         
    }
  }

  blur_color /= ( 5 * radius * radius); 
  diffuse_color = blur_color; 
  float diffuse = clamp(dot (vertNormal, vertLightDir),0.0,1.0);

  gl_FragColor = vec4(diffuse * diffuse_color.rgb, 1.0);
}
