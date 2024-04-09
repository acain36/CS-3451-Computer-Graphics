// Fragment shader

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_LIGHT_SHADER

// These values come from the vertex shader
varying vec4 vertColor;
varying vec3 vertNormal;
varying vec3 vertLightDir;
varying vec4 vertTexCoord;
vec2 center = vec2(0.5, 0.5);
//Trying below to rotate :((
/*
float newX = vertTexCoord.x * cos(radians(45)) - vertTexCoord.y * sin(radians(45));
float newY = vertTexCoord.x * sin(radians(45)) + vertTexCoord.y * cos(radians(45));
vertTexCoord = vec4(newX, newY, vertTexCoord.z, vertTexCoord.w);
*/
float absoluteValue(float num){
  if(num < 0) {
    return -1 * num;
  } else {
    return num;
  }
}

void main() { 
  mat2 r = mat2(cos(radians(45)), sin(radians(45)), -1 * sin(radians(45)), cos(radians(45)));
  float xD = absoluteValue(vertTexCoord.x - center.x);
  float yD = absoluteValue(vertTexCoord.y - center.y);
  vec2 tempCoord = vec2(xD, yD);
  tempCoord = r * tempCoord;
  tempCoord = vec2(tempCoord.x + center.x, tempCoord.y + center.y);
  float xDist = absoluteValue(tempCoord.x - center.x);
  float yDist = absoluteValue(tempCoord.y - center.y);
  if (xDist <= 0.07) {
    if ((yDist >= 0.31 && yDist <= 0.45) || (yDist >= 0.12 && yDist <= 0.26) || (yDist <= 0.07)) {
         gl_FragColor = vec4(0.2, 0.4, 1.0, 0);
    } else {
      gl_FragColor = vec4(0.2, 0.4, 1.0, 1);
    }
  } else if (xDist >= 0.12 && xDist <= 0.26) {
    if ((yDist >= 0.12 && yDist <= 0.26) || (yDist <= 0.07)) {
         gl_FragColor = vec4(0.2, 0.4, 1.0, 0);
    } else {
      gl_FragColor = vec4(0.2, 0.4, 1.0, 1);
    }
  } else if (xDist >= 0.31 && xDist <= 0.45) {
    if ((yDist <= 0.07)) {
         gl_FragColor = vec4(0.2, 0.4, 1.0, 0);
    } else {
      gl_FragColor = vec4(0.2, 0.4, 1.0, 1);
    }
  } else {
    gl_FragColor = vec4(0.2, 0.4, 1.0, 1);
  }
    
}

