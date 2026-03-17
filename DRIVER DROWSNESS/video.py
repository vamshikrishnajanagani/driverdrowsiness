from imutils.video import VideoStream
import argparse
import cv2
while True:
 state="Normal"
 ap = argparse.ArgumentParser()
 ap.add_argument("-w", "--webcam", type=int, default=0,help="index of webcam on system")
 args = vars(ap.parse_args())
 vs = VideoStream(src=args["webcam"]).start()
 frame=vs.read()
 gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
 cv2.imshow("Video",gray)
 key=cv2.waitKey(1)
 if key==ord('q'):
  break
cv2.destroyAllWindows()
vs.stop()
