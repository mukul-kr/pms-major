#include <ESP8266WiFi.h>
#include <WiFiManager.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

#define TdsSensorPin A0
#define VREF 3.3
#define SCOUNT 30

#define D0 16
#define D1 5
#define D2 4
#define D3 0
#define D4 2
#define D5 14
#define D6 12
#define D7 13
#define D8 15
#define D9 3
#define D10 1
#define D11 9
#define D12 10

const byte TDS_SENSOR_PIN = A0;

namespace sensor {
float ec = 0;
unsigned int tds = 0;
float waterTemp = 30;
float ecCalibration = 1;
}

void initSensors() {
  pinMode(TDS_SENSOR_PIN, INPUT);
  // for (int i = 0; i < 5; i++) {
  pinMode(LED_BUILTIN, OUTPUT);
  // }

  Serial.println("Initializing...");
  delay(1000);
}

void setup() {
  Serial.begin(115200);
  initSensors();
  WiFiManager wifiManager;
  Serial.println("Connecting...");
  wifiManager.autoConnect("Mukul Node 1", "mukul1234");
  Serial.println("Connected");
}



void loop() {
  HTTPClient http;
  WiFiClient client;
  readTdsQuick();

  DynamicJsonDocument doc(1024);
  doc["ext_id"] = "WaterWifi";
  doc["p"] = "WaterWifi";
  doc["value"] = sensor::tds;

  String json;
  serializeJson(doc, json);

  http.begin(client, "http://34.93.25.177:3000/api/data");
  http.addHeader("Content-Type", "application/json");

  int httpCode = http.POST(json);

  if (httpCode > 0) {
    String payload = http.getString();
    Serial.println(httpCode);
    Serial.println(payload);
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
    delay(100);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
    delay(100);
  } else {
    String payload = http.getString();
    Serial.println(httpCode);
    Serial.println(payload);
    Serial.println("Error on HTTP request");
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
    delay(1000);                      // wait for a second
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
    delay(1000);
  }

  http.end();
  delay(1000);
}

void readTdsQuick() {

  delay(1000);
  sensor::waterTemp = 30;
  float rawEc = analogRead(TDS_SENSOR_PIN) * VREF / 1024.0;
  float temperatureCoefficient = 1.0 + 0.02 * (sensor::waterTemp - 25.0);
  sensor::ec = (rawEc / temperatureCoefficient) * sensor::ecCalibration;
  sensor::tds = (133.42 * pow(sensor::ec, 3) - 255.86 * sensor::ec * sensor::ec + 857.39 * sensor::ec) * 0.5;
  Serial.print(F("TDS:"));
  Serial.println(sensor::tds);
  Serial.print(F("EC:"));
  Serial.println(sensor::ec, 2);
  delay(1000);
}
