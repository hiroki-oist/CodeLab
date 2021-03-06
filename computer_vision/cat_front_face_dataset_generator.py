"""
Detects cat faces in image, crop and save it in folder
"""


import cv2
import os

print('getcwd:      ', os.getcwd())


detector = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
cur_dir = os.getcwd()


import glob
cv_img = []


for img in glob.glob(cur_dir + "/cat_dataset" + "/*.jpg"):
    n = cv2.imread(img)

    print(img)
    #print(img.split("\\")[-1])


    #cv_img.append(n).
    #cv2.imshow("Cat Faces", n)
    #cv2.waitKey(0)


    # load the input image and convert it to grayscale
    image = cv2.imread(img)
    try:
       gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except:
        pass

    rects = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(30, 30))



    ## loop over the cat faces and draw a rectangle
    for (i, (x, y, w, h)) in enumerate(rects):

        image_out = image[y:y+h, x:x+w]


        print(image_out.shape)

        ## Discard smaller than 96x96 images in width or height
        if image_out.shape[0] < 96 or image_out.shape[1] < 96:
            continue


        ## resize the image to be 96x96
        resized = cv2.resize(image_out, (96, 96), interpolation=cv2.INTER_AREA)


        #print("output_data\\" + str(z) + ".jpg")
        cv2.imwrite("output_data\\" + img.split("\\")[-1], resized)



        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)


        cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)



    print("processed: " + img)


    ## show the detected cat faces, uncomment below to show bounding boxes
    #cv2.imshow("Cat Faces", image)
    #cv2.waitKey(0)
    #cv2.waitKey(1)


cv2.destroyAllWindows()

