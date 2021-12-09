

#lang racket

(require 2htdp/universe)
(require 2htdp/image)

(struct game (ball bar target pu) #:transparent) ; #:transparent = #:inspector #f

(struct box (x y w h) #:transparent)
(struct ball box (x-speed y-speed) #:transparent) ; able to hit or not?
(struct bar box (speed power) #:transparent) ; add color?
(struct target box (hits) #:transparent)
(struct pu box (speed power) #:transparent)

; world
(define WIDTH 400)
(define HEIGHT 600)

(define BAR_SPEED 20)
(define BAR_WIDTH (/ WIDTH 5))
(define BAR_HEIGHT 30)
(define INIT_BAR_X (/ WIDTH 2))
(define INIT_BAR_Y (/ HEIGHT 1.09))

(define NUM_ROWS 5)
(define NUM_BLOCKS_WIDE 15)
(define INIT_TARGET_X (* WIDTH 0.5))
(define INIT_TARGET_Y (* HEIGHT 0.25))
(define TARGET_WIDTH (/ WIDTH NUM_BLOCKS_WIDE))
(define TARGET_HEIGHT (/ HEIGHT 50))
(define NUM_HITS 2)
(define TARGET_COLORS (list "blue" "green" "yellow" "orange" "red" "gray"))
(define PU_WIDTH (* TARGET_WIDTH 0.8))
(define PU_HEIGHT (* TARGET_HEIGHT 0.9))

(define BALL_RATE 2000) ; xx
(define INIT_BALL_X (* WIDTH 0.125))
(define INIT_BALL_Y (/ HEIGHT 1.2))
(define INIT_BALL_X_SPEED 12)
(define INIT_BALL_Y_SPEED -6)
; (define INIT_BALL_DIR (/ pi 2))
(define BALL_RADIUS 3)
(define BALL_IMAGE (circle 4 "solid" "white"))
(define BACKGROUND (rectangle WIDTH HEIGHT "solid" "black"))

;;Initial game conditions
(define BALL (ball INIT_BALL_X INIT_BALL_Y 4 4 INIT_BALL_X_SPEED INIT_BALL_Y_SPEED)) ;;Initial ball conditions
(define BAR (bar INIT_BAR_X INIT_BAR_Y BAR_WIDTH BAR_HEIGHT BAR_SPEED 0))

(define TARGET_LIST (
                    map (lambda (i) (target  (- (* TARGET_WIDTH (+ (modulo i NUM_BLOCKS_WIDE) 1)) (/ TARGET_WIDTH 2))
                                                  (+ (+ (* (* TARGET_HEIGHT (ceiling (/ i NUM_BLOCKS_WIDE) )) 3) (/ TARGET_HEIGHT 2) 5)) ; height offset
                                                    TARGET_WIDTH TARGET_HEIGHT (- 1 (modulo (ceiling (/ i NUM_BLOCKS_WIDE)) 2)) ))    
                          (build-list (* NUM_ROWS NUM_BLOCKS_WIDE) (lambda (x) (+ x 1))))) 

(define POWER_UPS (
                   ; randomize power ups
                   ; get pu to drop
                   
                    map (lambda (i) (pu  (- (* TARGET_WIDTH (+ (modulo i NUM_BLOCKS_WIDE) 1)) (/ TARGET_WIDTH 2))
                                                  (+ (+ (* (* TARGET_HEIGHT (ceiling (/ i NUM_BLOCKS_WIDE) )) 3) (/ TARGET_HEIGHT 2) 5)) ; height offset
                                                    PU_WIDTH PU_HEIGHT (* INIT_BALL_Y_SPEED 2) (+ 0 (modulo (ceiling (/ i NUM_BLOCKS_WIDE)) 6)) ))    
                          (build-list (* NUM_ROWS NUM_BLOCKS_WIDE) (lambda (x) (+ x 1))))) 

;; render
(define (render t)
  (draw-ball (game-ball t)
  (draw-bar (game-bar t)
  (draw-target (game-target t) ; could generalize for boxes
  (draw-pu (game-pu t)            
  BACKGROUND)))))
 
; Render objects functions

(define (draw-ball b background)
  (cond
  [(empty? b) background]
  [(empty? (first b)) background]
  [else
   (match-define (ball x y w h xs ys) (first b))
   (place-image BALL_IMAGE x y (draw-ball (rest b) background))]))

(define (draw-bar t background)
  (match-define (bar x y w h speed power) t)
  (place-image (rectangle w (/ h 2) "solid" (list-ref TARGET_COLORS (+ power 1))) x y background))

(define (draw-target t background)
  (cond
    [(empty? t) background]
    [(empty? (first t)) background]  
    [else
     (match-define (target x y w h hits) (first t))
     (place-image (rectangle w h "solid" (list-ref TARGET_COLORS (- hits 0))) x y (draw-target (rest t) background))]))

(define (draw-pu t background)
  (cond
    [(empty? t) background]
    [(empty? (first t)) background]  
    [else
     (match-define (pu x y w h speed power) (first t))
     (place-image (rectangle w h "solid" (list-ref TARGET_COLORS (- power 0))) x y (draw-pu (rest t) background))]))

; color map

; move bar left
(define (move_bar_left t)
  (match-define (bar x y w h speed power) t)
  (bar (- x speed) y w h speed power))

; move bar right
(define (move_bar_right t)
  (match-define (bar x y w h speed power) t)
  (bar (+ x speed) y w h speed power))

(define (create-ball i)
  (cond
    [(empty? i) (cons (ball (random WIDTH) INIT_BAR_Y BALL_RADIUS BALL_RADIUS INIT_BALL_X_SPEED INIT_BALL_Y_SPEED)
                      empty)]
    [(< (random BALL_RATE) 2) (cons (ball (random WIDTH) INIT_BAR_Y BALL_RADIUS BALL_RADIUS (random 10) INIT_BALL_Y_SPEED) i)]
    [else i]))

;(define (move_pu lop ba)
;  (cond
;    [(empty? lop) lop]
;    [else
;       (match-define (bar x y w h speed power) t)
;       (bar (+ x speed) y w h speed power) ; xx
;    [(< (random BALL_RATE) 2) (cons (ball (random WIDTH) INIT_BAR_Y BALL_RADIUS BALL_RADIUS (random 10) INIT_BALL_Y_SPEED) i)]
;    [else i]]))

(define (update_lop p)
  (cond
     [(empty? p) p]
     [else
  (match-define (pu x y w h ps pp) (first p))
  (cond
    [false p]

    [else  (cons (pu x (+ y ps) w h ps pp) (update_lop (rest p) ))])]))

;move ball
(define (move_ball b)
  (cond
     [(empty? b) empty]
     [else
  (match-define (ball x y w h xs ys) (first b))
  (cond
    [(> x WIDTH) (cons (ball (- x xs) 
             (+ y ys) BALL_RADIUS BALL_RADIUS (* xs -1) ys) (move_ball (rest b) ))]
    [(< x 0)  (cons(ball (- x xs)
             (+ y ys) BALL_RADIUS BALL_RADIUS  (* xs -1) ys) (move_ball (rest b) ))]
    [(< y 0)  (cons(ball (+ x xs)
             (- y ys) BALL_RADIUS BALL_RADIUS xs (* ys -1)) (move_ball (rest b) ))]
    [(> y HEIGHT) (cons (ball (random WIDTH) INIT_BALL_Y BALL_RADIUS BALL_RADIUS (random INIT_BALL_X_SPEED) -6) (move_ball (rest b))) ]
    [else  (cons (ball (+ x xs) (+ y ys) BALL_RADIUS BALL_RADIUS xs ys) (move_ball (rest b) ))])]))


(define (colliding? b1 b2)
  (match-define (box x1 y1 w1 h1) b1)
  (match-define (box x2 y2 w2 h2) b2)
  (not (or (eq? b1 b2)
           (< (+ x1 w1) x2) (> x1 (+ x2 w2))
           (< (+ y1 h1) y2) (> y1 (+ y2 h2)))))

(define (hit_paddle lob p)
  (cond
         [(empty? lob) lob]
         [else
   (match-define (ball x y w h xs ys) (first lob))
   (match-define (bar px py pw ph pspeed power) p)
   (cond

     [(colliding? (first lob) p) (cons (ball (+ x xs)
             (- y ys) w h xs (* ys -1)) (move_ball (rest lob) ))]
       [else  (cons (first lob) (hit_paddle (rest lob) p))])]))

(define (hit_target t b)
  (cond
    [(empty? b) t] 
    [(empty? t) t]
    [else
     
  (match-define (ball x y w h xs ys) (first b))
  (match-define (target tx ty tw th hits) (first t))
  (cond
     [(colliding? (first t) (first b))
      (hit_target (rest t) b)
      ]
        [else (hit_target t (rest b))])]))

(define (hit_pu p lop)
  (cond
         [(empty? lop) p]
         [else
   (match-define (pu px py pw ph pspeed ppower) (first lop))
   (match-define (bar bx by bw bh bspeed bpower) p)
   (cond
     [(colliding? p (first lop)) (bar bx by bw bh bspeed ppower)]
       [else (cons (first lop) (hit_pu p (rest lop)))])]))

(define (destroy_targets lot lob)

  (cond[(empty? lot) empty]
   	[(empty? lob) lot]
   	[else
           (match-define (target tx ty tw th hits) (first lot))
    	(if (find_target (first lot) lob)         
            (if (= hits 0) (rest lot)
                (cons (target tx ty TARGET_WIDTH TARGET_HEIGHT
                      (- hits 1)  ) (destroy_targets (rest lot) lob)))
        	(cons (first lot) (destroy_targets (rest lot) lob))
        )]))

(define (find_target i b)
  (cond [(empty? b) false]
   	[else
         (if (colliding? i (first b))
        	true
        	(find_target i (rest b)))]))

(define (knock_ball lob lot)
  (cond[(empty? lob) empty]
   	[(empty? lot) lob]
   	[else
    	(if (find_ball (first lob) lot)
             (cons (new_dir (first lob)) (knock_ball (rest lob) lot))
        	(cons (first lob) (knock_ball (rest lob) lot)))]))

; not exactly right because can't tell which target from which direction xx
(define (new_dir b)
  (match-define (ball bx by bw bh bxs bys) b)
  (cond
    [(and (> bxs 0) (> bys 0)) (ball bx by BALL_RADIUS BALL_RADIUS  (* bxs 1) (* bys -1))]
    [(and (< bxs 0) (> bys 0)) (ball bx by BALL_RADIUS BALL_RADIUS  (* bxs 1) (* bys -1))]
      [(and (> bxs 0) (< bys 0)) (ball bx by BALL_RADIUS BALL_RADIUS  (* bxs 1) (* bys -1))]
        [(and (< bxs 0) (< bys 0)) (ball bx by BALL_RADIUS BALL_RADIUS  (* bxs 1) (* bys -1))]
   [else b]))



(define (find_ball i t)
  (cond [(empty? t) false]  
        	[else
                   (match-define (target tx ty tw th hits) (first t))
                   (match-define (ball bx by w h bxs bys) i)
                    (if
         (and      (< bx (+ tx (/ TARGET_WIDTH 2)))
                   (> bx (- tx (/ TARGET_WIDTH 2)))
                   (< by (+ ty (/ TARGET_HEIGHT 2)))
                     (> by (- ty (/ TARGET_HEIGHT 2))))
         true
        	(find_ball i (rest t)))])) 


; struct/keyevent -> struct
; checks whether or not a key has been hit and then updates the program accordingly
; (define (change i a-key))
(define (change i a-key)
  (cond
	[(key=? a-key "left") (game (game-ball i) (move_bar_left (game-bar i)) (game-target i) (game-pu i))]
	[(key=? a-key "right") (game (game-ball i) (move_bar_right (game-bar i)) (game-target i) (game-pu i))]
	[else i]))


; update game on tick tock
; struct -> struct

(define (tock x)
  
  (game (create-ball (knock_ball (move_ball (hit_paddle (game-ball x) (game-bar x))) (game-target x))) (game-bar x)
             (destroy_targets (game-target x) (game-ball x) )  (game-pu x)))


; big bang
(define (wthjs w)
  (big-bang w
    (to-draw render)
    (on-key change)
;    (on-release release_key)
    (on-tick tock)
;    (stop-when end-game? render_end_scene)))
))

(wthjs (game (create-ball (cons BALL empty)) BAR TARGET_LIST POWER_UPS))

