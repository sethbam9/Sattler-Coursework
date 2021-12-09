;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |Word Processor Project, Howell|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; Project
; How does the text editor on microsoft word work (WRITE 2 paragraghs DO FRIDAY)
; typesetting, latex, miketex, etc. -> 2 philosophies that Mircosoft chooses inbetween (what you see is what you get, vs. the text itself)
; TERMS : text-editor / word processor / typesetting program (Miktex)
; Create a text editor -> 1 sentence in 1 sentence out 
 ;; Plan the process (by Tuesday) - what do I want it to do? 
 ;; Exercise 31 (U1 Ch2) & Ex. 177-180 (U2 Ch10)

(define (change i a-key)
  (cond
	[(key=? a-key "left")  (make-game (game-ufos i) (move-left (game-tank i)) (game-missiles i) (game-comets i) (game-time i))]
	[(key=? a-key "right") (make-game (game-ufos i) (move-right (game-tank i)) (game-missiles i) (game-comets i) (game-time i))]
	[(key=? a-key " ") (make-game (game-ufos i) (game-tank i) (missilefire (game-missiles i) (tank-loc (game-tank i))) (game-comets i) (game-time i))]
	[else i]))

Have enter and backspace as conditions, then else statement to run function where key-event inserts character
*convert to int and use askii values if needed 