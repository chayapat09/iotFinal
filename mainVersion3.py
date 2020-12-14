# import serial
# import paho.mqtt.publish as publist
# import paho.mqtt.client as mqtt
import time
# import json
# import random
# import ssl
import threading
# #All values and states
# #Order is [inTemp, inHumid, outTemp, outHumid, soilPercent, FanState, SoilState, LightState]

# # def getFanState() :
# #     return allValues[5]

# # def getPumpState() :
# #     return allValues[6]

# # def getLightState() :
# #     return allValues[7]

# # def setFanState(state) :
# #     allValues[5] = state

# # def setFanState(state) :
# #     allValues[6] = state

# # def setFanState(state) :
# #     allValues[6] = state

# #Total = 8 values

# allValues = [0 for i in range(8)]

# allValues[0] = 70

# #Netpie dashboard--------------------------
# port = 1883
# Server_ip = "broker.netpie.io"

# Publish_Topic = "@shadow/data/update"

# Client_ID = "cf078981-67ea-4b21-b306-84cc0c295643"
# Token = "RwGCi8g82hteZt5MjC3Cv1NaHMhK4pgn"
# Secret = "9z7vULPm1vAgi*W67Fh$~b5ZnfJxk#lv"
# MqttUser_Pass = {"username":Token,"password":Secret}

# sensor_data = {"inTemp": allValues[0],
#                "inHumid":allValues[1],
#                "outTemp":allValues[2],
#                "outHumid":allValues[3],
#                "soilPercent":allValues[4] }

# def updateDashBoard():
#     data_out=json.dumps({"data": sensor_data}) # encode object to JSON
#     print(data_out)
#     client.publish(Publish_Topic, data_out, retain= True)
#     print ("Publish successfully")
#     #time.sleep(2)
# #--------------------------------

# #Netpie to rpi-----------------------------
# subscribeTopic = "@msg/AutocadLover"

# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code " + str(rc))
#     client.subscribe(subscribeTopic)
    
# def on_message(client, userdata, msg):
#     print(msg.topic+" "+str(msg.payload))
#     data_receive= msg.payload.decode("UTF-8")
#     print("data receive = ", data_receive)
#     resend = True
#     if(data_receive[0]=='F'):
#         allValues[5] = int(data_receive[1])
#     elif(data_receive[0]=='S'):
#         allValues[6] = int(data_receive[1])
#     elif(data_receive[0]=='L'):
#         allValues[7] = int(data_receive[1])
#     if(data_receive == "CP" or data_receive == "PD"):
#         resend = False
#         print("PiCameraApplication is activated")
#         sendPiCameraApplication(data_receive)
#     #if(resend):
#     #    sendCommunication()
#     print(allValues)

# client = mqtt.Client(protocol=mqtt.MQTTv311,client_id=Client_ID, clean_session=True)
# client.on_connect = on_connect
# client.on_message = on_message

# client.subscribe(subscribeTopic)
# client.username_pw_set(Token,Secret)
# client.connect(Server_ip, port)
# client.loop_start()

# #---------------------------------

# #Connect main with PiCameraApplication
# def sendPiCameraApplication(dataFromMain):
#     print(dataFromMain)
# #-------------------------------------

# #Serial--------------------------
# globalList = [0 for i in range(1000)]
# Size = 0
# resetCommunication = False

# def sendCommunication():
#     global uart
#     sendString = "S"
#     for i in range(5,8):
#         sendString += str(allValues[i])
#     for i in range(5,8):
#         sendString += str(2-allValues[i])
#     sendString += 'E'
#     uart.write((sendString).encode())
#     print(sendString, " is sending to STM32")

# def setCommunication(portName, baudrate):
#     global uart
#     uart = serial.Serial("/dev/" + portName, baudrate, timeout=1)
#     uart.close()
#     uart.open()

# def receiveCommunication():
#     global uart
#     string_echo = ""
#     ok = True
#     while(len(string_echo)==0):
#         string_echo = uart.read_until('E'.encode()).decode('utf-8')
#         if(len(string_echo) > 999):
#             ok = False
#             #can't find 'E'
#             print("Something is wrong")
#             resetCommunication = True
#             break
#     if ok:
#         for i in range(len(string_echo)):
#             globalList[i] = string_echo[i]
#         Size = len(string_echo)
#     return ok
                
