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
#define D5	14
#define D6	12
#define D7	13
#define D8	15
#define D9	3
#define D10	1
#define D11	9
#define D12	10

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
  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D4, OUTPUT);
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

void setAnalogInput(int a, int b, int c, int d) {
  Serial.printf("%d %d %d %d\n", a, b, c, d);

  if (a == 1) {
    digitalWrite(D0, HIGH);
  } else {
    digitalWrite(D0, LOW);
  }
  if (b == 1) {
    digitalWrite(D1, HIGH);
  } else {
    digitalWrite(D1, LOW);
  }
  if (c == 1) {
    digitalWrite(D2, HIGH);
  } else {
    digitalWrite(D2, LOW);
  }
  if (d == 1) {
    digitalWrite(D3, HIGH);
  } else {
    digitalWrite(D3, LOW);
  }

}

void loop() {
  HTTPClient http;
  WiFiClient client;
  readTdsQuick();

  DynamicJsonDocument doc(1024);
  doc["ext_id"] = "WaterWifi";
  doc["p"] = "WaterWifi";
  doc["sensor_id"] = 1;
  doc["value"] = sensor::tds;

  String json;
  serializeJson(doc, json);

  http.begin(client, "http://34.93.25.177:7001/api/data");
  http.addHeader("Content-Type", "application/json");

  int httpCode = http.POST(json);

  if (httpCode > 0) {
    String payload = http.getString();
    Serial.println(httpCode);
    Serial.println(payload);
    shortBlink();
  } else {
    String payload = http.getString();
    Serial.println(httpCode);
    Serial.println(payload);
    Serial.println("Error on HTTP request");
    longBlink();
  }

  http.end();
  delay(10000);
}

void readTdsQuick() {
  setAnalogInput(0, 0, 0, 0);
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
  setAnalogInput(1, 1, 1, 1);
}

bool readpHData(float& ph_act) {
  float calibration_value = 21.34;
  int phval = 0;
  unsigned long int avgval;
  int buffer_arr[10], temp;

  for (int i = 0; i < 10; i++) {
    buffer_arr[i] = analogRead(pH_Sensor_Pin);
    delay(30);
  }
  for (int i = 0; i < 9; i++) {
    for (int j = i + 1; j < 10; j++) {
      if (buffer_arr[i] > buffer_arr[j]) {
        temp = buffer_arr[i];
        buffer_arr[i] = buffer_arr[j];
        buffer_arr[j] = temp;
      }
    }
  }
  avgval = 0;
  for (int i = 2; i < 8; i++)
    avgval += buffer_arr[i];
  float volt = (float)avgval * 5.0 / 1024 / 6;
  ph_act = -5.70 * volt + calibration_value;
  Serial.println(ph_act);
  return true;
}

void shortBlink() {
  digitalWrite(D4, HIGH);
  delay(100);
  digitalWrite(D4, LOW);
}

void longBlink() {
  digitalWrite(D4, HIGH);
  delay(1000);
  digitalWrite(D4, LOW);
}
