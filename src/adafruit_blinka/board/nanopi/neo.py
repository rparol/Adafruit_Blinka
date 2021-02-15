"""Pin definitions for the NanoPi NEO."""
# Enable I2C0, UART1, and SPI by adding the following lines to /boot/armbianEnv.txt
#    overlays=usbhost2 usbhost3 spi-spidev uart1 i2c0
#    param_spidev_spi_bus=0

# changed pin names to be consistent with board pin numbers

from adafruit_blinka.microcontroller.allwinner.h3 import pin

# 24 PIN Header
D3 = pin.PA12
D5 = pin.PA11
D7 = pin.PG11
D8 = pin.PG6
D10 = pin.PG7
D11 = pin.PA0
D12 = pin.PA6
D13 = pin.PA2
D15 = pin.PA3
D16 = pin.PG8
D18 = pin.PG9
D19 = pin.PC0
D21 = pin.PC1
D22 = pin.PA1
D23 = pin.PC2
D24 = pin.PC3

# 12 PIN Header
U6 = pin.PL11
U7 = pin.PA17
U8 = pin.PA18
U9 = pin.PA19
U10 = pin.PA20
U11 = pin.PA21

#UART Header
C3 = pin.PA4
C4 = pin.PA5 

# I2C
SDA = D3
SCL = D5

# SPI
SCLK = D23
MOSI = D19
MISO = D21
CS0 = D24
SCK = SCLK

# Serial UART
UART1_TX = D8
UART1_RX = D10
UART1_RTS = D16
UART1_CTS = D18

UART2_RX = D22
UART2_TX = D11
UART2_RTS = D13
UART2_CTS = D15

UART0_RX =C4
UART0_TX =C3

# PWM
PWM0 = C4