# def checkCommunication():
#     if(Size != 18 or globalList[0] != 'S' or globalList[17] != 'E'):
#         return False
#     #Order is [inTemp, inHumid, outTemp, outHumid, soilPercent, FanState, SoilState, LightState]
#     ok = True
#     for i in range(1,6):
#         #All values from sensors
#         val = int(globalList[i])
#         checkVal = int(globalList[i+8])
#         if(checkVal == 255-val):
#             allValues[i-1] = val
#     for i in range(6,9):
#         #All states
#         state =  int(globalList[i])
#         checkState = int(globalList[i+8])
#         if(checkState == 255-state):
#             if(allValues[i-1] != state):
#                 ok = False
#                 print("State isn't sync")
#                 break
#     return ok
# #----------------------------------------

# #Start main

# #command for searching port in raspi 4 -> sudo dmesg | grep tty
# portName = "ttyAMA0"
# baudrate = 115200
# uart = serial.Serial("/dev/" + portName, baudrate, timeout=1)


# setCommunication(portName, baudrate)


def capturing() :
    for i in range(5) :
        print('capturing ... ')
        time.sleep(1)

def ML() :
    for i in range(5):
        print('ML is running ... ')
        time.sleep(1)

# line of camera predict
def cp_line() :
    for i in range(5):
        print('linecP is running ... ')
        time.sleep(1)

# line of camera capture
def cc_line() :
    for i in range(5):
        print('linecC is running ... ')
        time.sleep(1)

