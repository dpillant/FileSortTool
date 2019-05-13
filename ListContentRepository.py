import glob
import os
from os.path import basename, splitext
from datetime import datetime

outDirectory = "C:/Users/david.pillant/Downloads/rar/"
inDirectory= "C:/Users/david.pillant/Documents/Bibliothèque/Telechargement Code prog/"
programName="Sorting files"

filterFile = ["*.rar","*.zip","*.epub","*.pdf"]

mainKeywordList = [["java","java"],
                   ["java","clean-code"],
                   ["spring","spring"],
                   ["python","python"],
                   ["design-pattern","design-pattern"],
                   ["design-pattern","object-oriented"],
                   ["natural-language","natural-language"],
                   ["excel","excel"],
                   ["excel","tableau"],
                   ["ruby","ruby"],
                   ["adobe","adobe"],
                   ["tensorflow","tensorflow"],
                   ["javascript","javascript"],
                   ["react","react"],
                   ["vue","vue"],
                   ["apache","apache"],
                   ["typescript","typescript"],
                   ["ansible","ansible"],
                   ["kubernetes","kubernetes"],
                   ["nodejs","nodejs"],
                   ["microservices","microservices"],
                   ["opencv","opencv"],
                   ["postgresql","postgresql"],
                   ["cloud","cloud"],
                   ["oracle","oracle"],
                   ["security","security"],
                   ["raspberry","raspberry"],
                   ["mongodb","mongodb"],
                   ["docker","docker"],
                   ["deep-learning","deep-learning"],
                   ["kotlin","kotlin"],
                   ["big-data","big-data"],
                   ["big-data","data-visualization"],
                   ["css","css"],
                   ["html","html"],
                   ["matlab","matlab"],
                   ["swift","swift"],
                   ["gitlab","gitlab"],
                   ["machine-learning","machine-learning"],
                   ["linux","linux"],
                   ["aws","aws"],
                   ["blockchain","blockchain"],
                   ["blockchain","dart"],
                   ["iot","internet-of-things"],
                   ["iot","internet-things"],
                   ["iot","iot"],
                   ["security","security"],
                   ["security","malware"],
                   ["security","securing"],
                   ["security","cracking"],
                   ["security","cyber"],
                   ["architecture","architecture"],
                   ["architecture","design"],
                   ["adobe","illustrator"],
                   ["python","django"],
                   ["mobile","ios"],
                   ["mobile","apple"],
                   ["mobile","android"],
                   ["ia","ia"],
                   ["ia","artificial"],
                   ["ia","ai"],
                   ["architecture","algorithms"],
                   ["go","go"],
                   ["maven","maven"],
                   ["gaming","game"],
                   ["gaming","unity"],
                   ["javascript","d3"],
                   ["javascript","neo4j"],
                   ["blockchain","ethereum"],
                   ["data-science","data-science"],
                   ["mobile","flutter"],
                   ["keras","keras"],
                   ["matpotlib","matpotlib"],
                   ["divers","*"]
                   ]

def organizeFile(file,repository):
    if not (os.path.exists(inDirectory+repository)):
        os.makedirs(inDirectory+repository)
    destination = inDirectory+repository+"/"+file
    source = outDirectory+file
    try:
        os.rename(source,destination)
    except:
        try:
            os.remove(source)
            print("{} deleted!".format(source))
        except (OSError, IOError):
            pass


def start(programName):
    print("*********Start {}****************".format(programName))
    now = datetime.now()
    print("Start at {}".format(now))
    return now

def end(programName,start):
    end=datetime.now()
    duration=start - end
    print("End at {}".format(end))
    print("Durattion {} second(s)".format(duration.seconds))
    print("*********End {}****************".format(programName))

debut = start(programName)
fileCountManaged = 0
for filter in filterFile:
    filePathFiltered=outDirectory+filter
    for filePath in glob.glob(filePathFiltered):
        file = splitext(basename(filePath))
        for mainKeyword in mainKeywordList:
            if (mainKeyword[1] in file[0] or mainKeyword == mainKeywordList[-1]):
                fileCountManaged = fileCountManaged + 1
                organizeFile(file[0]+file[1],mainKeyword[0])
                break

print(str(fileCountManaged) + " file(s) moved!")
end(programName,debut)


