;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |CyberTruck Wheels Spin|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(require 2htdp/universe)
(require 2htdp/batch-io)

;CAR PROBLEM
(define WIDTH-OF-WORLD 1000)
(define CARBACKGROUND (empty-scene WIDTH-OF-WORLD 140))
(define WHEEL-RADIUS 20)
(define WHEEL-DISTANCE (* WHEEL-RADIUS 5))
(define CAR-FRAME (+ (* WHEEL-RADIUS 6) WHEEL-DISTANCE))
(define CAR-HOOD (* CAR-FRAME .5))
(define CAR-WINDOW (* CAR-HOOD .9))
 
(define (WHEEL mv t)
  (rotate (* -1 (movexang-ang mv) t) (add-line (circle WHEEL-RADIUS "solid" "black")
            (* WHEEL-RADIUS 1.8) (* WHEEL-RADIUS .8) (* WHEEL-RADIUS .8) (* WHEEL-RADIUS 1.8) "gray")))

(define SPACE
  (rectangle WHEEL-DISTANCE WHEEL-RADIUS "solid" "transparent"))
;- CAR-FRAME (* WHEEL-RADIUS 2)

(define (BOTH-WHEELS mv t)
  (beside (WHEEL mv t) SPACE (WHEEL mv t)))

(define CAR-BODY
  (overlay/offset (isosceles-triangle CAR-HOOD 120 "solid" "blue") 0 (* WHEEL-RADIUS 1) (rectangle CAR-FRAME (* WHEEL-RADIUS 2) "solid" "blue")))

(define (CyberTruck mv t) (overlay/offset (BOTH-WHEELS mv t) 0 (- 0 WHEEL-RADIUS) CAR-BODY))

(define-struct movexang [x ang])
(define m (make-movexang 3 100))

; (define SportsCar .)
; (define MuscleCar .)
; (define SuvCar . )

(define (CarMain t)
   (big-bang t
     [on-tick tock]
     [on-mouse hyper]
     [to-draw render]))

;(define (tock x) (+ x 3))
(define (tock t) (+ t (movexang-x m)))

(define (hyper t x-mouse y-mouse me)
  (cond
    [(string=? "button-down" me) x-mouse]
    [else t]))

(define (render t)
    (place-image (CyberTruck m t) (* t (movexang-x m)) 80 CARBACKGROUND))

;(define-struct CyberParts (wheel, xpos)