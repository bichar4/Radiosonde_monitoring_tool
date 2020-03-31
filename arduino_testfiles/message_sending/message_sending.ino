
typedef struct {
  int           nodeId; //store this nodeId
  //unsigned long uptime; //uptime in ms
  float         temp;   //temperature maybe?
  float         humidity;
  double         pressure;
  double         alti;
  double         latitude;
  double         longitude;
  //double        altitude;
  
} Payload;
Payload theData;

void setup(void){
    Serial.begin(9600);
}

void loop(){
int   id = 1;
  read_temp();
  read_humidity();
  read_pressure();
  read_gps();
  theData.nodeId = 1;
  Serial.print('$');
  Serial.print(',');
  Serial.print(theData.nodeId);
  Serial.print(',');
  Serial.print(theData.temp);
  Serial.print(",");
  Serial.print(theData.humidity);
  Serial.print(",");
  Serial.print(theData.pressure);
  Serial.print(",");
  Serial.print(theData.latitude,6);
  Serial.print(",");
  Serial.println(theData.longitude, 6);
  //delay(100);
   theData.nodeId += 1;
  Serial.print('$');
  Serial.print(',');
  Serial.print(theData.nodeId);
  Serial.print(',');
  Serial.print(theData.temp);
  Serial.print(",");
  Serial.print(theData.humidity);
  Serial.print(",");
  Serial.print(theData.pressure);
  Serial.print(",");
  Serial.print(theData.latitude,6);
  Serial.print(",");
  Serial.println(theData.longitude, 6);
  //delay(100);
   theData.nodeId += 1;
   Serial.print('$');
  Serial.print(',');
  Serial.print(theData.nodeId);
  Serial.print(',');
    Serial.print(theData.temp);
  Serial.print(",");
  Serial.print(theData.humidity);
  Serial.print(",");
  Serial.print(theData.pressure);
  Serial.print(",");
  Serial.print(theData.latitude,6);
  Serial.print(",");
  Serial.println(theData.longitude, 6);
  //delay(100);
  
}

void read_temp(){
  theData.temp = 19.0;
}

void read_humidity(){
  theData.humidity = 98.0;
}

void read_pressure(){
  theData.pressure = 760.05; 
  theData.alti = 1650;
}

void read_gps(){
  theData.latitude = 27.054320;
  theData.longitude = 89.076578;
}
