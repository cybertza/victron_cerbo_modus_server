from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusBinaryFramer
from pymodbus.client.sync import ModbusSerialClient
import signal
import sys
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Initialize Modbus RTU client
client = ModbusSerialClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600, stopbits=1, parity='N', bytesize=8, timeout=1)
log.info("Startup Welcome https://github.com/cybertza/victron_cerbo_modus_server")
# Make sure we can connect to the serial port
if not client.connect():
    log.error("Unable to connect to /dev/ttyUSB0")
    sys.exit(1)

class CustomDataBlock(ModbusSequentialDataBlock):
    def getValues(self, address, count=1):
        response = client.read_holding_registers(address-1, count, unit=1)
        if not response.isError():
            log.debug(f'Read request - Start Address: {address-1} Number of Registers: {count} Response: {response.registers}')
            return response.registers
        else:
            log.debug(f"Error reading registers: {response}")
            return None

store = ModbusSlaveContext(hr=CustomDataBlock(0, [0]*400))
context = ModbusServerContext(slaves=store, single=True)

def signal_handler(sig, frame):
    log.info("Exiting on Ctrl+C")
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

StartTcpServer(context, address=("0.0.0.0", 5020))
