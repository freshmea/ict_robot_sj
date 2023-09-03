void setup(){
    Serial.begin(119200);
    pinMode(A0, INPUT);
}

void loop(){
    int cdsData = analogRead(A0);
    Serial.print("CDS:");
    Serial.println(cdsData);
    delay(500);
}