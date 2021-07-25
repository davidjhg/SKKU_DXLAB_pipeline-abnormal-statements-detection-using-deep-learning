import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


movs = [file for file in os.listdir('./') if '.mov' in file]
rgbs = sorted([file for file in movs if 'RGB' in file])
thrs = sorted([file for file in movs if 'THR' in file])
rgb2thr = {}
for rgb,thr in zip(rgbs,thrs):
    rgb2thr[rgb] = thr



## frames에서 레이블 생성하는 코드 


drag = False #Mouse가 클릭된 상태 확인용
ix,iy = -1,-1

startX,startY = -1,-1
endX,endY = -1,-1
label_img = None

THR_WIN_NAME = 'THERMAL'
LABEL_WIN_NAME = 'LABEL'


def thermal_on_mouse(event, x, y, flags, param):
    global startX,startY,endX,endY,label_img,drag

    if event == cv2.EVENT_LBUTTONDOWN: #마우스를 누른 상태
        
        startX,startY = x,y
        drag = True
        print(drag,'start',(startX,startY),end='||')
    elif event == cv2.EVENT_MOUSEMOVE: # 마우스 이동
        pass
    elif event == cv2.EVENT_LBUTTONUP:
        if drag:
            endX,endY = x,y
            print(drag,'start',(endX,endY))
            label_img[startY:endY,startX:endX] = 255
            startX,startY,endX,endY = -1,-1,-1,-1
            drag = False
            cv2.imshow(LABEL_WIN_NAME,label_img)



rgbFiles = list(rgb2thr.keys())
dirNames = sorted([file.split('.')[0] for file in rgbFiles]) # frame이 저장된 디렉토리 이름들 
print(dirNames)


for dirName in dirNames:
    cv2.namedWindow(THR_WIN_NAME)
    cv2.namedWindow(LABEL_WIN_NAME)
    cv2.setMouseCallback(THR_WIN_NAME,thermal_on_mouse)


    print('current file --> ',dirName)
    rgbFrameList = [file for file in sorted(os.listdir(dirName)) if 'RGB' in file]
    num2frames = {}
    for file in rgbFrameList:
        num = int(file.split('.')[0][3:])
        num2frames[num] = file
    numbers = sorted(list(num2frames.keys()))
    
    for num in numbers:
        print('[KEY] current key:',num,'/',len(numbers))
        rgbFileName = num2frames[num]
        thrFileName = rgbFileName.replace('RGB','THR')

        frameTH = cv2.imread(dirName+'/'+thrFileName)
        frame = cv2.imread(dirName+'/'+rgbFileName)
        label_img = np.zeros((frameTH.shape[0],frameTH.shape[1],3), np.uint8)

        cv2.imshow('frame',frame)
        cv2.imshow(THR_WIN_NAME,frameTH)
        cv2.imshow(LABEL_WIN_NAME,label_img)


        while True:
            key = cv2.waitKey() & 0xFF
            if key == ord('r'):
                label_img = np.zeros((frameTH.shape[0],frameTH.shape[1],3), np.uint8)
                cv2.imshow(LABEL_WIN_NAME,label_img)
            elif key == ord('n'):
                cv2.imwrite(dirName+'/LAB%d.png'%(num),label_img)
                break
            elif key == ord('q'):
                cv2.destroyAllWindows()
                break
            else:
                continue
        if key == ord('q'):
            break

cv2.destroyAllWindows()