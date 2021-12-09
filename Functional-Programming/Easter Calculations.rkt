;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |Easter Calendar|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; Julian Calculation
(define year 2020)
(define juliA (modulo year 4))
(define juliB (modulo year 7))
(define juliC (modulo year 19))
(define juliD (modulo (+ (* 19 juliC) 15) 30))
(define juliE (modulo (+ (* 2 juliA) (* 4 juliB) 34 (* -1 juliD)) 7))

(define juliMonth (floor (/ (+ (modulo (+ (* 19 juliC) 15) 30) juliE 114) 31)))
(define juliDay (+ (modulo (+ juliD juliE 114) 31) 1))

; Orthodox Calculation
  var a = modulo year 19;
    var b = modulo year 7;
    var c = modulo year 4;

    var d = (modulo (+ (* 19 (modulo year 19)) 16) 30);
    var e = modulo (+ (* 2 (modulo year 4)) (* 4 (modulo year 7)) (* 6 (modulo (+ (* 19 (modulo year 19)) 16) 30)) 7);

    var key = (+ (modulo (+ (* 19 (modulo year 19)) 16) 30) ( modulo (+ (* 2 (modulo year 4)) (* 4 (modulo year 7)) (* 6 (modulo (+ (* 19 (modulo year 19)) 16) 30)) 7)) 3);
    orthoMonth = (key > 30) ? 5 : 4;
    orthoDay = (key > 30) ? key - 30 : key;

; Gregorian Calculation 

(define gregA (modulo year 19))
(define gregB (floor (/ year 100)))
(define gregC (modulo year 100))
(define gregD (floor (/ gregB 4)))
(define gregE (modulo gregB 4))
(define gregF (floor (/ (+ gregB 8) 25)))
(define gregG (floor (/ (- gregB gregF -1) 3)))
(define gregH (modulo (+ (* 19 gregA) gregB (* -1 gregD) (* -1 gregG) 15) 30))
(define gregI (floor (/ gregC 4)))
(define gregJ (modulo gregC 4))
(define gregK (modulo (+ 32 (* 2 gregE) (* 2 gregI) (* -1 gregH) (* -1 gregJ)) 7))
(define gregL (floor (/ (+ gregA (* 11 gregH) (* 22 gregK)) 451)))

(define gregMonth (floor (/ (+ gregH gregK (* -7 gregL) 114) 31)))
(define gregDay (+ (modulo (+ gregH gregK (* -7 gregL) 114) 31) 1))

; num -> string
; convert the days and months to strings for printing
(define gM (number->string gregMonth))
(define gD (number->string gregDay))
(define jM (number->string juliMonth))
(define jD (number->string juliDay))

; string -> string
; append day and month and display to user
(define (main calType year)
  
  (cond
    [(string=? "julian" calType) (string-append jM "/" jD)]
    [(string=? "gregorian" calType) (string-append gM "/" gD)]
    )
  )
