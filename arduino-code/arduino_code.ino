/*
 * Atmospheric CO2 Level..............400ppm
 * Average indoor co2.............350-450ppm
 * Maxiumum acceptable co2...........1000ppm
 * Dangerous co2 levels.............>2000ppm
*/
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>
 
const char* ssid = "Rocha"; //nombre de la red wifi
const char* password = "PRocha0503"; //contraseña del wifi
WiFiClient wifiClient;
#define         DELAY          (10000) 
#define         DB_CLIENT          (1) 
#define         DB_MODEL          ("MQ135-CO2") 
#define         PINUMBER    (A0)

float R2 = 1000; //Resistencia del circuito, calculada con un multimetro
float R0=0;
bool DEBUG=true;

void setup() {
  pinMode(PINUMBER,INPUT);    
  Serial.begin(115200);
  
  Serial.println("Calibrando...");
  initialize(PINUMBER);
  
  establishConnection();
  
}

void establishConnection(){
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
 
    delay(1000);
    Serial.println("Connecting Module..");
 
  }
}

void loop() {
   float volts = voltage(PINUMBER);
   float RS = R2 * (1-volts);
   RS = RS/volts;
   //-------Cálculo de las concentraciones de los gases------------
   double co2 = 119.63*pow(RS/R0, -2.81); 
   
   double co22 = 336.68-231.36*(RS/R0); 
   
   if(co22<0){
    co22=0;
   }
   
   Serial.print("  CO2 metodo2: ");
   Serial.print(co22);
   Serial.println();
   
   sendRequest(co22);
   // print out the gases concentration:
   /*Serial.print("  CO2 metodo1: ");
   Serial.print(co2);
   Serial.print("  VOLTAJE: ");
   Serial.print(volts);
   Serial.print("  RS: ");
   Serial.print(RS);
   Serial.print("  CO2 metodo2: ");
   Serial.print(co22);
   Serial.println();*/
   delay(DELAY); // delay in between reads for stability
}

float voltage(int pinNum){
    // read the input on analog pin:
   int sensorValue = analogRead(pinNum);
   //int sensorValue = digitalRead(pinNum);
   // convert to voltage:
   float volts = sensorValue * 5;
   volts = volts / 1023;
   return volts;
}

void initialize(int pinNum){
  float volts=0;
  for(int i=0;i<50;i++){
    volts+=voltage(pinNum);
    delay(500);
  }
  volts/=50;
  Serial.print("V0: ");
  Serial.println(volts);
  R0=((R2*(1-volts))/(volts));
  Serial.print("R0: ");
  Serial.println(R0);
}



String makeJSON(int clientID, String model, double gasConcentration){
  DynamicJsonDocument doc(1024);
  doc["client_id"] = clientID;
  doc["model"] = model;
  doc["gas_concentration"] = gasConcentration;
  String a;
  serializeJson(doc, a);
  return a;
}

void sendRequest(double co2){
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
 
    HTTPClient http;  //Declare an object of class HTTPClient

    http.begin(wifiClient, "http://52.87.242.29/data-records");      //Specify request destination
    http.addHeader("Content-Type", "application/json");  //Specify content-type header

    int httpCode = http.POST(makeJSON(DB_CLIENT,DB_MODEL,co2));   //Send the request
    String payload = http.getString();  //Get the response payload
 
    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload
 
    http.end();  //Close connection
 
  }
}
