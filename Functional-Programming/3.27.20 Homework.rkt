;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname |3.27.20 Homework|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(require 2htdp/universe)
(require 2htdp/batch-io)

; * * * * Ex. 295 - Develop n-inside-playground?, a specification of the random-posns function below. * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ;

; The function generates a predicate that ensures that the length of the given list is some given count
; and that all Posns in this list are within a WIDTH by HEIGHT rectangle:

; distances in terms of pixels 
(define WIDTH 300)
(define HEIGHT 300)
 
; N -> [List-of Posn]
; generates n random Posns in [0,WIDTH) by [0,HEIGHT)
;(check-satisfied (random-posns 3)
  ;               (n-inside-playground? 3))

(define (n-inside-playground? x)
  (cond
    [(and (< (posn-x (first (random-posns x))) WIDTH)
          (< (posn-y (first (random-posns x))) HEIGHT)) (first (random-posns x))]
                                  ))

(define (random-posns n)
  (build-list
    n
    (lambda (i)
      (make-posn (random WIDTH) (random HEIGHT)))))

; Define random-posns/bad that satisfies n-inside-playground? and does not live up to the expectations implied by the above purpose statement. 

; * * * * Ex. 297 - Design the function distance-between. * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ;

; It consumes two numbers and a Posn: x, y, and p.
; The function computes the distance between the points (x, y) and p.

; * * * * Ex. 298 - Design my-animate. * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ;

; Recall that the animate function consumes the representation of a stream of images, one per natural number.
; Since streams are infinitely long, ordinary compound data cannot represent them. Instead, we use functions:

; An ImageStream is a function: 
;   [N -> Image]
; interpretation a stream s denotes a series of images

; Here is a data example:

; ImageStream
(define (create-rocket-scene height)
  (place-image  50 height (empty-scene 60 60)))

; The job of (my-animate s n) is to show the images (s 0), (s 1), and so on at a rate of 30 images per second up to n images total.
; Its result is the number of clock ticks passed since launched.