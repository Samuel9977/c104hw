import cv2
solarsystem = cv2.imread("solar-system.jpg")
cv2.imshow("solarsystem",solarsystem)
cv2.putText(solarsystem,"Sun", (20,300),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(solarsystem,"Mercury", (100,300),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(solarsystem,"Venus", (200,300),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(solarsystem,"Earth", (300,300),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(solarsystem,"Mars", (400,300),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(solarsystem,"Jupiter", (500,300),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(solarsystem,"Saturn", (800,300),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(solarsystem,"Uranus", (950,300),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(solarsystem,"Neptune", (1100,300),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.imshow("solarsystem",solarsystem)
cv2.waitKey(0)