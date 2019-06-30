// say one unit is a tenth of a second

int pin = 2;
int unit = 1000;

void dash() {
  digitalWrite(pin, HIGH);
  delay(unit * 3);
}

void betweenWords() {
  digitalWrite(pin, LOW);
  delay(unit * 7);
}

void betweenLetters() {
  digitalWrite(pin, LOW);
  delay(unit * 3);
}

void betweenPartsOfLetter() {
  digitalWrite(pin, LOW);
  delay(unit);
}

void dot() {
  digitalWrite(pin, HIGH);
  delay(unit);
}

void letterA() {
  dot();
  betweenPartsOfLetter();
  dash();
}

void letterB() {
  dash();
  betweenPartsOfLetter();
  dot();
  betweenPartsOfLetter();
  dot();
  betweenPartsOfLetter();
  dot();
}

void setup() {
  // put your setup code here, to run once:
  pinMode(pin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Letter A");
  letterA();
  betweenLetters();
  Serial.println("Letter B");
  letterB();
  betweenLetters();
}
