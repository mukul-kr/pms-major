#include <ESP8266WiFi.h>
#include <WiFiManager.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

#define SensorPin A0
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

const byte SENSOR_PIN = A0;

namespace tds_sensor {
  float ec = 0;
  unsigned int tds = 0;
  float waterTemp = 30;
  float ecCalibration = 1;
}

namespace turbidity_sensor {
  float value = 0;
}

namespace pH_sensor {
  float value = 0;
}

void initSensors() {
  pinMode(SENSOR_PIN, INPUT);
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
  // WiFiManager wifiManager;
  // Serial.println("Connecting...");
  // wifiManager.autoConnect("Mukul Node 1", "mukul1234");
  // Serial.println("Connected");
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
  // HTTPClient http;
  // WiFiClient client;
  readTdsQuick();

  // DynamicJsonDocument doc(1024);
  // doc["ext_id"] = "WaterWifi";
  // doc["p"] = "WaterWifi";
  // doc["sensor_id"] = 1;
  // doc["value"] = tds_sensor::tds;

  // String json;
  // serializeJson(doc, json);

  // http.begin(client, "http://34.93.25.177:7001/api/data");
  // http.addHeader("Content-Type", "application/json");

  // int httpCode = http.POST(json);

  // if (httpCode > 0) {
  //   String payload = http.getString();
  //   Serial.println(httpCode);
  //   Serial.println(payload);
  //   shortBlink();
  // } else {
  //   String payload = http.getString();
  //   Serial.println(httpCode);
  //   Serial.println(payload);
  //   Serial.println("Error on HTTP request");
  //   longBlink();
  // }

  // http.end();
  // delay(10000);

  delay(1000);

  readpHData();

  // delay(10000);
  delay(1000);

  readTurbidityData();
  delay(1000);
}

void readTdsQuick() {
  setAnalogInput(0, 0, 0, 1);
  delay(1000);
  tds_sensor::waterTemp = 30;
  float rawEc = analogRead(SENSOR_PIN) * VREF / 1024.0;
  float temperatureCoefficient = 1.0 + 0.02 * (tds_sensor::waterTemp - 25.0);
  tds_sensor::ec = (rawEc / temperatureCoefficient) * tds_sensor::ecCalibration;
  tds_sensor::tds = (133.42 * pow(tds_sensor::ec, 3) - 255.86 * tds_sensor::ec * tds_sensor::ec + 857.39 * tds_sensor::ec) * 0.5;
  Serial.print(F("TDS:"));
  Serial.println(tds_sensor::tds);
  Serial.print(F("EC:"));
  Serial.println(tds_sensor::ec, 2);
  delay(1000);
  setAnalogInput(1, 1, 1, 1);
}

void readTurbidityData() {
  setAnalogInput(0, 0, 0, 0);

  // float Turbidity_Sensor_Voltage = 0;
  // int samples = 600;
  // for (int i = 0; i < samples; i++) {
  //   Turbidity_Sensor_Voltage += ((float)analogRead(SENSOR_PIN) / 1023) * 5;
  // }

  // Turbidity_Sensor_Voltage = Turbidity_Sensor_Voltage / samples;
  // Turbidity_Sensor_Voltage = round_to_dp(Turbidity_Sensor_Voltage, 2);
  // // if (Turbidity_Sensor_Voltage < 2.5) {
  // //   turbidity_sensor::value = 3000;
  // // } else {
  //   turbidity_sensor::value = -1120.4 * square(Turbidity_Sensor_Voltage) + 5742.3 * Turbidity_Sensor_Voltage - 4352.9;
  // // }
  turbidity_sensor::value = customMap((float)analogRead(SENSOR_PIN), 0,640, 100, 0) + 16;
  Serial.print("turbidity: ");
  Serial.println(turbidity_sensor::value);

  setAnalogInput(1, 1, 1, 1);
  
}

float square(float num) {
  return num * num;
}

float round_to_dp(float in_value, int decimal_place) {
  float multiplier = powf(10.0f, decimal_place);
  in_value = roundf(in_value * multiplier) / multiplier;
  return in_value;
}

float customMap(float x, float fromLow, float fromHigh, float toLow, float toHigh) {
    return toLow + ((x - fromLow) / (fromHigh - fromLow)) * (toHigh - toLow);
}

void readpHData() {
  setAnalogInput(0, 0, 1, 0);
  Serial.println((float)analogRead(SENSOR_PIN)-65); 
  pH_sensor::value = customMap((float)analogRead(SENSOR_PIN) - 65, 0,1024, 0, 14);
  // float calibration_value = 21.34;
  // int phval = 0;
  // unsigned long int avgval;
  // int buffer_arr[10], temp;

  // for (int i = 0; i < 10; i++) {
  //   buffer_arr[i] = analogRead(SENSOR_PIN);
  //   delay(30);
  // }
  // for (int i = 0; i < 9; i++) {
  //   for (int j = i + 1; j < 10; j++) {
  //     if (buffer_arr[i] > buffer_arr[j]) {
  //       temp = buffer_arr[i];
  //       buffer_arr[i] = buffer_arr[j];
  //       buffer_arr[j] = temp;
  //     }
  //   }
  // }
  // avgval = 0;
  // for (int i = 2; i < 8; i++)
  //   avgval += buffer_arr[i];
  // float volt = (float)avgval * 5.0 / 1024 / 6;
  // pH_sensor::value = -5.70 * volt + calibration_value;
  Serial.println(pH_sensor::value);
  
  setAnalogInput(1, 1, 1, 1);

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
