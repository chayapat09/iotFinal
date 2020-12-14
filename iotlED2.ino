#include <FastLED.h>

//#define ALL
//#define LED_PIN 2
//#define NUM_LEDS 96

#define BRIGHTNESS 200


CRGB leds[6][32];
//const LED_PIN[6] = {1,2,3,4,5,6};
const int LED_PER_STRIP[6] = {1,8,12,16,24,32};
int l = 0 , r = 12;
int l4 = 0 , r4 = 9;
void setup() {
  Serial.begin(115200);
int i = 0;
FastLED.addLeds<WS2812,2,GRB>(leds[i],LED_PER_STRIP[i]);
i++;
FastLED.addLeds<WS2812,3,GRB>(leds[i],LED_PER_STRIP[i]);
i++;
FastLED.addLeds<WS2812,4,GRB>(leds[i],LED_PER_STRIP[i]);
i++;
FastLED.addLeds<WS2812,5,GRB>(leds[i],LED_PER_STRIP[i]);
i++;
FastLED.addLeds<WS2812,6,GRB>(leds[i],LED_PER_STRIP[i]);
i++;
FastLED.addLeds<WS2812,7,GRB>(leds[i],LED_PER_STRIP[i]);

FastLED.setBrightness(BRIGHTNESS);


}
char serialState = 'a'; // a = violet , b = watering , c = close
void loop() {
  // Transition state 
  if (Serial.available()) {
    char x  = Serial.read();
    if (x >= 'a' && x <= 'd') {
      if (x != serialState) {
        // Transition
        serialState = x;
        if (x == 'b') initStateB();
      }
    }
  }

    switch (serialState - 'a') {
    case 0 : 
      stateA();
      break;
    case 1 :
      stateB();
      break;
    case 2 :
      stateC();
      break;
    case 3 :
      stateD();
      break;
  }
  
  FastLED.show();
  delay(20);
}

void initStateA() {
  // Violet const
}
void initStateB() {
  // Circular
  setLED(CRGB(0,0,0));
  l = 0;
  r = 12;
  l4 = 0;
  r4 = 9;
  for (int i = 0 ; i < r ; i++) {
    leds[5][i] = CRGB(0,255,255);
  }
  for (int i = 0 ; i < r4 ; i++) {
    leds[4][i] = CRGB(0,255,255);
  }
}

void initStateC() {
  // 
}

void initStateD() {
  //
}
void stateA() {
  setLED(CRGB(255,0,255));
}

void stateB() {
    //Set Color
  leds[5][l] = CRGB(0,0,0);
  leds[5][r] = CRGB(0,255,255);
  l++;r++;
  if(l % 4 != 0) {
    leds[4][l4] = CRGB(0,0,0);
    leds[4][r4] = CRGB(0,255,255);
    l4++;r4++;
  }
  if ( l == 32) l = 0;
  if ( r == 32) r = 0;
  if ( l4 == 24) l4 = 0;
  if ( r4 == 24) r4 = 0;
  
}

void stateC() {
  setLED(CRGB(0,0,0));
}

void stateD() {
  setLED(CRGB(150,150,150));
}

void setLED(CRGB val) {
  for (int i = 0 ; i < 6 ; i++ ) {
    for (int j = 0 ; j < 32 ; j++) {
      leds[i][j] = val;
    }
  }
}
