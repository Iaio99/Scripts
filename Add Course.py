#!/usr/bin/python
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('COURSE', help="course's folder")
parser.add_argument('CODE', help="code of curse")
parser.add_argument("-v","--video", help="add Videolezioni folder", action="store_true")
parser.add_argument("-e","--exercises", help="add Esercizi folder", action="store_true")
parser.add_argument("-t","--tutoring", help="add Tutoraggio folder", action="store_true")
parser.add_argument("-x","--examples", help="add Esempi folder", action="store_true")

args = parser.parse_args()

if __name__ == '__main__':

    os.chdir("/home/Giuliano/Documenti/Uni")
    try:
        os.mkdir(args.COURSE)
    except FileExistsError:
        print("La cartella del corso esiste già")
        exit()
    
    os.chdir(args.COURSE)

    file = open(("Appunti %s.tex" %  args.CODE.upper()),"x")
    file.close()

    os.mkdir("Dispense")

    if args.video:
        os.mkdir("Videolezioni")
    
    if args.examples:
        os.mkdir("Esempi")

    if args.exercises:
        os.mkdir("Esercizi")
    
    if args.tutoring:
        os.mkdir("Tutoraggio")