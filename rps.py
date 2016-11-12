from random import randint
import cv2
import numpy
t=["rock", 'paper', 'scissors']
player=False
while player==False:
	rnd=randint(0,2)
	computer=t[rnd]
	player=1
	raw_input()
#account for multiple hand positions rock=0,1 paper=4,5 scissors=2,3
	if computer=='rock':

		img = cv2.imread('rock.png',0)
		if player==1 or player==0:
			cv2.putText(img,"Tie!!!", (750,400), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
		elif player==2 or player==3:
			cv2.putText(img,"You Lose!!!", (750,400), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
		elif player==5 or player==4: 
			cv2.putText(img,"You Win!!!", (750,400), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
		else:
			img=cv2.imread('Harambe.jpg')
		cv2.imshow('image',img)
		cv2.waitKey(500)
		cv2.destroyAllWindows()
	elif computer=='paper':
		img = cv2.imread('paper.png',0)
		if player==5 or player==4:
			cv2.putText(img,"Tie!!!", (1150,300), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
		elif player==1 or player==0:
			cv2.putText(img,"You Lose!!!", (1150,300), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
		elif player==2 or player==3:
			cv2.putText(img,"You Win!!!", (1150,300), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
		else:
			img=cv2.imread('Harambe.jpg')
		cv2.imshow('image',img)
		cv2.waitKey(500)
		cv2.destroyAllWindows()
	else:
		img = cv2.imread('scissors.jpg',0)
		if player==2 or player==3:
			cv2.putText(img,"Tie!!!", (1150,300), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
		elif player==5 or player==4:
			cv2.putText(img,"You Lose!!!", (1150,300), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
		elif player==1 or player==0:
			cv2.putText(img,"You Win!!!", (1150,300), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
		else:
			img=cv2.imread('Harambe.jpg')
		cv2.imshow('image',img)
		cv2.waitKey(500)
		cv2.destroyAllWindows()
	player=False