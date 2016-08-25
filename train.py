# -*- coding: utf-8 -*-
import capchaEn
import os,time

FONTNAME = "VeraMoBd".lower()
LANG = FONTNAME[:3]
NUMS = 10000
DIR = "./trainingfile/"

class TrainsCapcha(object):

    def __init__(self):
        self.temp_filename = DIR + "tempfile"
        
    def get_pic(self, c, pic_name):
        return c.createChecker(DIR + pic_name)[0]
        
    def modify_box(self, file_name, name, box_name, t):
        cmd = " cd %s && tesseract %s %s batch.nochop makebox" % (DIR, file_name, name)
        os.system(cmd)
        f = open(DIR + box_name)
        self.f_temp = open(self.temp_filename, 'w')
        i = 0
        for line in f:
            line = line.split()
            line[0] = t[i]
            i = i + 1
            #print(" ".join(line))
            self.f_temp.write(" ".join(line) + '\n')
        f.close()
        self.f_temp.close()
        cmd = "mv %s %s" % (self.temp_filename, DIR + box_name)
        #print("mv file:", cmd)
        os.system(cmd)
    
    def trains(self):
        c = capchaEn.picChecker()
        trs = []
        boxs = []
        for num in range(NUMS):
            name = LANG + "." + FONTNAME + "." + "exp" + str(num)
            file_name = name + ".tif"
            tr_name = name + ".tr"
            trs.append(tr_name)
            box_name = name + ".box"
            boxs.append(box_name)
            t = self.get_pic(c, file_name)
            time.sleep(0.01)
            #print(num, ": t:",t)
            self.modify_box(file_name, name, box_name, t)
            cmd = "cd %s && tesseract %s %s nobatch box.train" % (DIR, file_name, name)
            os.system(cmd)
            
        #print(" ".join(boxs))
        #print(" ".join(files))
        
        #unicharset_extractor
        cmd = "cd %s && unicharset_extractor %s" % (DIR, " ".join(boxs))
        os.system(cmd)
        time.sleep(1)
        
        #mftraining
        cmd = "cd %s && mftraining -F font_properties -U unicharset -O %s.unicharset %s" % (DIR, LANG, " ".join(trs))
        os.system(cmd)
        time.sleep(1)
        
        #cntraining
        cmd = "cd %s && cntraining %s" % (DIR, " ".join(trs))
        os.system(cmd)
        time.sleep(1)
        
        #combine_tessdata
        cmd = "cd %s && mv normproto %s.normproto && mv inttemp %s.inttemp  && mv pffmtable %s.pffmtable  && mv shapetable %s.shapetable  && combine_tessdata %s." % (DIR, LANG , LANG, LANG, LANG, LANG)
        os.system(cmd)
        
        #"/usr/local/Cellar/tesseract/3.02.02_3/share/tessdata/"
            
        
    
if __name__ == '__main__':
    tc = TrainsCapcha()
    tc.trains()