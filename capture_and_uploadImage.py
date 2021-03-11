import cv2
import dropbox
import time
import random


start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    #Initializing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #Read the frames while the camera is on
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"

        #cv2.imwrite() method is usd to save an image to an storage device
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
    return img_name
    print("Snapshot Taken!!")

    #Releases the camera videoCaptureObject.release()
    videoCaptureObject.release()

    #Closes all the window that might be open while this process
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="sl.Asra1XV7CurUgwB0pkVIznw3rivVqLvoWZ55hhpjMmnEa84Krjj0pWvEiJUc5QwMcxlPDtI2lia6ABA2HLzkCLPRig_HXIYeQURRIlmmZkEBh0myMG4GpAtnki5igHlt19rTKU4"
    file=img_counter
    file_from=file
    file_to="/newFolder1"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded!!")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)
main()