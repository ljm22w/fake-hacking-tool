from ast import While
import os
import random
import time

# Change to Green font / 녹색 폰트로 바꿈
# make: ljm22w(jimin lee / 이지민)
os.system ('color 02')
os.system ('cls')

# Command Guide / 명령어 가이드
print ('------------------------------------------------------')
print ('//                            //          //')
print ('//                            //            ')
print ('//                            //          //')
print ('////////////////////////////////          //')
print ('//                            //          //')
print ('//                            //          //')
print ('//                            //          //')
print ('-------------------------------------------------------')
print ('')
print ('how to use?')
print ('')
print ('con: connecting to the server')
print ('toolis: Install the hacking tool on the server (only used after connecting to the server)')
print ('hack: Start hacking to the attached server (only used after connecting to the server and Install the hacking tool on the server)')
print ('')
print ('Guide: This program is a fake hacking program. / Run this program as a command on the terminal. / Also, do not rename this file. Causes an error in the command.')

# Command input space / 명령어 입력 칸

a = input()

# Conditional statement for reply to input command / input 명령어에 대해 사용자가 남긴 답변에 대한 조건문

# When entering the con command / con 명령어를 입력했을 때

if a == "con":
    os.system('cls')
    print ('Attempting to connect with server.')
    time.sleep (1)

    os.system('cls')
    print ('You have successfully connected to the server.')
    time.sleep (1)

    os.system('cls')
    print ('Command:')
    print ('toolis: Install the hacking tool on the server (only used after connecting to the server)')
    print ('hack: Start hacking to the attached server (only used after connecting to the server and Install the hacking tool on the server)')
    print ('')
    b = input()

    if b == "toolis":
        print ('Creating a folder in server.')
        rtm = 5
        time.sleep(rtm)
        print ('Installing database and creating executable redirect files')
        time.sleep(rtm)
        print ('Installing Sub-Programs')
        time.sleep(rtm)
        print ('Download Successful!')
        print ('This message will be turned off in 3 seconds.')
        time.sleep(3)
        os.system ('cls')
        

        # Wait for command input after download / 다운로드 이후 명령어 입력 대기

        print ('Command:')
        print ('hack: Start hacking to the attached server (only used after connecting to the server and Install the hacking tool on the server)')
        print ('')
        c = input()

        os.system('cls')
        if c == "hack":
            print ('start the attack!')
            time.sleep (0.5)
            print ('All processes preventing hacking are shutting down.')
            print ('[/------------]')
            time.sleep (0.5)
            os.system ('cls')
            print ('All processes preventing hacking are shutting down.')
            print ('[//-----------]')
            time.sleep (0.5)
            os.system ('cls')
            print ('All processes preventing hacking are shutting down.')
            print ('[///----------]')
            time.sleep (0.5)
            os.system ('cls')
            print ('All processes preventing hacking are shutting down.')
            print ('[////---------]')
            time.sleep (0.5)
            os.system ('cls')
            print ('All processes preventing hacking are shutting down.')
            print ('[/////--------]')
            time.sleep (0.5)
            os.system ('cls')
            print ('All processes preventing hacking are shutting down.')
            print ('[//////-------]')
            time.sleep (0.5)
            os.system ('cls')
            print ('All processes preventing hacking are shutting down.')
            print ('[///////------]')
            time.sleep (0.5)
            os.system ('cls')
            print ('All processes preventing hacking are shutting down.')
            print ('[////////-----]')
            time.sleep (0.5)
            os.system ('cls')
            print ('All processes preventing hacking are shutting down.')
            print ('[/////////----]')
            time.sleep (0.5)
            os.system ('cls')
            print ('All processes preventing hacking are shutting down.')
            print ('[//////////---]')
            time.sleep (0.5)
            os.system ('cls')
            print ('All processes preventing hacking are shutting down.')
            print ('[///////////--]')
            time.sleep (0.5)
            os.system ('cls')
            print ('All processes preventing hacking are shutting down.')
            print ('[////////////-]')
            time.sleep (0.5)
            os.system ('cls')
            print ('All processes preventing hacking are shutting down.')
            print ('[/////////////]')
            time.sleep (0.5)
            os.system ('cls')
            print ('First attack successful!')
            print ("We're preparing a DDoS attack. Please wait.")
            time.sleep (3)
            print ('Initiate a DDoS attack.')
            print ('Sending 30 million packets via zombie pc!!!!')
            wh = 0
            while wh < 1500:
                wh = wh + 1
                print ('Packet sending succeeded.')
            print ("We've finished all the attacks. Close the program in 10 seconds.")
            time.sleep(10)
            exit ()

            
        
# If enter another command / 유효하지 명령어를 입력했을 때
    else:
        print ('Either you entered an invalid command, or you entered a command that is currently unavailable.')
        print ('Press any key to restart the program. (a return to the former times)')
        input()
        os.system ('python gf-sh-dm.py')
        exit()

else:
    os.system('cls')
    print ('The command is either missing or currently unavailable.')
    print ('Press any key to restart the program.')
    input()
    os.system('python Green-font-server-hacking.py')
    exit()