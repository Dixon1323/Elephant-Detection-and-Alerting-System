
int interval=30000;
unsigned int current,previous=0;

void setup()
{
    Serial.begin(115200);
    pinMode(D0,OUTPUT);
    pinMode(D2,OUTPUT);
    pinMode(D5,OUTPUT);
    digitalWrite(D0,LOW);
    digitalWrite(D2,LOW);
    digitalWrite(D5,LOW);
    
    
}
/Users/dixonsmac/Downloads/Algorithm for Elephant Detection and Notification System.docx
void loop()
{
  current=millis();
    if (Serial.available())
    {
        String a = Serial.readString();
        Serial.print("Received Value: ");
        Serial.println(a);
        int b = a.toInt();
        if(b==2){
          digitalWrite(D0,HIGH);
          noti(30,100); //times  delay
        }
    }
  if(current-previous>=interval)
  {
    previous=current;
    digitalWrite(D0,LOW);
  }
}

void noti(int count, int time){
  for(int i=0;i<=count;i++){
    digitalWrite(D2,HIGH);
    digitalWrite(D5,HIGH);
    delay(time);
    digitalWrite(D2,LOW);
    digitalWrite(D5,LOW);
    delay(time);
  }
}