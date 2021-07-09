#include <EtherCard.h>
#include <IPAddress.h>

static byte mymac[] = { 0x1A,0x2B,0x3C,0x4D,0x5E,0x6F };
byte Ethernet::buffer[700];
static uint32_t timer;

const static uint8_t ip[] = {10,1,17,6};
const static uint8_t gw[] = {10,1,17,1};
//const static uint8_t hip[] = {10,1,17,185};
const static uint8_t hip[] = {255,255,255,255};
//const static uint8_t hip[] = {192,168,0,101};
const static uint8_t dns[] = {0,0,0,0};
const int dstPort PROGMEM = 1234;

const int srcPort PROGMEM = 4321;
char temp[32];
void setup () 
{
  Serial.begin(9600);
  if (ether.begin(sizeof Ethernet::buffer, mymac, SS) == 0){
    Serial.println( "Failed to access Ethernet controller");}
if(!ether.staticSetup(ip, gw, dns))
{
   Serial.println("fail staticv");
}
  ether.udpServerListenOnPort(&udpSerialPrint, 1337);
}

char textToSend[32] = "K";//"E";
uint8_t rec;
//sizeof(textToSend)
void loop () 
{
  ether.sendUdp(textToSend, sizeof(textToSend) , srcPort, hip, dstPort );
  rec = ether.packetLoop(ether.packetReceive());
  delay(1);
}
void udpSerialPrint(uint16_t dest_port, uint8_t src_ip[IP_LEN], uint16_t src_port, const char *data, uint16_t len)
{
  uint8_t c = data[1];
  Serial.println(c);
  Serial.println(data);
}