class cameraCapturing(threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print("Starting " + self.name)
      capturing()
      print("Exiting " + self.name)


class cameraPredict_ML(threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print("Starting " + self.name)
      ML()
      print("Exiting " + self.name)



class cameraPredict_Line(threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print("Starting " + self.name)
      cp_line()
      print("Exiting " + self.name)


class cameraCapture_Line(threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print("Starting " + self.name)
      cc_line()
      print("Exiting " + self.name)


# fanState = 1
# pumpState = 1
# lightState = 1

# called this function
def predicting_request_callback() :
    global cameraPredictState
    if cameraPredictState != STATE_IDLE :
        return
    cameraPredict_edge_idle_capturing()

# called this function
def capturing_request_callback() :
    global cameraCaptureState
    if cameraCaptureState != STATE_IDLE :
        return
    cameraCapture_edge_idle_capturing()


cameraWorking = False

CAPTURED = 0
CAPTURING = 1

cameraState = CAPTURED

STATE_IDLE = 0
STATE_CAPTURING = 1
STATE_MACHINE_LEARNING = 2
STATE_LINE = 3
cameraPredictState = 0
cameraCaptureState = 0

cameraThreading = None
cameraPredictThreading = None
cameraCaptureThreading = None

def isCameraWorking():
    return cameraPredictState == STATE_CAPTURING or cameraCaptureState == STATE_CAPTURING

def cameraControlLoop() :
    # print('predictState' + str(cameraPredictState))
    print('captureState' + str(cameraCaptureState))
    # cameraPredict
    if cameraPredictState == STATE_IDLE :
        cameraPredict_state_idle()
    elif cameraPredictState == STATE_CAPTURING:
        cameraPredict_state_capturing()
    elif cameraPredictState == STATE_MACHINE_LEARNING:
        cameraPredict_state_ml()
    elif cameraPredictState == STATE_LINE:
        cameraPredict_state_line()
    else :
        print('wrong state')

    # cameraCapture
    if cameraCaptureState == STATE_IDLE :
        cameraCapture_state_idle()
    elif cameraCaptureState == STATE_CAPTURING:
        cameraCapture_state_capturing()
    elif cameraCaptureState == STATE_LINE:
        cameraCapture_state_line()
    else :
        print('wrong state')   

    # cameraCapture
    
def mqtt_send_capturing() :
    # handle thread start
    global cameraThreading
    cameraThreading = cameraCapturing(0,'CameraCapturing')
    cameraThreading.start()
    return
def mqtt_captured_finished_callback() :
    edges_capturing_captured()

def mqtt_cameraPredict_send_ml():
    # handle thread start
    global cameraPredictThreading
    cameraPredictThreading = cameraPredict_ML(1 , 'CameraObjectdetection')
    cameraPredictThreading.start()
    return

def mqtt_cameraPredict_ml_finished_callback() :
    cameraPredict_edge_ml_line()
    return

def mqtt_cameraPredict_send_line() :
    # handle thread start
    global cameraPredictThreading
    cameraPredictThreading = cameraPredict_Line(2 , 'LineNotifyPrediction')
    cameraPredictThreading.start()
def mqtt_cameraPredict_line_finished_callback() :
    
    cameraPredict_edge_line_idle()

def mqtt_cameraCapture_send_line() :
    # handle thread start
    global cameraCaptureThreading
    cameraCaptureThreading = cameraCapture_Line(3 , 'LineNotifyCapturing')
    cameraCaptureThreading.start()
    

def mqtt_cameraCapture_line_finished_callback():
    cameraCapture_edge_line_idle()
    return

def cameraPredict_state_idle() :
    return

def cameraPredict_state_capturing() :
    state_Capturing()
    

def cameraPredict_state_ml() :
    threadFinished = not cameraPredictThreading.is_alive()
    if threadFinished :
        mqtt_cameraPredict_ml_finished_callback()

def cameraPredict_state_line() :
    threadFinished = not cameraPredictThreading.is_alive()
    if threadFinished :
        mqtt_cameraPredict_line_finished_callback()
        

def cameraPredict_edge_idle_capturing () :
    global cameraPredictState
    cameraPredictState = STATE_CAPTURING

    if cameraCaptureState == STATE_CAPTURING :
        return
    edges_captured_capturing()
    

def cameraPredict_edge_capturing_ml () :
    global cameraPredictState
    cameraPredictState = STATE_MACHINE_LEARNING
    mqtt_cameraPredict_send_ml()

def cameraPredict_edge_ml_line () :
    global cameraPredictState
    cameraPredictState = STATE_LINE
    mqtt_cameraPredict_send_line()

def cameraPredict_edge_line_idle() :
    global cameraPredictState
    cameraPredictState = STATE_IDLE
    cameraPredictThreading = None


def cameraCapture_state_idle() :
    return

def cameraCapture_state_capturing() :
    state_Capturing()

def cameraCapture_state_line() :
    threadFinished = not cameraCaptureThreading.is_alive()
    if threadFinished :
        mqtt_cameraCapture_line_finished_callback()
    
    return

def cameraCapture_edge_idle_capturing () :
    global cameraCaptureState
    cameraCaptureState = STATE_CAPTURING
    if (cameraPredictState == STATE_CAPTURING) :
        return
    edges_captured_capturing()

def cameraCapture_edge_capturing_line () :
    #cameraState = CAPTURED
    global cameraCaptureState
    cameraCaptureState = STATE_LINE
    mqtt_cameraCapture_send_line()

def cameraCapture_edge_line_idle () :
    global cameraCaptureState
    cameraCaptureState = STATE_IDLE
    cameraCaptureThreading = None


def state_Captured():

    return

def state_Capturing() :
    # threading check for finished
    threadFinished = not cameraThreading.is_alive()
    if threadFinished :
        mqtt_captured_finished_callback()
    return

def edges_captured_capturing() :
    global cameraState
    cameraState = CAPTURING
    mqtt_send_capturing()

def edges_capturing_captured() :
    # set camera_line and camera_cameraPredict to nextState
    global cameraState
    cameraState = CAPTURED
    if cameraCaptureState == STATE_CAPTURING :
        cameraCapture_edge_capturing_line()
    if cameraPredictState == STATE_CAPTURING :
        cameraPredict_edge_capturing_ml()

# cameraPredict_edge_idle_capturing()


while True:
    #success = receiveCommunication()
    #if(not success):
    #    setCommunication(portName, baudrate)
    #syncState = checkCommunication()
    #if(not syncState):
    #    print("resend orders to STM32")
    
    #update dashboard
    #updateDashBoard()
    #send all states to STM32
    #sendCommunication()
    
    #cameraPredictThreading = cameraPredict_ML()
    print('123')
    cameraControlLoop()
    time.sleep(0.5)

## TODO
## timeout for eachState too long -> return to idleState




