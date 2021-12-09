;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |Functional Calendar|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; JULIAN CALCULATION
; Math taken from https://en.wikipedia.org/wiki/Computus#Anonymous_Gregorian_algorithm

;; Julian month algorithm
(check-expect (juliMonth 2020) "4")
(check-expect (juliMonth 1933) "4")
(check-expect (juliMonth 2741) "4")

(define (juliMonth year) (number->string ; turn month output into a string
                         (floor (/
                                 (+
                                   (modulo (+ (* 19 (modulo year 19)) 15) 30)
                                   (modulo (+ (* 2 (modulo year 4)) (* 4 (modulo year 7)) 34 (* -1 (modulo (+ (* 19 (modulo year 19)) 15) 30))) 7)
                                   114)
                                 31))
                         )
  )

;; Julian day algorithm
(check-expect (juliDay 2020) "6")
(check-expect (juliDay 1933) "3")
(check-expect (juliDay 2741) "15")

(define (juliDay year) (number->string ; turn day output into a string
                        (+
                         (modulo
                           (+
                             (modulo (+ (* 19 (modulo year 19)) 15) 30)
                             (modulo (+ (* 2 (modulo year 4)) (* 4 (modulo year 7)) 34 (* -1 (modulo (+ (* 19 (modulo year 19)) 15) 30))) 7)
                             114)
                            31)
                         1)
                        )
  )

; REVISED JULIAN (ORTHODOX) CALCULATION
; Math taken from https://blog.georgekosmidis.net/2013/04/28/c-calculating-orthodox-and-catholic-easter/

;; Orthodox month algorithm
(check-expect (orthoMonth 2020) "4")
(check-expect (orthoMonth 2087) "4")
(check-expect (orthoMonth 2741) "5")

(define (orthoMonth year) (number->string ; turn day output into a string
                           (cond
                             [(> (+
               (modulo (+ (* 19 (modulo year 19)) 16) 30) ;f 
               (modulo (+ (* 2 (modulo year 4)) (* 4 (modulo year 7)) ;e
                           (* 6 (modulo (+ (* 19 (modulo year 19)) 16) 30))) ;d
                       7) 
               3)
                                 30) 5]
                             [else 4]
                             )
                           )
  )

;; Orthodox day algorithm
(check-expect (orthoDay 2020) "19")
(check-expect (orthoDay 2087) "27")
(check-expect (orthoDay 2741) "4")

(define (orthoDay year) (number->string ; turn day output into a string
                           (cond
                             [(> (+
               (modulo (+ (* 19 (modulo year 19)) 16) 30) ;f 
               (modulo (+ (* 2 (modulo year 4)) (* 4 (modulo year 7)) ;e
                           (* 6 (modulo (+ (* 19 (modulo year 19)) 16) 30))) ;d
                       7) 
               3)
                                 30) (- (+
               (modulo (+ (* 19 (modulo year 19)) 16) 30) ;f 
               (modulo (+ (* 2 (modulo year 4)) (* 4 (modulo year 7)) ;e
                           (* 6 (modulo (+ (* 19 (modulo year 19)) 16) 30))) ;d
                       7) 
               3) 30)]
                             [else (+
               (modulo (+ (* 19 (modulo year 19)) 16) 30) ;f 
               (modulo (+ (* 2 (modulo year 4)) (* 4 (modulo year 7)) ;e
                           (* 6 (modulo (+ (* 19 (modulo year 19)) 16) 30))) ;d
                       7) 
               3)]
                             )
                           )
  )

; GREGORIAN CALCULATION
; Math taken from https://en.wikipedia.org/wiki/Computus#Anonymous_Gregorian_algorithm

;; Gregorian month algorithm
(check-expect (gregMonth 2016) "3")
(check-expect (gregMonth 1981) "4")
(check-expect (gregMonth 1737) "4")

