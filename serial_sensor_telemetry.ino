const int sensorPin = A3;
const int photoPin = A0;

void setup() {
  Serial.begin(9600);

}

void loop() {
  int sensorVal = analogRead(sensorPin);
  int photoVal = analogRead(photoPin);
  float voltage = sensorVal * (4.75 / 1023.0);
  float temp = (voltage - 0.55) * 100;
  float voltagel = photoVal * (5.0 / 1023.0);
  float luxScala = (voltagel / 5.0) * (10.0 - 1.0) + 0.2;
  Serial.print(temp);
  Serial.print(";");
  Serial.println(luxScala, 1);
  delay(3000);
}
