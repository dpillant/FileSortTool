import glob
import os
from os.path import basename, splitext
from datetime import datetime

outDirectory = "C:/Users/david.pillant/Downloads/rar/"
inDirectory= "C:/Users/david.pillant/Documents/Bibliothèque/Telechargement Code prog/"
programName="Sorting files"

filterFile = ["*.rar","*.zip","*.epub","*.pdf"]
mainKeywordList = [["3d-graphics","3d-graphics"],
                   ["adobe","adobe"],
                   ["adobe","illustrator"],
                   ["adobe","photoshop"],
                   ["agilite","agile"],
                   ["agilite","lean"],
                   ["architecture","architecture"],
                   ["architecture","design"],
                   ["architecture","pattern"],
                   ["architecture","algorithms"],
                   ["ansible","ansible"],
                   ["apache","apache"],
                   ["aws","aws"],
                   ["big-data","big-data"],
                   ["big-data","data-visualization"],
                   ["blockchain","blockchain"],
                   ["blockchain","dart"],
                   ["blockchain","ethereum"],
                   ["bpmn","process"],
                   ["bpmn","bpmn"],
                   ["camel","camel"],
                   ["cloud","cloud"],
                   ["css","css"],
                   ["cucumber","cucumber"],
                   ["data-mining","data-mining"],
                   ["data-science","data-science"],
                   ["deep-learning","deep-learning"],
                   ["design-pattern","design-pattern"],
                   ["design-pattern","object-oriented"],
                   ["docker","docker"],
                   ["elixir","elixir"],
                   ["excel","excel"],
                   ["excel","tableau"],
                   ["excel","spreadsheet"],
                   ["firebase","firebase"],
                   ["gaming","game"],
                   ["gaming","unity"],
                   ["general database","database"],
                   ["github","github"],
                   ["github","git"],
                   ["gitlab","gitlab"],
                   ["go","go"],
                   ["graph","graph"],
                   ["graph","graphql"],
                   ["hardware","hardware"],
                   ["hardware","computer"],
                   ["hardware","computing"],
                   ["html","html"],
                   ["ia","ia"],
                   ["ia","artificial"],
                   ["ia","ai"],
                   ["iot","internet-of-things"],
                   ["iot","internet-things"],
                   ["iot","iot"],
                   ["java","java"],
                   ["java","clean-code"],
                   ["javascript","javascript"],
                   ["javascript","d3"],
                   ["javascript","neo4j"],
                   ["javascript","rxjs"],
                   ["javascript","sveltejs"],
                   ["keras","keras"],
                   ["kotlin","kotlin"],
                   ["kubernetes","kubernetes"],
                   ["linear-algebra","linear-algebra"],
                   ["linux","linux"],
                   ["linux","ubuntu"],
                   ["linux","redhat"],
                   ["linux","red-hat"],
                   ["machine-learning","machine-learning"],
                   ["matlab","matlab"],
                   ["matplotlib","matplotlib"],
                   ["maven","maven"],
                   ["microservices","microservices"],
                   ["mobile","ios"],
                   ["mobile","apple"],
                   ["mobile","android"],
                   ["mobile","flutter"],
                   ["mongodb","mongodb"],
                   ["natural-language","natural-language"],
                   ["nginx","nginx"],
                   ["nodejs","nodejs"],
                   ["nodejs","mern"],
                   ["odoo","odoo"],
                   ["opencv","opencv"],
                   ["oracle","oracle"],
                   ["perl","perl"],
                   ["postgresql","postgresql"],
                   ["python","python"],
                   ["python","django"],
                   ["raspberry","raspberry"],
                   ["react","react"],
                   ["reseau","network"],
                   ["reseau","networking"],
                   ["ruby","ruby"],
                   ["scratch","scratch"],
                   ["security","security"],
                   ["security","malware"],
                   ["security","securing"],
                   ["security","cracking"],
                   ["security","cyber"],
                   ["security","cybersecurity"],
                   ["security","hacker"],
                   ["security","hacking"],
                   ["spring","spring"],
                   ["sql","sql"],
                   ["swift","swift"],
                   ["tensorflow","tensorflow"],
                   ["tomcat","tomcat"],
                   ["typescript","typescript"],
                   ["vmware","vmware"],
                   ["vue","vue"],
                   ["windows","windows"],
                   ["divers","*"]
                   ]


def organize_file(file,repository):
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


def start(program_name):
    print("*********Start {}****************".format(program_name))
    now = datetime.now()
    print("Start at {}".format(now))
    return now

def end(program_name,start):
    end=datetime.now()
    duration=start - end
    print("End at {}".format(end))
    print("Duration {} second(s)".format(duration.seconds))
    print("*********End {}****************".format(program_name))

debut = start(programName)
fileCountManaged = 0
for filter in filterFile:
    filePathFiltered=outDirectory+filter
    for filePath in glob.glob(filePathFiltered):
        file = splitext(basename(filePath))
        for mainKeyword in mainKeywordList:
            if (mainKeyword[1] in file[0] or mainKeyword == mainKeywordList[-1]):
                fileCountManaged = fileCountManaged + 1
                organize_file(file[0]+file[1],mainKeyword[0])
                break

print(str(fileCountManaged) + " file(s) moved!")
end(programName,debut)


