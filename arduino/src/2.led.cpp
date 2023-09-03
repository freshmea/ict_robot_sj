int GREEN = 11;
int RED = 10;
int BLUE = 9;

void setup(){
    pinMode(GREEN, OUTPUT);
    pinMode(RED, OUTPUT);
    pinMode(BLUE, OUTPUT);
}

void loop(){
  for(int i=0;i<256;i++){
    digitalWrite(GREEN, 0);
    digitalWrite(RED, i);
    digitalWrite(BLUE, 0);
    delay(5);
    
  }
  for(int i=0;i<256;i++){
    analogWrite(GREEN, i);
    analogWrite(RED, 0);
    analogWrite(BLUE, 0);
    delay(5);
  }
  for(int i=0;i<256;i++){
    analogWrite(GREEN, 0);
    analogWrite(RED, 0);
    analogWrite(BLUE, i);
    delay(5);
  }
}