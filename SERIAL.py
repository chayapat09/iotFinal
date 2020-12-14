import serial , time

uart = serial.Serial('/dev/cu.usbmodem141103',115200,timeout=0)#acm0 or acm1
uart.close()
uart.open()

#uart.write('AE'.encode())

inTempIdx = 0
inHumIdx = 1
outTempIdx = 2
outHumIdx = 3
soilMoisureIdx = 4

fanStateIdx = 5
pumpStateIdx = 6
lightStateIdx = 7

stateFromSTM = [0 for i in range(8)]

uartRxBufferMxSize = 20
uartRxBuffer = [0 for i in range(uartRxBufferMxSize)]
uartRxBufferPointer = 0
def increment_Pointer():
    global uartRxBufferPointer
    uartRxBufferPointer = (uartRxBufferPointer + 1)%uartRxBufferMxSize

def cpy_to_buffer(read_ints):
    for i in read_ints:
        uartRxBuffer[uartRxBufferPointer] = i
        increment_Pointer()


def checkCorrectness(_from,to) :
    if to - _from + 1 != 18: return False
    if uartRxBuffer[_from%uartRxBufferMxSize] != ord('S'): return False
    if uartRxBuffer[to%uartRxBufferMxSize] != ord('E') : return False

    _from += 1

    for i in range(3):
        if uartRxBuffer[(_from+i)%uartRxBufferMxSize] + uartRxBuffer[(_from+8+i)%uartRxBufferMxSize] != 255:
            return False
    return True
 
def getStateFromUart() :
    startPtr = 0 ; endPtr = 0 ; ansStPtr = -1 ;ansEndPtr = -1

    for i in range(uartRxBufferMxSize << 1):
        idx = i % uartRxBufferMxSize

        if uartRxBuffer[idx] == ord('S'):
            startPtr = i
            continue
        
        if uartRxBuffer[idx] == ord('E'):
            endPtr = i
            if checkCorrectness(startPtr , endPtr):
                ansStPtr = startPtr
                ansEndPtr = endPtr
            continue

    if ansStPtr == -1: return False

    global stateFromSTM
    # setNewState
#    print(ansStPtr , ansEndPtr)
#    stateFromSTM = list(uartRxBuffer[(ansStPtr+1)%uartRxBufferMxSize : (ansStPtr+9)%uartRxBufferMxSize])
    ptr = 0
    for i in range(ansStPtr+1 , ansStPtr+9):
        idx = i %uartRxBufferMxSize
        stateFromSTM[ptr] = uartRxBuffer[idx]
        ptr+=1

    return True

        

# cpy_to_buffer([1,2,3,4,5,6])
# print(uartRxBuffer)
# cpy_to_buffer([ord('S'),20,60,25,70,43, 0,2,1 , 255 - 20 , 255 - 60 , 255 - 25 , 255 - 70 , 255 - 43 , 255 - 0 , 255 - 2,255 - 1,ord('E')])
# print(uartRxBuffer)
# getStateFromUart()

# print(stateFromSTM)

# cpy_to_buffer([13,14,15,16,17,18,19,20,21,22,23])
# print(uartRxBuffer)
label = ['inTemp' , 'inHummudity' , 'outTemp' , 'outhummudity' , 'soilMoisure' , 'fanState' , 'pump/soil State' , 'lightState']
while True:
    #uart.write('A'.encode())
    read_bytes = bytearray(uart.read_all())
    #int.from_bytes(read_bytes , 'little')

    cpy_to_buffer(read_bytes)
    getStateFromUart()
    for i in range(8):
        print(label[i] + ' : ' + str(stateFromSTM[i]))
    print()
    print()
    time.sleep(1)
    
