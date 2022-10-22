
#define SHIFT_DATA 2
#define SHIFT_CLOCK 3
#define SHIFT_LATCH 4


void setup() {
  pinMode(SHIFT_DATA, OUTPUT);
  pinMode(SHIFT_CLOCK, OUTPUT);
  pinMode(SHIFT_LATCH, OUTPUT);

  shiftOut(SHIFT_DATA, SHIFT_CLOCK, MSBFIRST, 0xaa);
  digitalWrite(SHIFT_LATCH, LOW);
  digitalWrite(SHIFT_LATCH, HIGH);
  digitalWrite(SHIFT_LATCH, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:

  //0xf = 1111
  //1010 = 0xa
}