(define (gregMonth year) (number->string ; turn month output into a string
                          (floor (/
                                  (+
                                   (modulo (+ (* 19 (modulo year 19)) (floor (/ year 100)) ; gH
                                                  (* -1 (floor (/ (floor (/ year 100)) 4)))
                                                  (* -1 (floor (/ (- (floor (/ year 100)) (floor (/ (+ (floor (/ year 100)) 8) 25)) -1) 3))) ;gregG
                                                  15) 30)
                                   (modulo (+ 32 (* 2 (modulo (floor (/ year 100)) 4)) ;gK
                                              (* 2 (floor (/ (modulo year 100) 4)))
                                              (* -1 (modulo (+ (* 19 (modulo year 19)) (floor (/ year 100)) ; gH
                                                  (* -1 (floor (/ (floor (/ year 100)) 4)))
                                                  (* -1 (floor (/ (- (floor (/ year 100)) (floor (/ (+ (floor (/ year 100)) 8) 25)) -1) 3))) ;gregG
                                                  15) 30))
                                              (* -1 (modulo (modulo year 100) 4))) 7)
                                   (* -7 (floor (/ (+ (modulo year 19)
                                                      (* 11 (modulo (+ (* 19 (modulo year 19)) (floor (/ year 100)) ; gH
                                                  (* -1 (floor (/ (floor (/ year 100)) 4)))
                                                  (* -1 (floor (/ (- (floor (/ year 100)) (floor (/ (+ (floor (/ year 100)) 8) 25)) -1) 3))) ;gregG
                                                  15) 30))
                                                      (* 22 (modulo (+ 32 (* 2 (modulo (floor (/ year 100)) 4)) ;gK
                                              (* 2 (floor (/ (modulo year 100) 4)))
                                              (* -1 (modulo (+ (* 19 (modulo year 19)) (floor (/ year 100)) ; gH
                                                  (* -1 (floor (/ (floor (/ year 100)) 4)))
                                                  (* -1 (floor (/ (- (floor (/ year 100)) (floor (/ (+ (floor (/ year 100)) 8) 25)) -1) 3))) ;gregG
                                                  15) 30))
                                              (* -1 (modulo (modulo year 100) 4))) 7))) 451)))
                                   114)
                                  31))
                          )
  )
  
;; Gregorian day algorithm
(check-expect (gregDay 2016) "27")
(check-expect (gregDay 1981) "19")
(check-expect (gregDay 1737) "21")

(define (gregDay year) (number->string ; turn day output into a string
                          (+
                           (modulo
                            (+
                                   (modulo (+ (* 19 (modulo year 19)) (floor (/ year 100)) ; gH
                                                  (* -1 (floor (/ (floor (/ year 100)) 4)))
                                                  (* -1 (floor (/ (- (floor (/ year 100)) (floor (/ (+ (floor (/ year 100)) 8) 25)) -1) 3))) ;gregG
                                                  15) 30)
                                   (modulo (+ 32 (* 2 (modulo (floor (/ year 100)) 4)) ;gK
                                              (* 2 (floor (/ (modulo year 100) 4)))
                                              (* -1 (modulo (+ (* 19 (modulo year 19)) (floor (/ year 100)) ; gH
                                                  (* -1 (floor (/ (floor (/ year 100)) 4)))
                                                  (* -1 (floor (/ (- (floor (/ year 100)) (floor (/ (+ (floor (/ year 100)) 8) 25)) -1) 3))) ;gregG
                                                  15) 30))
                                              (* -1 (modulo (modulo year 100) 4))) 7)
                                   (* -7 (floor (/ (+ (modulo year 19)
                                                      (* 11 (modulo (+ (* 19 (modulo year 19)) (floor (/ year 100)) ; gH
                                                  (* -1 (floor (/ (floor (/ year 100)) 4)))
                                                  (* -1 (floor (/ (- (floor (/ year 100)) (floor (/ (+ (floor (/ year 100)) 8) 25)) -1) 3))) ;gregG
                                                  15) 30))
                                                      (* 22 (modulo (+ 32 (* 2 (modulo (floor (/ year 100)) 4)) ;gK
                                              (* 2 (floor (/ (modulo year 100) 4)))
                                              (* -1 (modulo (+ (* 19 (modulo year 19)) (floor (/ year 100)) ; gH
                                                  (* -1 (floor (/ (floor (/ year 100)) 4)))
                                                  (* -1 (floor (/ (- (floor (/ year 100)) (floor (/ (+ (floor (/ year 100)) 8) 25)) -1) 3))) ;gregG
                                                  15) 30))
                                              (* -1 (modulo (modulo year 100) 4))) 7))) 451)))
                                   114)
                            31)
                           1)
                          )
  )

; MAIN FUNCTION
; string number -> string
; append day and month and display to user
(define (main calType year)
  (cond
    [(string=? "julian" calType) (string-append (juliMonth year) "/" (juliDay year))]
    [(string=? "gregorian" calType) (string-append (gregMonth year) "/" (gregDay year))]
    [(string=? "orthodox" calType) (string-append (orthoMonth year) "/" (orthoDay year))]

    )
  )
