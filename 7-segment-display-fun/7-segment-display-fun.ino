#define PIN_2 2
#define PIN_3 3

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(PIN_2, OUTPUT);
  pinMode(PIN_3, OUTPUT);
}

int count = 0;

// the loop function runs over and over again forever
void loop() {

  count++;

  if (count == 1) {
    digitalWrite(PIN_2, HIGH);
  }
  else if (count == 2) {
    digitalWrite(PIN_3, HIGH);
  }
  else {
    digitalWrite(PIN_2, LOW);
    digitalWrite(PIN_3, LOW);
    count = 0;
  }
  
  delay(1000);
}
