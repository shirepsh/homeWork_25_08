import time
import datetime 

def live_clock (): 
    """
    we get the current sec, min, hours for the prog
    """
    while True:
      print (datetime.datetime.now().strftime("%H:%M:%S"), end= "\r")

def main():
    live_clock()

if __name__ == "__main__":
    main()

 
 