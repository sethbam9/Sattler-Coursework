;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |CH. 8 Notes|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(require 2htdp/universe)
(require 2htdp/batch-io) 

; CH. 8 NOTES -> LISTS

; 8.1
; (cons String List-of-names)
(define myLife 
         (cons "homies" (cons "Dan" (cons "Kenny" (cons "Maykel" '())))

  ))

; 8.2
(define-struct pair [left right])
; A ConsPair is a structure:
;   (make-pair Any Any)
; Any Any -> ConsPair
; Any Any -> ConsOrEmpty
(define (our-cons a-value a-list)
  (cond
    [(empty? a-list) (make-pair a-value a-list)]
    [(pair? a-list) (make-pair a-value a-list)]
    [else (error "cons: second argument ...")]))
; ConsOrEmpty -> Any
; extracts the left part of the given pair
(define (our-first a-list)
  (if (empty? a-list)
      (error 'our-first "...")
      (pair-left a-list)))

                         
;; Fg. 47
; List-of-names -> Boolean
; determines whether "Flatt" occurs on alon

(define (contains-name? alon name)
  (cond
    [(empty? alon) #false]
    [(cons? alon)
     (or (string=? (first alon) name)
         (contains-name? (rest alon) name))]))

;(make-layer "pink" (make-layer "black" "white"))

; CH. 9 NOTES -> SELF-REFERENTIAL DATA DEFINITIONS

;; Fg. 55
 ; calculates number of strings in list
(define (how-many alos)
  (cond
    [(empty? alos) 0]
    [else (+ (how-many (rest alos)) 1)]))

;; Ex. 138
 ; adds values of each list element. 
(define (sum lonum)
  (cond
    [(empty? lonum) 0]
    [else (+ (sum (rest lonum)) (first lonum))]))

;; Fg. 59
(define (copier n s)
  (cond
    [(zero? n) '()]
    [(positive? n) (cons s (copier (sub1 n) s))]))

(define (copier.v2 n s)
  (cond
    [(zero? n) '()]
    [else (cons s (copier.v2 (sub1 n) s))]))

;; Ex. 152
(define bGreen (rectangle 10 15 "solid" "green"))
(define (imgCopier n img)
  (cond
    [(zero? n) '()]
    [(positive? n) (cons img (copier (sub1 n) img))]))

;; Fg. 61

(define HEIGHT 220) ; distances in terms of pixels 
(define WIDTH 30)
(define XSHOTS (/ WIDTH 2.5))
 
; graphical constants 
(define BACKGROUND (rectangle WIDTH HEIGHT "solid" "green"))
(define SHOT (rectangle 5 10 "solid" "black"))

; ShotWorld -> ShotWorld 
(define (main w0)
  (big-bang w0
    [on-tick tock]
    [on-key keyh]
    [to-draw to-image]))
 
; ShotWorld -> ShotWorld 
; moves each shot up by one pixel 
(define (tock w)
  (cond
    [(empty? w) '()]
    [else (cons (sub1 (first w)) (tock (rest w)))]))
 
; ShotWorld KeyEvent -> ShotWorld 
; adds a shot to the world if the space bar is hit 
(define (keyh w ke)
  (if (key=? ke " ") (cons HEIGHT w) w))
 
; ShotWorld -> Image 
; adds each shot y on w at (XSHOTS,y} to BACKGROUND
(define (to-image w)
  (cond
    [(empty? w) BACKGROUND]
    [else (place-image SHOT XSHOTS (first w)
                       (to-image (rest w)))]))

;; 9.6 SETS and Lists
; List-of-string String -> N
; determines how often s occurs in los
(define (count los s)
  0)

; Son
(define es '())
 
; Number Son -> Boolean
; is x in s
(define (in? x s)
  (member? x s))

; Number Son.L -> Son.L
; removes x from s 
(define s1.L
  (cons 1 (cons 1 '())))

(define (set-.L x s)
  (remove-all x s))

; Number Son.R -> Son.R
; removes x from s
(define s1.R
  (cons 1 '()))

(define (set-.R x s)
  (remove x s))

; Number Son -> Son
; subtracts x from s 
(define (set- x s)
  s)

(define set123-version1
  (cons 1 (cons 2 (cons 3 '()))))
 
(define set123-version2
  (cons 1 (cons 3 (cons 2 '()))))

(define set23-version1
  (cons 2 (cons 3 '())))
 
(define set23-version2
  (cons 3 (cons 2 '())))

(check-member-of (set-.v1 1 set123.v1)
                 set23-version1
                 set23-version2)

; Son -> Boolean
; #true if 1 a member of s;  #false otherwise
(define (not-member-1? s)
  (not (in? 1 s)))

