#include <Adafruit_NeoPixel.h>

#define NEOPIXEL_PIN 6

# define REQUEST_BOARD_STATUS '1'
# define REQUEST_CLEAR_BOARD '2'

int WHITE_MARGIN = 650;
int BLACK_MARGIN = 450; 

char boardStatus[64];

Adafruit_NeoPixel strip = Adafruit_NeoPixel(64, NEOPIXEL_PIN);

int multiplexerPinsValues[16][4] = { 
                                    {0, 0, 0, 0},
                                    {0, 0, 0, 1},
                                    {0, 0, 1, 0},
                                    {0, 0, 1, 1},
                                    {0, 1, 0, 0},
                                    {0, 1, 0, 1},
                                    {0, 1, 1, 0},
                                    {0, 1, 1, 1},
                                    {1, 0, 0, 0},
                                    {1, 0, 0, 1},
                                    {1, 0, 1, 0},
                                    {1, 0, 1, 1},
                                    {1, 1, 0, 0},
                                    {1, 1, 0, 1},
                                    {1, 1, 1, 0},
                                    {1, 1, 1, 1}
                                 };


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  strip.begin();
  strip.show();
  
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
}

void loop() {
  if (Serial.available()){
    char request = Serial.read();
    switch(request){
      case REQUEST_BOARD_STATUS:
        readBoard();
        break;
      case REQUEST_CLEAR_BOARD:
        clearBoard();
        break;
    }
  }
}

void readBoard(){
  for (int multiplexerPin=0; multiplexerPin<16; multiplexerPin++){
    // Set multiplexer pin
    for (int i=0; i<4; i++){
      digitalWrite(9+i, multiplexerPinsValues[multiplexerPin][i]);
    }
    readValues(multiplexerPin);
  }

  for (int i=0; i<64; i++){
    Serial.write(boardStatus[i]);
  }
  Serial.println();
}

void clearBoard(){
  for (int i=0; i<64; i++){
    strip.setPixelColor(i, 0, 0, 0);
  }
}

void readValues(int multiplexerPin){
  int z = multiplexerPin*4;
  boardStatus[z] = checkVal(analogRead(A0));
  z++;
  boardStatus[z] = checkVal(analogRead(A1));
  z++;
  boardStatus[z] = checkVal(analogRead(A2));
  z++;
  boardStatus[z] = checkVal(analogRead(A3));
}


char checkVal(int val){
  if (val < WHITE_MARGIN){
    return 'w';
  }else{
    if (val > BLACK_MARGIN){
      return 'b';
    }else{
      return '-';
    }
  }
}

