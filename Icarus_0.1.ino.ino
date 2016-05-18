int setUp = 12;
int photocellPin = A0;
int photocellReading = 0;
int LED = 8;
int buttonState = 0;
//Light Values
int lightValue = 0;
int lightValueMax = 0;
int lightValueMin = 0;
//Dark Values
int darkValue = 0;
int darkValueMax = 0;
int darkValueMin = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(setUp,INPUT);
  pinMode(LED,OUTPUT);
  
  

}

void loop() {
  // put your main code here, to run repeatedly:
  photocellReading = analogRead(photocellPin);
  delay(2000);
  //Serial.println(photocellReading);
  

  if(digitalRead(setUp) == HIGH)
  {
    digitalWrite(LED,HIGH);
    delay(2000);
    lightValue = analogRead(photocellPin);
    lightValueMax = lightValue + 20;
    lightValueMin = lightValue - 20;
    Serial.print("Light set at");
    Serial.println(lightValue);
    delay(3000);
    digitalWrite(LED,LOW);
    delay(5000);
    digitalWrite(LED,HIGH);
    darkValue = analogRead(photocellPin);
    darkValueMax = darkValue + 20;
    darkValueMin = darkValue - 60;
    Serial.print("Dark set at");
    Serial.println(darkValue);
    delay(3000);
    digitalWrite(LED,LOW);
  }

  if (photocellReading >= lightValueMin && photocellReading <= lightValueMax)
  {
    Serial.println("Light");
  }
  if (photocellReading >= darkValueMin && photocellReading <= darkValueMax)
  {
    Serial.println("Dark");
  }

  
  
}
