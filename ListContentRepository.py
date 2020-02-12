import glob
import os
import re
import shutil
from os.path import basename, splitext
from datetime import datetime

outDirectory = "C:/Users/david.pillant/Downloads/rar/"
inDirectory= "E:/Bibliotheque/"
programName="Sorting files"
                   ["cucumber","cucumber"],
                   ["dark-web","dark-web"],
                   ["data-mining","mining"],
                   ["data-science","science"],
                   ["deep-learning","deep"],
                   ["design-pattern","pattern"],
                   ["design-pattern","design"],
                   ["design-pattern","object-oriented"],
                   ["devops","devops"],
                   ["docker","docker"],
                   ["elk","elasticsearch"],
                   ["elk","elastic"],
                   ["elk","kibana"],
                   ["elk","logstach"],
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
                   ["iot","things"],
                   ["iot","iot"],
                   ["java","java"],
                   ["java","clean"],
                   ["java","code"],
                   ["java","coder"],
                   ["java","jakarta-ee"],
                   ["javascript","javascript"],
                   ["javascript","d3"],
                   ["javascript","js"],
                   ["javascript","neo4j"],
                   ["javascript","rxjs"],
                   ["javascript","sveltejs"],
                   ["jhipster","jhipster"],
                   ["jira","jira"],
                   ["kafka","kafka"],
                   ["keras","keras"],
                   ["kotlin","kotlin"],
                   ["kubernetes","kubernetes"],
                   ["linear-algebra","algebra"],
                   ["linux","linux"],
                   ["linux","ubuntu"],
                   ["linux","redhat"],
                   ["linux","vim"],
                   ["lua","lua"],
                   ["machine-learning","machine"],
                   ["matlab","matlab"],
                   ["matplotlib","matplotlib"],
                   ["maven","maven"],
                   ["microservices","microservices"],
                   ["mobile","ios"],
                   ["mobile","apple"],
                   ["mobile","android"],
                   ["mobile","flutter"],
                   ["mongodb","mongodb"],
                   ["natural-language","natural"],
                   ["network","network"],
                   ["network","tcp-ip"],
                   ["nginx","nginx"],
                   ["nodejs","nodejs"],
                   ["nodejs","mern"],
                   ["odoo","odoo"],
                   ["opencv","opencv"],
                   ["oracle","oracle"],
                   ["perl","perl"],
                   ["postgresql","postgresql"],
                   ["postman","postman"],
                   ["puppet","puppet"],
                   ["pycharm","pycharm"],
                   ["python","python"],
                   ["python","django"],
                   ["rabbit mq","rabbit"],
                   ["raspberry","raspberry"],
                   ["react","react"],
                   ["redis","redis"],
                   ["reseau","network"],
                   ["reseau","networking"],
                   ["reseau","vpn"],
                   ["rpa","rpa"],
                   ["ruby","ruby"],
                   ["rust","rust"],
                   ["salesforce","salesforce"],
                   ["scratch","scratch"],
                   ["security","security"],
                   ["security","malware"],
                   ["security","securing"],
                   ["security","cracking"],
                   ["security","cyber"],
                   ["security","cybersecurity"],
                   ["security","hacker"],
                   ["security","hacking"],
                   ["selenium","selenium"],
                   ["spark","spark"],
                   ["spring","spring"],
                   ["sql","sql"],
                   ["swift","swift"],
                   ["tensorflow","tensorflow"],
                   ["tomcat","tomcat"],
                   ["typescript","typescript"],
                   ["vmware","vmware"],
                   ["vue","vue"],
                   ["windows","windows"],
                   ["wordpress","wordpress"],
                   ["divers","*"]
                   ]


def organize_file(file,repository):
    if not (os.path.exists(inDirectory+repository)):
        os.makedirs(inDirectory+repository)
    destination = inDirectory+repository+"/"+file
    source = outDirectory+file
    try:
        shutil.move(source,destination)
    except OSError as e :
        print ("error({0}): {1}".format(e.errno, e.strerror))
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
    duration= end - start
    print("End at {}".format(end))
    print("Duration {} second(s)".format(duration.total_seconds()))
    print("*********End {}****************".format(program_name))

debut = start(programName)
fileCountManaged = 0

for filter in filterFile:
    filePathFiltered=outDirectory+filter
    for filePath in glob.glob(filePathFiltered):

        moved = False
        file = splitext(basename(filePath))
        keywordFile = file[0].replace(".","-").split("-")
        # 1- on vérifie si le couple de mots clés dans le titre du doc
        for mainKeyword in mainKeywordList:
            if (mainKeyword[1] in keywordFile and mainKeyword[0] in keywordFile):
                fileCountManaged = fileCountManaged + 1
                organize_file(file[0]+file[1],mainKeyword[0])
                moved = True
                break

        #2- on vérifie si le 2eme mot clé est dans le titre du mot
        if not (moved):
            for mainKeyword in mainKeywordList:
                if (mainKeyword[1] in keywordFile):
                    fileCountManaged = fileCountManaged + 1
                    organize_file(file[0]+file[1],mainKeyword[0])
                    moved = True
                    break
        #3 on vérifie si le mot clé est contenu dans le titre du fichier
        if not (moved):
            for mainKeyword in mainKeywordList:
                if (mainKeyword[1] in file[0] or mainKeyword == mainKeywordList[-1]):
                    fileCountManaged = fileCountManaged + 1
                    organize_file(file[0]+file[1],mainKeyword[0])
                    break

print(str(fileCountManaged) + " file(s) moved!")
end(programName,debut)


