Datensatz Ordner:
	\HR_Pic = Native full rendered Resoution
	\LR_Pic = HR_Pic/2 oder 50% resolution von HR_Pic
	\ULR_Pic= LR_Pic/2 oder 25% resolution von HR_Pic

	Inhalt von HR_Pic, gefüllt mit ".png" Bildern, welche im falle des Projektes aus dem Spiel "Cyberpunk2077" 
	entnommen wurden.

********************************!!WICHTIG!!*******************************
Der Datensatz ist im Git Nicht komplett und 
dient nur zur  veranschaulichung wie der Datensatz aufgebaut ist.
**************************************************************************



**Dateien**
______________________________________________________________________________________________________________________
Main_CNN+Train.ipynb
	Nutzt \HR_Pic und \ULR_Pic um ein Modell zu erstellen

______________________________________________________________________________________________________________________
scale_Script.py :
	Nimmt Bilder aus \HR_Pic oder \LR_Pic je nach Options wahl um bilder um den Faktor 2x zu verkleinern
______________________________________________________________________________________________________________________

Prediction+RenderQueue.ipynb:
	Lädt gewähltes model, welches im Konfigurations absatz gewählt werden kann und Predictet entweder einzelne 
	Bilder oder einen Ganzen Ordern wie Folgend erklärt:	
		In/Output Ordern für Prediction eines Models:
			\Input = ULR_Pic Bilder 
			\Prediction = Ausgabe Ordner für Erzeugtes Modell:
______________________________________________________________________________________________________________________



Video mit AI im einsatz:
https://drive.google.com/file/d/1-2X3wgPN699jQ2Oz6IotdXhUJYOOSHaG/view?usp=sharing