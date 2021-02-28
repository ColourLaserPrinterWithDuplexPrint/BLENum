'''
Version : 1.0
Required Libraries (all default libraries) : Socket, Time, Random, Base64, Sys

Socket : Bluetooth Connections
Time   : Waiting
Random : Generating Random Data
Base64 : Generating Invalid Packets
Sys    : Checking Operating System
OS     : Coloring For Windows
'''
#!/usr/bin/env python3
try:
    timeOutTime = 10
    silenceTimeOut = 999999999
    print("/*Starting Up*/")
    canStart = 1
    try:
        import socket
        #Make the socket time out after 10 seconds
        socket.setdefaulttimeout(timeOutTime)
        ##########################################
        test = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        del test
        print("[+] Socket Dependency Met")
    except:
        print("[-] Socket Dependency Not Met")
        canStart = 0
    try:
        import time
        print("[+] Time Dependency Met")
    except:
        print("[-] Time Dependency Not Met")
        canStart = 0
    try:
        import random
        print("[+] Random Dependency Met")
    except:
        print("[-] Random Dependency Not Met")
        canStart = 0
    try:
        import base64
        print("[+] Base64 Dependency Met")
    except:
        print("[-] Base64 Dependency Not Met")
        canStart = 0
    try:
        import os
        print("[+] OS Dependency Met")
    except:
        print("[-] OS Dependency Not Met")
        canStart = 0
    try:
        import sys
        print("[+] Sys Dependency Met")
    except:
        print("[-] Sys Dependency Not Met")
        canStart = 0
    if canStart == 0:
        print("[/] - Additional Dependencies Needed To Run This Program")
        input("Press Any Key To Exit : ")
        exit()
    print(
    '''
    ___________________________________________________________________________________
    | ___      _      ____    ___     __   __       __       ____        ____         |        
    | ||\\    ||     ||===|   ||\\    ||   ||       ||       //\\        //\\         |        
    | || \\   ||     ||___    || \\   ||   ||       ||      //  \\      //  \\        |        
    | ||==||  ||     ||===|   ||  \\  ||   ||       ||     //    \\    //    \\       |        
    | || //   ||     ||___    ||   \\ ||   \\       //    //      \\  //      \\      |        
    | ||//    ||==== ||===|   ||    \\||    \\=====//    //        \\//        \\     |        
    |_________________________________________________________________________________|            
    '''.replace("\\", "\\\\")
    )
    print('''
    |=============================|
    |+|=-Bluetooth Enumeration-=|+|
    |=============================|
    ''')
    operatingSystem = sys.platform
    print("\n")
    messg = ""
    if operatingSystem.startswith("win"):
        colour_option = input("Windows OS Detected. Would You Like To Colour The Terminal? [y/n] : ")
        if colour_option == 'y':
            os.system("color 09")
        elif colour_option == 'n':
            #Nothing
            print('',end='')
        else:
            print("Invalid Option, Defaulting To No")
        print("\n")
    def portScan():
        '''
        Re-making the socket object after every use slows the program down, and it might lead to many open connections, but it works.
        Please note that this causes a DOS on S08 Bluetooth speakers.
        ''' 
        mac = input("MAC Address To Scan : ")
        print("Starting Port Scan || Range : 0,100")
        #Kind of slow
        openPorts = []
        for _ in range(0, 100):
            s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            try:
                s.connect((mac, _))
                print("[+] " + str(_))
                openPorts.append(str(_))
            except Exception as e:
                print('[-] ' + str(_))
            del s
        print("\nOpen Ports : ",end="")
        print(openPorts)
        print("Done!")
        getInput()
    def incrementalAscii():
        mac = input("MAC Address Of Target : ")
        port = input("Port To Connect On : ")
        try:
            port = int(port)
        except:
            print("Invalid Port Number")
            getInput()
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~`!@#$%^&*()1234567890-_=+{}[]|;:'<>,.?/"
        chars = chars + '"'
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        try:
            s.connect((mac, port))
        except Exception as e:
            print("Failed To Connect To Device")
            print(e)
            getInput()
        for t1 in chars:
            print(t1, end="/")
            message = t1.encode()
            s.send(message)
        for t1 in chars:
            for t2 in chars:
                message = t1 + t2
                print(message, end="/")
                message = message.encode()
                s.send(message)
        for t1 in chars:
            for t2 in chars:
                for t3 in chars:
                    message = t1 + t2 + t3
                    print(message,end="/")
                    message = message.encode()
                    s.send(message)
        for t1 in chars:
            for t2 in chars:
                for t3 in chars:
                    for t4 in chars:
                        message = t1 + t2 + t3 + t4
                        print(message, end="/")
                        message = message.encode()
                        s.send(message)
        for t1 in chars:
            for t2 in chars:
                for t3 in chars:
                    for t4 in chars:
                        for t5 in chars:
                            message = t1 + t2 + t3 + t4 + t5
                            print(message,end="/")
                            message = message.encode()
                            s.send(message)
        for t1 in chars:
            for t2 in chars:
                for t3 in chars:
                    for t4 in chars:
                        for t5 in chars:
                            for t6 in chars:
                                message = t1 + t2 + t3 + t4 + t5 + t6
                                print(message,end="/")
                                message = message.encode()
                                s.send(message)
        for t1 in chars:
            for t2 in chars:
                for t3 in chars:
                    for t4 in chars:
                        for t5 in chars:
                            for t6 in chars:
                                for t7 in chars:
                                    message = t1 + t2 + t3 + t4 + t5 + t6 + t7
                                    print(message,end="/")
                                    message = message.encode()
                                    s.send(message)
        print("\nDone!")
        getInput()
            
    def mirror():
        mac = input("MAC Address Of Target : ")
        port = input("Port To Connect On : ")
        itera = input("Amount Of Reflections : ")
        responses = []
        try:
            port = int(port)
            itera = int(itera)
        except:
            print("Invalid Port Number Or Reflection Number")
            getInput()
        try:
            s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            s.connect((mac, port))
        except Exception as e:
            print(e)
            print("Failed To Connect To Target MAC Address")
            getInput()
        data = s.recv(1024)
        responses.append(data.decode())
        print("\nReceived : ",end="")
        print(data)
        print("\n")
        try:
            for _ in range(1, itera+1):
                    s.send(data)
                    print("Sent : ",end="")
                    print(data)
                    data = s.recv(1024)
                    responses.append(data.decode())
                    print("Received : ",end="")
                    print(data)
                    print("\n")
        except Exception as e:
                e = str(e)
                if 'timed' in e:
                    print("Connection Timed Out. Continuing With Statistics...")
                    
        print("\n[+] Data Collected. Preparing Data...")
        print("\n==DATA==")
        print(" /_\\ All Responses Collected : ")
        non_repeating = list(set(responses))
        for _ in non_repeating:
            print("-- " + repr(_))
        print("\nDone")
        getInput()
    def incremental_base10():
        num = 0
        mac = input("MAC Address Of Target : ")
        port = input("Port To Connect On : ")
        num = input("Number To Stop At : ")
        try:
            port = int(port)
            num = int(num)
        except:
            print("Invalid Port Number Or 'stop-at' Number")
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        try:
            s.connect((mac, port))
        except:
            print("Can't Connect To Device")
            getInput()
        try:
            for _ in range(0, num+1):
                print(_, end="")
                s.send(str(_).encode())
                print('/',end='')
                time.sleep(0.1)
        except:
            print("Socket Connection Broken")
            getInput()
        print("Done!")
        getInput()
        
    def send_buffer():
        mac = input("MAC Address Of Target : ")
        port = input("Port To Connect On :")
        bufferSize = input("Size Of Buffer : ")
        try:
            port = int(port)
            bufferSize = int(bufferSize)
        except:
            print("Port Or BufferSize is invalid")
        print("Generating Buffer...")
        try:
            buffer = 'A'*bufferSize
            buffer = buffer.encode()
        except:
            print("Error! A problem has occured while creating the buffer to send")
            getInput()
        print("Generated Buffer, Sending...")
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        try:
            print("Connecting...")
            s.connect((mac, port))
            print("Sending Buffer")
            s.sendall(buffer)
            print("Buffer Sent, Trying To Receive Data")
            data = s.recv(1024)
            print("\n")
            print(data)
        except Exception as e:
            print("Failed\n" + str(e))
        print("Done!")
        getInput()
            
    def getData(mac, port, message):
        #Connects To Mac Address On Port, Receives Data, Sends Message, Receives Second Data
        try:
            message = message.encode()
            bufferSize = 1024
            s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            s.connect((mac, port))
            firstData = s.recv(bufferSize)
            s.send(message)
            data = s.recv(bufferSize)
            return firstData,data
        except Exception as e:
            print("Failed!")
            print(e)
            getInput()
        except Exception as e:
            print(e)
        getInput()
    def repeated_send_buffer():
        mac = input("MAC Address Of Target : ")
        port = input("Port To Connect On : ")
        size = input("Size Of Buffer : ")
        amnt = input("Amount Of Times To Send Buffer : ")
        try:
            amnt = int(amnt)
            port = int(port)
            size = int(port)
        except:
            print("Port, Buffersize Or Send Amount Is Invalid")
            getInput()
        buffer = 'A'*size
        buffer = buffer.encode()
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        try:
            s.connect((mac, port))
        except Exception as e:
            print("Failed")
            print(e)
            getInput()
        print("Sending Buffers")
        for _ in range(1, amnt+1):
            s.sendall(buffer)
        print("All Data Sent. Receiving...")
        data = s.recv(1024)
        print("\n")
        print(data)
        print("Done!")
        try:
            s.close()
        except:
            print('',end='')
        getInput()
    def repeatSend():
        addr = input("MAC Address Of Target : ")
        port = input("Port To Connect On : ")
        messg = input("Message To Send : ")
        amnt = input("Amount Of Times To Send Message : ")
        try:
            port = int(port)
            amnt = int(amnt)
        except:
            print("Invalid Port Or Send Amount")
            getInput()
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        try:
            messg = messg.encode()
            print("Connecting")
            s.connect((addr, port))
            print("Connected, Sending Messages")
            for _ in range(0, amnt):
                s.send(messg)
                print("Sent Message Number " + str(_ + 1))
            print("Done!")
            getInput()
        except Exception as e:
            print("Error : " + str(e))
            getInput()
    def radioSilence():
        data = "a"
        addr = input("MAC Address : ")
        port = input("Port To Connect On : ")
        try:
            port = int(port)
        except:
            print("Invalid Port Number")
            getInput()
        bufferSize = 1024

        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        socket.setdefaulttimeout(silenceTimeOut)
        try:
                print("Connecting On Port : " + str(port))
                s.connect((addr, port))
                while True:
                    print("Receiving Data")
                    data = s.recv(bufferSize)
                    if data != b"":
                        print("Data : ",end="")
                        print(data)
                print("\nClosing Connection...")
                try:
                    s.close()
                    print("Closed")
                except:
                    print("Closed")
                time.sleep(1)
                print("\n\n")
        except Exception as e:
            print("Error : " + str(e))
            input()
        socket.setdefaulttimeout(timeOutTime)
        print("Finished!")
        input()
        getInput()
    def randomMessage():
        messg = ""
        addr = input("MAC Address : ")
        port = input("Port To Connect On : ")
        try:
            port = int(port)
        except:
            print("Invalid Port Number")
            getInput()
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for _ in range(1, 50):
            messg = messg + random.choice(chars)
        print("Created String")
        print("Message : " + messg)
        messg = messg.encode('utf-8')
        print("\n")
        bufferSize = 1024

        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        try:
                print("Port : " + str(port))
                s.connect((addr, port))
                print("Receiving Data")
                data = s.recv(bufferSize)
                print("Data : ",end="")
                print(data)
                print("Sending Data...")
                s.send(messg)
                print("Receiving Data")
                data = s.recv(bufferSize)
                print("Data : ",end="")
                print(data)
                print("\nClosing Connection...")
                try:
                    s.close()
                    print("Closed")
                except:
                    print("Closed")
                time.sleep(1)
                print("\n\n")
        except Exception as e:
            print("Error : " + str(e))
            input()
        print("Finished!")
        input()
        getInput()

    def invalidPackets():
        messg = ""
        addr = input("MAC Address : ")
        port = input("Port To Connect On : ")
        try:
            port = int(port)
        except:
            print("Invalid Port Number")
            getInput()
        print("Invalidating Packets...")
        chars = "abcdefghijklmnopqrstuvwxyz123457890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        messgLength = 100
        for _ in range(0, messgLength):
            messg = messg + random.choice(chars)
        messg = messg + "="*len(messg)
        print("Currently Invalidating Message Of A Length Of " + str(messgLength))
        print("\n")
        print("Full Message : " + messg)
        print("\n")
        invalid = base64.b64decode(messg)
        print("Created Invalid Packets")
        print("\n")
        bufferSize = 1024

        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

        try:
                print("Port : " + str(port))
                s.connect((addr, port))
                print("Sending Data...")
                s.send(invalid.encode('utf-8'))
                print("Successful! Receiving Data")
                data = s.recv(bufferSize)
                data = s.recv(1024)
                print("Data : ",end="")
                print(data)
                print("\nClosing Connection...")
                try:
                    s.close()
                    print("Closed")
                except:
                    print("Closed")
                time.sleep(1)                
                print("\n\n")
        except Exception as e:
            print("Error : " + str(e))
            input()
        print("Finished!")
        input()
        getInput()
    def specifiedMessage():
        messg = ""
        addr = input("MAC Address : ")
        port = input("Port To Connect On : ")
        messg = input("Message To Send : ")
        messg = messg.encode('utf-8')
        print("\n")
        try:
            port = int(port)
        except:
            print("Invalid Port")
            getInput()
        bufferSize = 1024

        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

        try:
                print("Port : " + str(port))
                s.connect((addr, port))
                print('Receiving Data')
                data = s.recv(bufferSize)
                print("Data : ", end="")
                print(data)
                print("Sending Data...")
                s.send(messg)
                print("Successful! Receiving Data")
                data = s.recv(bufferSize)
                print("Data : ",end="")
                print(data)
                print("\nClosing Connection...")
                try:
                    s.close()
                    print("Closed")
                except:
                    print("Closed")
                time.sleep(1)
                print("\n\n")
        except Exception as e:
            print("Error : " + str(e))
            input()
        print("Finished!")
        input()
        getInput()
    def checkConn():
        mac = input("MAC Address To Test : ")
        port = input("Port To Connect On : ")
        try:
            port = int(port)
        except:
            print("Invalid Port")
            getInput()
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        try:
            s.connect((mac, port))
            print("Successful! : Can Connect To " + mac + " On Port " + str(port))
        except :
            print("Can't Connect To " + mac + " On Port " + str(port))
        print("\n\n")
        getInput()
    def banner():
        print('''
     _____________________________________________________________
    |                                                             |
    |                                                             |
    |   {SENDING DATA}                                            |
    |       [1] - Specified Message                               |
    |       [2] - Repeatedly Send Specified Message               |
    |       [3] - Random Message                                  |
    |                                                             |
    |   {RESPONSE HARVESTING}                                     |
    |       [4] - Silence                                         |
    |       [5] - Mirror (Recommended)                            |
    |                                                             |                                                                                                              
    |   {MISCELLANEOUS}                                           |
    |       [6] - Invalid Message                                 |
    |       [7] - Send Buffer Of Specified Length                 |
    |       [8] - Repeatedly Send Buffer Of Specified Length      |
    |                                                             |
    |   {BRUTE-FORCE}                                             |
    |       [9] - Incremental Base10                              |
    |       [10] - Incremenetal Ascii                             |
    |                                                             |
    |   {SCANNING}                                                |
    |       [11] - Check Connection                               |
    |       [12] - Port Scan (could cause a temporary DOS)        |
    |                                                             |             
    |   {COMMANDS}                                                |
    |       [exit] - Exit                                         |
    |       [help] - Display This Message                         |
    |                                                             |
    |_____________________________________________________________|
''')
    def getInput():
        print("=================================================================\n")
        option = input("Option : ")
        if option == '1':
            specifiedMessage()
        elif option == '2':
            repeatSend()
        elif option ==  '3':
            randomMessage()
        elif option == '4':
            radioSilence()
        elif option == '5':
            mirror()
        elif option == 'help':
            banner()
            getInput()
        elif option == '6':
            invalidPackets()
        elif option == '7':
            send_buffer()
        elif option == '8':
            repeated_send_buffer()
        elif option == '9':
            incremental_base10()
        elif option == '10':
            incrementalAscii()
        elif option == '11':
            checkConn()
        elif option == '12':
            portScan()
            getInput()
        elif option == 'exit':
            exit()
        else:
            print("Invalid Option")
            getInput()
    if __name__ == '__main__':
        banner()
        getInput()
except Exception as err:
    print("Error : ",end="")
    print(err)
    socket.setdefaulttimeout(timeOutTime)
    getInput()
