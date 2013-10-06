
#include <Servo.h> 
 
Servo leftMotor; 
Servo rightMotor;
const int ledPin = 13;
char inBytes[5]; 

 
void setup() 
{ 
  Serial.begin(9600);
  leftMotor.attach(9); 
  rightMotor.attach(3);
  pinMode(ledPin, OUTPUT); 
} 
 
 
void loop() 
{ 
  
  if ( Serial.available() > 0 ) 
  {
     Serial.readBytes(inBytes, 3);
     //Starts with A
     if( inBytes[0] == 122 ) 
     {
       
       digitalWrite(ledPin, HIGH);
       
       if( inBytes[1] != 0 )
       {
          rightMotor.write( byteScale( inBytes[1] ) );
       }
       
       if( inBytes[2] != 0 )
       {
          leftMotor.write( byteScale( inBytes[2] ) );
       }
       Serial.print("\nRight: ");
       Serial.print( byteScale( inBytes[1] ), DEC);
       Serial.print("\n Left: ");       
       Serial.print( byteScale( inBytes[1] ), DEC);    

     }else
     {
       digitalWrite(ledPin, LOW);
       leftMotor.write(90);
       rightMotor.write(90); 
     }
      
  }
  
} 

int byteScale( char input )
{
  int number = input - 0;
  int x = map(number, 0, 100, 75, 105);
  if( x > 105 || x < 75 )
  {
    x = 90;
  }  
  return x;
  //return number;
}
