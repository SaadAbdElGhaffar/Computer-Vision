import cv2  # import opencv

cap = cv2.VideoCapture(0)  #  your laptop camera / or set the path of video like 'saad.mp4'
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # use any fourcc type to improve quality for the saved video
out = cv2.VideoWriter("data/output.avi", fourcc, 20.0, (640, 480))  # Video settings 20 frame per sec

print(cap.isOpened())  # check if the camera is opened
while cap.isOpened():  # while loop to read all frames
    ret, frame = (cap.read())  # read all frams if ret is TRUE it means that there is a frames to process
    if ret == True:  # if ret is true
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # get the frame width
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # get the frame height

        out.write(frame)  # save your video

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert frames from BGR2GRAY
        cv2.imshow("frame", gray)  # show the frames

        if cv2.waitKey(1) & 0xFF == ord(
            "q"
        ):  # if u pressed q close the window and break
            break
    else:  # it will enter here if the ret = false and break the code
        break

cap.release()  # close the camera after u finish the running process
out.release()  # release your video after u save it
cv2.destroyAllWindows()  # close any opened window
