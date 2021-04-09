from RPi import GPIO
import os
import sys




def setup():

    #Find out our pid so we can remap to cpu 3
    mypid=os.getpid()  # Get the process ID of the current procss
    myppid=os.getppid() # Get the parent process ID of the curent process

    print("My pid is ", mypid)

    print('Setting cpu affinity to cpu 3')
    select_cpu="sudo taskset  -cp 3 "
    print('Setting priority to -20')
    set_priority="sudo renice -n -20 -p "   #用戶為100到139。好的值範圍是-20到+19，其中-20最高，0默認，+ 19最低。

    #Call out to the os to remap the cpu and set priority high
    ret=os.system(set_priority+str(mypid))
    ret=os.system(select_cpu+str(mypid))

    sys.setcheckinterval(1000); ##no Python threading so just let Python run for a long time

setup()

try:

    while True:                             #busy work for Python main loop to do
        if counter != lastcounter:
            lastcounter=counter
            sys.stdout.write("\r" + str(counter) + "   \r")
            sys.stdout.flush()

except KeyboardInterrupt:
      print("Ctl C pressed - ending program") 