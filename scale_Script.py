from PIL import Image
import os
from tqdm import tqdm

#Bicubic downsampling function
def resize(input_datei, output_datei):
    # open IMG
    bild = Image.open(input_datei)

    neue_breite = bild.width // 2
    neue_höhe = bild.height // 2

    verkleinertes_bild = bild.resize((neue_breite, neue_höhe), resample=Image.Resampling.BICUBIC)
    verkleinertes_bild.save(output_datei)




#Script for Console
benutzereingabe = input("Start Script\n1 = HR -> LR \n2= LR ->ULR\n==>")
#InsertPaths of folders
HR_PAHT = "HR_Pic"
LR_PATH ="LR_Pic"
ULR_PATH ="ULR_Pic"

if(benutzereingabe =="1"):
    print("Option 1 Starts:")
    for img in tqdm(os.listdir(HR_PAHT)):
        resize(str(HR_PAHT+img) , str(LR_PATH+"LR"+img[2:]))
        
elif benutzereingabe=="2":
        print("Option 2 Starts:")
        for img in tqdm(os.listdir(LR_PATH)):
            resize(str(LR_PATH+img) , str(ULR_PATH+"ULR"+img[2:]))
