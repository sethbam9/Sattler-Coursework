;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname frogger) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ())))
(require 2htdp/image)
(require 2htdp/universe)

#|
----------------
---- INDEX -----
----------------
0. World Definitions
1. The Canvas
  a. Canvas size
  b. Canas divisions
2. Images
  a. Background
  b. Text
  c. Cursor
  d. Frogger
  e. Vehicle
  f. Turtle
  g. Plank
3. Title Screen
  a. Menu
  b. Location on Canvas
  c. Header
  d. Compiling the image
4. The Player
  a. Definition
  b. Location
  c. Movement
5. The Vehicles & Swimmers
  a. Definition
  b. Location
  c. Movement
5.1 The Info Box
  a. The Display Box
  b. Lives
  c. High Score
6. Drawing the Worlds
  a. Drawing the Title Screen
  b. Drawing the Game Screen
  c. Drawing the Restart Screen
  d. Drawing the Quit Screen
  e. Drawing the Score Screen
7. "Ticking" the World
  a. Ticks
8. "On-key" functions
  a. Menu Keys
  b. Restart Keys
  c. Game Keys
  d. Score Keys
9. Animation
  a. Handling the game
  b. Big-bang
10. Tests
|#

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 0. World Definitions

;; a god-world is a (make-god-world title-world game-world score-world Number)
(define-struct god-world (title-world 
                          game-world 
                          score-world
                          placeholder))
;; where title-world is a (make-title-world ...) and
;; where game-world is a (make-game-world ...) and
;; where score-world is a (make-score-world ...) and
;; the Number is a placeholder for each of the worlds

;; a title-world is a (make-title-world posn posn)
(define-struct title-world (cursor-1 cursor-2))
;; where cursor-1 is the posn of the left cursor's position and
;; cursor-2 is the posn of the right cursor's position

;; a game-world is a (make-game-world player traffic)
(define-struct game-world (player traffic swimmers score))
;; where player is a player and  
;; traffic is traffic  


;; a score-world is a (make-score-world list)
(define-struct score-world (list-of-scores))
;; where list-of-scores is the list of high scores


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 1. The Canvas
;;;; 1a. Canvas Size

;; Defines the screen size
;; size in x must be an interval of 90
;; size in y must be an interval of 130
(define CANVAS (empty-scene 990 780))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 1b. Canvas Divisions

;; Defines standard constants derived from CANVAS
(define CANVAS_WIDTH (image-width CANVAS))
(define CANVAS_HEIGHT (image-height CANVAS))
(define CENTER_CANVAS_X (/ (image-width CANVAS) 2))
(define CENTER_CANVAS_Y (/ (image-height CANVAS) 2))

;; Defines how big each lane is based on how many there are
(define DIVISION_HEIGHT (/ CANVAS_HEIGHT 13))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 2. Images
;;;; 2a. Background

;; Defines the background layers
(define GRASS
  (rectangle
   CANVAS_WIDTH (+ DIVISION_HEIGHT 1) 'solid (make-color 8 137 21)))
(define GROUND 
  (rectangle 
   CANVAS_WIDTH (+ DIVISION_HEIGHT 1) 'solid (make-color 152 117 46)))
(define ROAD 
  (rectangle
   CANVAS_WIDTH (- DIVISION_HEIGHT 1) 'solid (make-color 134 135 134)))
(define WATER
  (rectangle
   CANVAS_WIDTH (+ DIVISION_HEIGHT 1) 'solid (make-color 22 150 206)))


;; Defines the center of each lane
(define LANE_1_CENTER (- CANVAS_HEIGHT (/ DIVISION_HEIGHT 2)))
(define LANE_2_CENTER (- LANE_1_CENTER DIVISION_HEIGHT))
(define LANE_3_CENTER (- LANE_2_CENTER DIVISION_HEIGHT))
(define LANE_4_CENTER (- LANE_3_CENTER DIVISION_HEIGHT))
(define LANE_5_CENTER (- LANE_4_CENTER DIVISION_HEIGHT))
(define LANE_6_CENTER (- LANE_5_CENTER DIVISION_HEIGHT))
(define LANE_7_CENTER (- LANE_6_CENTER DIVISION_HEIGHT))
(define LANE_8_CENTER (- LANE_7_CENTER DIVISION_HEIGHT))
(define LANE_9_CENTER (- LANE_8_CENTER DIVISION_HEIGHT))
(define LANE_10_CENTER (- LANE_9_CENTER DIVISION_HEIGHT))
(define LANE_11_CENTER (- LANE_10_CENTER DIVISION_HEIGHT))
(define LANE_12_CENTER (- LANE_11_CENTER DIVISION_HEIGHT))
(define LANE_13_CENTER (- LANE_12_CENTER DIVISION_HEIGHT))

;; Defines the edges of each lane
(define CUT_LINE_1 (* 1 DIVISION_HEIGHT))
(define CUT_LINE_2 (* 2 DIVISION_HEIGHT))
(define CUT_LINE_3 (* 3 DIVISION_HEIGHT))
(define CUT_LINE_4 (* 4 DIVISION_HEIGHT))
(define CUT_LINE_5 (* 5 DIVISION_HEIGHT))
(define CUT_LINE_6 (* 6 DIVISION_HEIGHT))
(define CUT_LINE_7 (* 7 DIVISION_HEIGHT))
(define CUT_LINE_8 (* 8 DIVISION_HEIGHT))
(define CUT_LINE_9 (* 9 DIVISION_HEIGHT))
(define CUT_LINE_10 (* 10 DIVISION_HEIGHT))
(define CUT_LINE_11 (* 11 DIVISION_HEIGHT))
(define CUT_LINE_12 (* 12 DIVISION_HEIGHT))

;; Defines the background image
(define BACKGROUND
  
      ;; starting layer of grass
      (place-image 
       GRASS
       CENTER_CANVAS_X
       LANE_1_CENTER
       ;; bottom layer of road
       (place-image 
        ROAD
        CENTER_CANVAS_X
        LANE_2_CENTER
        ;; second layer of road
        (place-image 
         ROAD
         CENTER_CANVAS_X
         LANE_3_CENTER
         ;; middle layer of road
         (place-image
          ROAD
          CENTER_CANVAS_X
          LANE_4_CENTER
          ;; fourth layer of road
          (place-image 
           ROAD
           CENTER_CANVAS_X
           LANE_5_CENTER
           ;; top part of road
           (place-image
            ROAD
            CENTER_CANVAS_X
            LANE_6_CENTER
            ;; layer of dirt
            (place-image
             GROUND
             CENTER_CANVAS_X
             LANE_7_CENTER
             ;; bottom layer of water
             (place-image 
              WATER
              CENTER_CANVAS_X
              LANE_8_CENTER
              ;; second layer of water
              (place-image
               WATER 
               CENTER_CANVAS_X
               LANE_9_CENTER
               ;; middle layer of water
               (place-image 
                WATER
                CENTER_CANVAS_X
                LANE_10_CENTER
                ;; fourth layer of water
                (place-image
                 WATER
                 CENTER_CANVAS_X
                 LANE_11_CENTER
                 ;; top layer of water
                 (place-image
                  WATER
                  CENTER_CANVAS_X
                  LANE_12_CENTER
                  ;; final layer of grass
                  (place-image
                   GRASS
                   CENTER_CANVAS_X
                   LANE_13_CENTER
                   ;; the empty scene
                   CANVAS))))))))))))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 2b. Text

;; Defines the size of the text on screen
(define TEXT_SIZE (round (/ DIVISION_HEIGHT 4)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 2c. Cursor

;; Defines the image of the cursor
(define CURSOR (rotate -90 (triangle (/ TEXT_SIZE 2) 'solid 'blue)))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 2d. Frogger

;; Defines the player's body parts sizes
(define BODY_SIZE (/ DIVISION_HEIGHT 5))
(define EYE_SIZE (/ BODY_SIZE 3))
(define LEG_SIZE (* EYE_SIZE 2))
;; Defines the player's body parts images
(define FROGGER_BODY (circle BODY_SIZE 'solid (make-color 4 255 29)))
(define FROGGER_EYE (circle EYE_SIZE 'solid 'red))
(define FROGGER_LEG 
  (ellipse LEG_SIZE (* 2 LEG_SIZE) 'solid (make-color 133 13 156)))

;; Defines the constructed body of the player
(define FROGGER
  (overlay/xy
   (overlay/xy 
    (overlay/offset FROGGER_EYE
                    (- (* BODY_SIZE 2) (* 1.6 EYE_SIZE)) 0
                    FROGGER_EYE)
    0 0
    FROGGER_BODY)
  (* -1 EYE_SIZE) BODY_SIZE
  (overlay/offset (rotate 20 FROGGER_LEG)
                  (- (* 2 BODY_SIZE) (/ EYE_SIZE 2)) 0
                  (rotate -20 FROGGER_LEG))))
(define FROGGER_WIDTH (image-width FROGGER))
(define FROG_HEIGHT (image-height FROGGER))


;;Defines the broken frog to the right
(define DEAD_FROG_RIGHT_IMAGE
  (overlay/xy
   (overlay/xy 
    (overlay/offset FROGGER_BODY
                    (- (* BODY_SIZE 4) (* .6 EYE_SIZE)) LEG_SIZE
                    FROGGER_EYE)
    (* -1 LEG_SIZE) EYE_SIZE
    FROGGER_EYE)
  (* -2 EYE_SIZE) EYE_SIZE
  (overlay/offset (rotate 20 FROGGER_LEG)
                  (- (* 4 BODY_SIZE) (/ EYE_SIZE 2)) (* -1 EYE_SIZE)
                  (rotate -20 FROGGER_LEG))))
;; Defines the broken frog to the left
(define DEAD_FROG_LEFT_IMAGE
  (overlay/xy
   (overlay/offset (rotate -20 FROGGER_LEG)
                   (- (* -4 BODY_SIZE) (/ EYE_SIZE -2)) EYE_SIZE
                   (rotate 20 FROGGER_LEG))
   (* 2 EYE_SIZE) EYE_SIZE
   (overlay/xy 
    (overlay/offset FROGGER_BODY
                    (- (* BODY_SIZE -4) (* -1 .6 EYE_SIZE)) LEG_SIZE
                    FROGGER_EYE)
    LEG_SIZE EYE_SIZE
    FROGGER_EYE)))

;; Defines blood splatter to the right
(define BLOOD_SPLATTER_RIGHT
  (overlay/offset
   (overlay
   (overlay/offset
    (circle 4 'solid 'red)
    -60 10
    (circle 8 'solid 'red))
  
   (overlay/offset
    (circle 10 'solid 'red)
    75 -30
    (circle 6 'solid 'red)))
   
   15 8
   
  (overlay
   (overlay/offset
    (circle 4 'solid 'red)
    -90 30
    (circle 8 'solid 'red))
  
   (overlay/offset
    (circle 9 'solid 'red)
    40 30
    (circle 2 'solid 'red)))))
;; Defines blood splatter to the left
(define BLOOD_SPLATTER_LEFT
  (overlay/offset
   (overlay
   (overlay/offset
    (circle 4 'solid 'red)
    60 -10
    (circle 8 'solid 'red))
  
   (overlay/offset
    (circle 10 'solid 'red)
    -75 30
    (circle 6 'solid 'red)))
   
   -15 -8
   
  (overlay
   (overlay/offset
    (circle 4 'solid 'red)
    90 -30
    (circle 8 'solid 'red))
  
   (overlay/offset
    (circle 9 'solid 'red)
    -40 -30
    (circle 2 'solid 'red)))))

;; Defines the dead frog with blood to the right
(define DEAD_FROG_RIGHT
  (overlay BLOOD_SPLATTER_RIGHT
           DEAD_FROG_RIGHT_IMAGE))
;; Defines the dead frog with blood to the left
(define DEAD_FROG_LEFT
  (overlay BLOOD_SPLATTER_LEFT
           DEAD_FROG_LEFT_IMAGE))

;; Defines different orientations of the player
(define FROGGER_LEFT (rotate 90 FROGGER))
(define FROGGER_RIGHT (rotate -90 FROGGER))
(define FROGGER_DOWN (rotate 180 FROGGER))
  
;; orientation: player -> image
;; determines the direction the player is facing and produces
;; the coressponding image
(define (orientation player)
  (cond [(symbol=? 'up (player-dir player)) FROGGER]
        [(symbol=? 'down (player-dir player)) FROGGER_DOWN]
        [(symbol=? 'left (player-dir player)) FROGGER_LEFT]
        [(symbol=? 'right (player-dir player)) FROGGER_RIGHT]))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 2e. Vehicle

(define VEHICLE_WIDTH (/ DIVISION_HEIGHT 1.5))
(define WHEEL_SIZE (/ VEHICLE_WIDTH 6))

(define WHEEL (circle WHEEL_SIZE 'solid 'black))
;; Defines the vehicle's image
(define
  BODY_IMAGE 
  (rectangle VEHICLE_WIDTH (/ VEHICLE_WIDTH 2)
             'solid (make-color (random 255) (random 255) (random 255))))

(define WHEELS
  (overlay/xy WHEEL
              (- (image-width BODY_IMAGE) (image-width WHEEL))
              0
              WHEEL))

(define VEHICLE_IMAGE
  (overlay/xy WHEELS
              0
              (* (image-height WHEEL) -1)
              BODY_IMAGE))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 2f. Turtle

;; Defines the images for turtles
(define TURTLE_BODY
  (ellipse (* 2.25 FROG_HEIGHT) (* 1.75 FROG_HEIGHT) 'solid 'tan))

(define TURTLE_HEAD_SHAPE 
  (ellipse (* 1.5 FROG_HEIGHT) FROG_HEIGHT 'solid 'green))

(define TURTLE_LEG 
  (ellipse (* .8 FROG_HEIGHT) (* 1.25 FROG_HEIGHT) 'solid 'green))

(define TURTLE_EYE 
  (overlay 
   (circle (/ EYE_SIZE 2) 'solid 'black) (circle EYE_SIZE 'solid 'white)))

(define TURTLE_EYES 
  (overlay/offset
   TURTLE_EYE 0 (/ (image-height TURTLE_HEAD_SHAPE) 2) TURTLE_EYE))

(define TURTLE_HEAD 
  (overlay/xy TURTLE_EYES
              (- (/ (image-width TURTLE_HEAD_SHAPE) 2))
              (- (/ (image-height TURTLE_HEAD_SHAPE) 8))
              TURTLE_HEAD_SHAPE))

(define LEG_SET 
  (overlay/offset TURTLE_LEG (/ (image-width TURTLE_BODY) 2) 0 TURTLE_LEG))
(define ALL_LEGS 
  (overlay/offset LEG_SET 0 (/ (image-height TURTLE_BODY) 2) LEG_SET))

(define BODY_LEGS (underlay ALL_LEGS TURTLE_BODY))

(define TURTLE_FACE
  (add-curve
   TURTLE_HEAD
   (* 2.6 BODY_SIZE) (/ (image-height TURTLE_HEAD_SHAPE) 4) 0 1/3
   (* 2.6 BODY_SIZE) (* (/ (image-height TURTLE_HEAD_SHAPE) 4) 3) 0 -1/3
   "black"))

(define TURTLE_RIGHT 
  (overlay/xy BODY_LEGS
              (/ (image-width BODY_LEGS) 1.5)
              (/ (image-height BODY_LEGS) 4)
              TURTLE_FACE))

(define TURTLE_LEFT (rotate 180 TURTLE_RIGHT))

(define FROG_TURTLE_RIGHT
  (overlay/xy FROGGER 
              (- (/ (image-width TURTLE_HEAD) 2.75))
              (- (/ (image-height TURTLE_HEAD) 2))
              TURTLE_RIGHT))

(define FROG_TURTLE_LEFT
  (overlay/xy FROGGER 
              (- (/ (image-width TURTLE_HEAD) 1.125))
              (- (/ (image-height TURTLE_HEAD) 2))
              TURTLE_LEFT))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 2g. Plank

;; Defines the images of the planks
(define PLANK (rectangle (* 3 FROG_HEIGHT) (* 1.5 FROG_HEIGHT) 'solid 'tan))

(define FROG_ON_PLANK (overlay FROGGER PLANK))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 3. Title Screen
;;;; 3a. Menu

;; Defines each menu item name 
(define MENU_ITEM_1
  (text/font
   "New Game" TEXT_SIZE 'white #f 'system 'normal 'normal #f)) ;; New Game
(define MENU_ITEM_2
  (text/font
   "High Scores" TEXT_SIZE 'white #f 'system 'normal 'normal #f)) ;; High Scores
(define MENU_ITEM_3 
  (text/font
   "Quit Game" TEXT_SIZE 'white #f 'system 'normal 'normal #f)) ;; Quit Game


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 3b. Location on Canvas

;;Creates a buffer on the side of the image
;;buffer-in-x: image -> number
(define (buffer-in-x image)
  (+ 20 (image-width image)))

;; Defines location positions for the cursors
(define LOCATION_1
  (make-posn (- CENTER_CANVAS_X (/ (buffer-in-x MENU_ITEM_1) 2)) LANE_6_CENTER))
;; Menu item 1 left side ^
(define LOCATION_3
  (make-posn (- CENTER_CANVAS_X (/ (buffer-in-x MENU_ITEM_2) 2)) LANE_4_CENTER))
;; Menu item 2 left side ^
(define LOCATION_5 
  (make-posn (- CENTER_CANVAS_X (/ (buffer-in-x MENU_ITEM_3) 2)) LANE_2_CENTER))
;; Menu item 3 left side ^

(define LOCATION_6 
  (make-posn (+ CENTER_CANVAS_X (/ (buffer-in-x MENU_ITEM_1) 2)) LANE_6_CENTER))
;; Menu item 1 right side ^
(define LOCATION_8 
  (make-posn (+ CENTER_CANVAS_X (/ (buffer-in-x MENU_ITEM_2) 2)) LANE_4_CENTER))
;; Menu item 2 right side ^
(define LOCATION_10
  (make-posn (+ CENTER_CANVAS_X (/ (buffer-in-x MENU_ITEM_3) 2)) LANE_2_CENTER))
;; Menu item 3 right side ^


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 3c. Header

;; Defines the name of the game 
(define GAME_NAME
  (text/font 
   "FROGGER" (round DIVISION_HEIGHT) 'green #f 'modern 'normal 'bold #t))

;; Defines the author of the game
(define AUTHOR
  (text/font "Created by: Joshua Caron & Amanda McAllister" TEXT_SIZE
                          'white #f 'system 'normal 'bold #f))

;; Defines the title block of the game
(define TITLE 
  (overlay/offset GAME_NAME
                  0 (/ DIVISION_HEIGHT 1.5)
                  AUTHOR))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 3d. Compiling the image

;; Defines the opening scene of the game
(define TITLE_SCREEN
  (place-image 
   ;; title block of the game
   TITLE
   CENTER_CANVAS_X
   CUT_LINE_2
   ;; top menu item
   (place-image
    MENU_ITEM_1
    CENTER_CANVAS_X
    LANE_6_CENTER
    ;; middle menu item
    (place-image 
     MENU_ITEM_2 
     CENTER_CANVAS_X
     LANE_4_CENTER
     ;; bottom menu item
     (place-image 
      MENU_ITEM_3
      CENTER_CANVAS_X
      LANE_2_CENTER
      BACKGROUND)))))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 4. The Player
;;;; 4a. Definition

;; a player is a (make-player Number Number Symbol)
(define-struct player (x y dir lives))
;; where x is the x position of the player and
;; y is the y position of the player and
;; dir is the direction the player is facing and 
;; lives is the number of chances the player has to win before
;; a restart prompt

;; Number of starting lives of the player
(define START_LIVES 5)

;; The initial position of the player
(define 
  START_PLAYER (make-player (/ CANVAS_WIDTH 2) LANE_1_CENTER 'up START_LIVES))

;; The interval on which the player moves
(define MOVE_INTERVAL DIVISION_HEIGHT)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 4b. Location

;; on-screen?: player -> boolean
;; determines if the player's position is on the screen or not
(define (on-screen? player)
  (and (> (player-x player) 0)
       (< (player-x player) CANVAS_WIDTH)
       (> (player-y player) 0)
       (< (player-y player) CANVAS_HEIGHT)))

;; in-water?: player -> boolean
;; determines if the player's position is in a water lane
(define (in-water? player)
  (or (= (player-y player) LANE_8_CENTER)
      (= (player-y player) LANE_9_CENTER)
      (= (player-y player) LANE_10_CENTER)
      (= (player-y player) LANE_11_CENTER)
      (= (player-y player) LANE_12_CENTER)))

;; in-range?: number number number -> boolean
;; is n1 within range of n2?
(define (in-range? n1 n2 range)
  (and (< n1 (+ n2 range))
       (> n1 (- n2 range))))

;; hit?: player vehicle -> boolean
;; was the player hit by the vehicle?
(define (hit? player vehicle)
  (and (= (player-y player)
          (vehicle-y vehicle))
       (in-range? (player-x player)
                  (vehicle-x vehicle)
                  (+ (/ (image-width FROGGER) 2)
                     (/ (image-width VEHICLE_IMAGE) 2)))))

;; list-hit?: player list-of-traffic -> boolean
;; determines if the player hit any car in the list of traffic
(define (list-hit? player list-of-traffic)
  (local ((define all-traffic
            (append (first list-of-traffic)
                    (second list-of-traffic)
                    (third list-of-traffic)
                    (fourth list-of-traffic)
                    (fifth list-of-traffic)))
          (define (was-hit? p t)
            (cond [(empty? t) false]
                  [(hit? p (first t))
                   true]
                  [else (was-hit? p (rest t))])))
    (was-hit? player all-traffic)))


;; end-game?: game-world -> boolean
;; Determines if the game should end or not based on
;; the location of the player 
(define (end-game? god)
  (local ((define the-player (game-world-player (god-world-game-world god)))
          (define LoS (game-world-swimmers (god-world-game-world god)))
          (define on-a-swimmer?
            (cond [(on-swimmer? the-player LoS) true]
                  [else false])))
    (or (list-hit? (game-world-player (god-world-game-world god))
                   (game-world-traffic (god-world-game-world god)))
        (and (in-water? (game-world-player (god-world-game-world god)))
             (not on-a-swimmer?)))))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 4c. Movement 

;; move-frog-left: player -> player
;; changes the direction of the frog to left and
;; moves it left in x a set amount
(define (move-frog-left player)
  (make-player (- (player-x player) MOVE_INTERVAL)
               (player-y player)
               'left
               (player-lives player)))

;; move-frog-right: player -> player
;; changes the direction of the frog to the right and
;; moves it right in x a set amount
(define (move-frog-right player)
  (make-player (+ (player-x player) MOVE_INTERVAL)
               (player-y player)
               'right
               (player-lives player)))

;; move-frog-up: player -> player
;; changes the direction of the frog to facing up and
;; moves it up in y a set amount
(define (move-frog-up player)
  (make-player (player-x player)
               (- (player-y player) MOVE_INTERVAL)
               'up
               (player-lives player)))

;; move-frog-down: player -> player
;; changes the direction of the frog to facing down and 
;; moves it down in y a set amount
(define (move-frog-down player)
  (make-player (player-x player)
               (+ (player-y player) MOVE_INTERVAL)
               'down
               (player-lives player)))

;; move-frog-on-swimmer: player LoS -> player
;; when a player is on a swimmer, makes
;; a new player that will move with the swimmer
(define (move-frog-on-swimmer player LoS)
  (local ((define y-location (player-y player)))
    (cond [(or (= LANE_8_CENTER y-location)
               (= LANE_11_CENTER y-location))
           (make-player (new-player-x player LoS)
                        y-location 
                        (player-dir player)
                        (player-lives player))]
          [(or (= LANE_9_CENTER y-location)
               (= LANE_10_CENTER y-location))
           (make-player (new-player-x player LoS)
                        y-location 
                        (player-dir player) 
                        (player-lives player))]
          [(= LANE_12_CENTER y-location)
           (make-player (new-player-x player LoS) 
                        y-location
                        (player-dir player) 
                        (player-lives player))]
          [else player])))

;; new-player-x: player LoS -> Number
;; checks if a player has collided with a swimmer
;; if so, produces the x-posn of the swimmmer
(define (new-player-x player LoS)
  (local ((define LoS-single-list
            (append (first LoS)
                    (second LoS)
                    (third LoS)
                    (fourth LoS)
                    (fifth LoS)))
          (define (hit-a-swimmer? player list)
            (cond [(hit-swimmer? player (first list))
                    (cond [(symbol=? 'left (swimmer-dir (first list)))
                           (+ (* .25 FROGGER_WIDTH) (swimmer-x (first list)))]
                          ;; this part used to center FROG on TURTLE ^
                          [else (swimmer-x (first list))])]
                   [else (hit-a-swimmer? player (rest list))])))
    (hit-a-swimmer? player LoS-single-list)))


  

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 5. The Vehicles
;;;; 5a. Definition

;; a vehicle is a (make-vehicle Number Number Symbol)
(define-struct vehicle (x y dir))
;; where x is the location of the vehicle in x and
;; y is the location of the vehcile in y
;; and dir is the direction the vehicle is moving in

;; a swimmer is a (make-swimmer Number Number Symbol)
(define-struct swimmer (x y dir))
;; where x is the location of the swimmer in x and
;; y is the location of the swimmer in y
;; and dir is the direction the swimmer is moving in


;;Definitions of starting points of cars in each lane
(define LANE_1_CAR (make-vehicle 0 LANE_2_CENTER 'right))
(define LANE_2_CAR (make-vehicle CANVAS_WIDTH LANE_3_CENTER 'left))
(define LANE_3_CAR (make-vehicle 0 LANE_4_CENTER 'right))
(define LANE_4_CAR (make-vehicle CANVAS_WIDTH LANE_5_CENTER 'left))
(define LANE_5_CAR (make-vehicle 0 LANE_6_CENTER 'right))

;; a traffic is either:
;; - empty
;; - (cons vehicle traffic)

;;Defines the starting list of vehicles
(define INITIAL_VEHICLE_LIST 
  (list (list LANE_1_CAR)
        (list LANE_2_CAR)
        (list LANE_3_CAR)
        (list LANE_4_CAR)
        (list LANE_5_CAR)))

;;Defines the various velocities of the vehicles
(define FAST_VELOCITY 20)
(define MEDIUM_VELOCITY 10)
(define SLOW_VELOCITY 5)

;; move-velocity: [X] Symbol Number -> Number
;; moves a given object at the given speed and direction
;; where the symbol is either 'left or 'right
(define (move-velocity thing-x dir how-fast)
  [cond [(symbol=? dir 'left)
         (- thing-x how-fast)] 
        [(symbol=? dir 'right)
         (+ thing-x how-fast)]])



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 5b. Location

;; on-road? vehicle -> boolean
;; determines if the given vehicle is within the scene
(define (on-road? vehicle)
  (and (>= (vehicle-x vehicle) 0)
       (<= (vehicle-x vehicle) CANVAS_WIDTH)))

;; drowning?: swimmer -> boolean
;; determines if the swimmer is on the screen
(define (drowning? swimmer)
  (and (>= (swimmer-x swimmer) 0)
       (<= (swimmer-x swimmer) CANVAS_WIDTH)))

;; destroy-car: list of vehicles -> list of vehicles
;; removes vehicles from list that are outside the range of the scene
(define (kill-lane-cars LOV)
  (cond [(empty? LOV) empty]
        [(not (on-road? (first LOV)))
         (kill-lane-cars (rest LOV))]
        [else (cons (first LOV)
                    (kill-lane-cars (rest LOV)))]))

; destroy-cars: lov -> lov
;; removes offscreen vehicles from each lane
(define (destroy-car LOV)
  (list (kill-lane-cars (first LOV))
        (kill-lane-cars (second LOV))
        (kill-lane-cars (third LOV))
        (kill-lane-cars (fourth LOV))
        (kill-lane-cars (fifth LOV))))

;; kill-lane-swimmers: list of swimmers -> list of swimmers
;; removes swimmers from list that are offscreen
(define (kill-lane-swimmers LOS)
  (cond [(empty? LOS) empty]
        [(not (drowning? (first LOS)))
         (kill-lane-swimmers (rest LOS))]
        [else (cons (first LOS)
                    (kill-lane-swimmers (rest LOS)))]))

; kill-swimmers: los -> los
;; removes offscreen swimmers from each lane
(define (kill-swimmers LOS)
  (list (kill-lane-swimmers (first LOS))
        (kill-lane-swimmers (second LOS))
        (kill-lane-swimmers (third LOS))
        (kill-lane-swimmers (fourth LOS))
        (kill-lane-swimmers (fifth LOS))))


;; make-more-traffic: list of vehicles -> list of vehicles
;; determines whether or not to add more vehicles to the scene
;; and adds them if nessecary
(define (make-more-traffic LOV)
  (local ((define LANE_2_CARS (first LOV))
          (define LANE_3_CARS (second LOV))
          (define LANE_4_CARS (third LOV))
          (define LANE_5_CARS (fourth LOV))
          (define LANE_6_CARS (fifth LOV)))
    
    
    (list
     (cond [(integer? (/ (vehicle-x (first LANE_2_CARS)) 300))
            (append (first INITIAL_VEHICLE_LIST) LANE_2_CARS)]
           [else LANE_2_CARS])
     
     (cond [(integer? (/ (vehicle-x (first LANE_3_CARS)) 600))
            (append (second INITIAL_VEHICLE_LIST) LANE_3_CARS)]
           [else LANE_3_CARS])
     
     (cond [(integer? (/ (vehicle-x (first LANE_4_CARS)) 300))
            (append (third INITIAL_VEHICLE_LIST) LANE_4_CARS)]
           [else LANE_4_CARS])
     
     (cond [(integer? (/ (vehicle-x (first LANE_5_CARS)) 600))
            (append (fourth INITIAL_VEHICLE_LIST) LANE_5_CARS)]
           [else LANE_5_CARS])
     
     (cond [(integer? (/ (vehicle-x (first LANE_6_CARS)) 400))
            (append (fifth INITIAL_VEHICLE_LIST) LANE_6_CARS)]
           [else LANE_6_CARS]))))


;; make-more-swimmers: los -> los
;; determines whether or not to add more swimmers to the scene
;; and adds them if nessecary
(define (make-more-swimmers LOS)
  (local ((define LANE_8_SWIMMERS (first LOS))
          (define LANE_9_SWIMMERS (second LOS))
          (define LANE_10_SWIMMERS (third LOS))
          (define LANE_11_SWIMMERS (fourth LOS))
          (define LANE_12_SWIMMERS (fifth LOS)))
    
    
    (list
     (cond [(integer? (/ (swimmer-x (first LANE_8_SWIMMERS)) 330))
            (append (first INITIAL_SWIMMER_LIST) LANE_8_SWIMMERS)]
           [else LANE_8_SWIMMERS])
     
     (cond [(integer? (/ (swimmer-x (first LANE_9_SWIMMERS)) 350))
            (append (second INITIAL_SWIMMER_LIST) LANE_9_SWIMMERS)]
           [else LANE_9_SWIMMERS])
     
     (cond [(integer? (/ (swimmer-x (first LANE_10_SWIMMERS)) 500))
            (append (third INITIAL_SWIMMER_LIST) LANE_10_SWIMMERS)]
           [else LANE_10_SWIMMERS])
     
     (cond [(integer? (/ (swimmer-x (first LANE_11_SWIMMERS)) 300))
            (append (fourth INITIAL_SWIMMER_LIST) LANE_11_SWIMMERS)]
           [else LANE_11_SWIMMERS])
     
     (cond 
       [(= (swimmer-x (first LANE_12_SWIMMERS)) 30)
        (append (fifth INITIAL_SWIMMER_LIST) LANE_12_SWIMMERS)]
       [else LANE_12_SWIMMERS]))))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 5c. Movement

;; move-lane-vehicles: list of vehicles -> list of vehicles
;; moves all vehicles in a list based on their direction
(define (move-lane-vehicles list-of-vehicles)
  (local ((define y-location 
            (cond [(empty? list-of-vehicles) empty]
                  [else (vehicle-y (first list-of-vehicles))]))
          (define x-location
            (cond [(empty? list-of-vehicles) empty]
                  [else (vehicle-x (first list-of-vehicles))]))
          (define direction
            (cond [(empty? list-of-vehicles) empty]
                  [else (vehicle-dir (first list-of-vehicles))]))
          (define vehicle
            (cond [(empty? list-of-vehicles) empty]
                  [else (first list-of-vehicles)])))
    
    (cond [(empty? list-of-vehicles) empty]
          [(or (= LANE_2_CENTER y-location)
               (= LANE_5_CENTER y-location))
           (cons 
            (make-vehicle (move-velocity x-location direction SLOW_VELOCITY)
                          y-location 
                          (vehicle-dir vehicle))
            (move-lane-vehicles (rest list-of-vehicles)))]
          [(or (= LANE_3_CENTER y-location)
               (= LANE_4_CENTER y-location))
           (cons 
            (make-vehicle (move-velocity x-location direction MEDIUM_VELOCITY)
                          y-location 
                          (vehicle-dir vehicle))
            (move-lane-vehicles (rest list-of-vehicles)))]
          [(= LANE_6_CENTER y-location)
           (cons 
            (make-vehicle (move-velocity x-location direction FAST_VELOCITY)
                          y-location 
                          (vehicle-dir vehicle))
            (move-lane-vehicles (rest list-of-vehicles)))])))

;; vehicle-movement: lov -> lov
;; moves all the vehicles in each lane
(define (vehicle-movement LOV)
  (list (move-lane-vehicles (first LOV))
        (move-lane-vehicles (second LOV))
        (move-lane-vehicles (third LOV))
        (move-lane-vehicles (fourth LOV))
        (move-lane-vehicles (fifth LOV))))

;;Definitions of starting points of swimmers in each lane
(define LANE_8_TURTLE (make-swimmer CANVAS_WIDTH LANE_8_CENTER 'left))
(define LANE_9_PLANK (make-swimmer 0 LANE_9_CENTER 'right))
(define LANE_10_TURTLE (make-swimmer CANVAS_WIDTH LANE_10_CENTER 'left))
(define LANE_11_PLANK (make-swimmer 0 LANE_11_CENTER 'right))
(define LANE_12_TURTLE (make-swimmer CANVAS_WIDTH LANE_12_CENTER 'left))

;;Defines the starting list of swimmers
(define INITIAL_SWIMMER_LIST 
  (list (list LANE_8_TURTLE)
        (list LANE_9_PLANK)
        (list LANE_10_TURTLE)
        (list LANE_11_PLANK)
        (list LANE_12_TURTLE)))

(define SLOW_SWIMMER_VELOCITY 2)
(define MEDIUM_SWIMMER_VELOCITY 5)
(define FAST_SWIMMER_VELOCITY 6)

;; swimmer-movement: list of swimmers -> list of swimmers
;; moves all swimmers in a list based on their direction
(define (lane-swimmer-movement list-of-swimmers)
  (local ((define y-location 
            (cond [(empty? list-of-swimmers) empty]
                  [else 
                   (swimmer-y (first list-of-swimmers))]))
          (define x-location 
            (cond [(empty? list-of-swimmers) empty]
                  [else (swimmer-x (first list-of-swimmers))]))
          (define direction
            (cond [(empty? list-of-swimmers) empty]
                  [else (swimmer-dir (first list-of-swimmers))]))
          (define swimmer
            (cond [(empty? list-of-swimmers) empty]
                  [else (first list-of-swimmers)])))
    
    (cond [(empty? list-of-swimmers) empty]
          [(or (= LANE_8_CENTER y-location)
               (= LANE_11_CENTER y-location))
           (cons 
            (make-swimmer 
             (move-velocity x-location direction SLOW_SWIMMER_VELOCITY)
             y-location 
             (swimmer-dir swimmer))
            (lane-swimmer-movement (rest list-of-swimmers)))]
          [(or (= LANE_9_CENTER y-location)
               (= LANE_10_CENTER y-location))
           (cons 
            (make-swimmer 
             (move-velocity x-location direction MEDIUM_SWIMMER_VELOCITY)
             y-location 
             (swimmer-dir swimmer))
            (lane-swimmer-movement (rest list-of-swimmers)))]
          [(= LANE_12_CENTER y-location)
           (cons 
            (make-swimmer
             (move-velocity x-location direction FAST_SWIMMER_VELOCITY) 
             y-location 
             (swimmer-dir swimmer))
            (lane-swimmer-movement (rest list-of-swimmers)))])))


;; swimmer-movement: los -> los
;; moves all the swimmers in each lane
(define (swimmer-movement LOS)
  (list (lane-swimmer-movement (first LOS))
        (lane-swimmer-movement (second LOS))
        (lane-swimmer-movement (third LOS))
        (lane-swimmer-movement (fourth LOS))
        (lane-swimmer-movement (fifth LOS))))
        


;; hit-swimmer?: player vehicle -> boolean
;; was the player hit by the vehicle?
(define (hit-swimmer? player swimmer)
  (and (= (player-y player)
          (swimmer-y swimmer))
       (in-range? (player-x player)
                  (swimmer-x swimmer)
                  (+ (/ (image-width FROGGER) 2)
                     (/ (image-width PLANK) 2)))))


;; on-swimmer?: player list-of-traffic -> boolean
;; determines if the player hit any car in the list of traffic
(define (on-swimmer? player list-of-swimmers)
  (local ((define LoS-single-list
            (append (first list-of-swimmers) 
                    (second list-of-swimmers)
                    (third list-of-swimmers)
                    (fourth list-of-swimmers)
                    (fifth list-of-swimmers)))
          (define (was-hit? player list)
            (cond [(empty? list) false]
                  [(hit-swimmer? player (first list))
                   true]
                  [else (was-hit? player (rest list))])))
    (was-hit? player LoS-single-list)))
  

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 5.1. The Info Box
;;;; 5.1a. The Display Box

;; The image size for a life representation
(define LIFE_IMAGE
  (scale .5 FROGGER))

;;; Defines the starting score of the game
(define SCORE 10000)

;; score-image: number -> image
;; takes in a score and displays it as a text image
(define (score-image score)
  (text/font (string-append 
              "Score: " (number->string score))
             TEXT_SIZE 'black #f 'system 'normal 'normal #f))

;; The image size for representing the score
(define SCORE_IMAGE (score-image SCORE))

;; an info is a (make-info number number)
(define-struct info (score lives))
;; where score is the current score of the player and 
;; lives is the number of remaining lives the player has

(define INFO_BOX
  (empty-scene
   (* 5.5 (buffer-in-x LIFE_IMAGE)) (* 3 (image-height LIFE_IMAGE))))
(define START_X (- (image-width INFO_BOX) (image-width LIFE_IMAGE)))
(define START_Y (- (image-height INFO_BOX) (image-height LIFE_IMAGE)))


(define INFO_BOX_CUT_LINE (/ (image-height INFO_BOX) 2))
(define INFO_LANE_1_CENTER (/ INFO_BOX_CUT_LINE 2))
(define INFO_LANE_2_CENTER (+ INFO_LANE_1_CENTER INFO_BOX_CUT_LINE))

(define CENTER_INFO_BOX_X (/ (image-width INFO_BOX) 2))
(define CENTER_INFO_BOX_Y (/ (image-height INFO_BOX) 2))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 5.1b. Lives

;; draw-lives: number number number -> image
;; draws the correct number of life images evenly spaced
(define (draw-lives lives start-x start-y) 
  (cond [(= lives 1)
         (place-image 
          LIFE_IMAGE
          start-x
          start-y
          INFO_BOX)]
        [(<= lives 0)
         (place-image
          empty-image
          start-x
          start-y
          INFO_BOX)]
        [else 
         (place-image
          LIFE_IMAGE
          start-x
          start-y
          (draw-lives 
           (- lives 1) (+ start-x (buffer-in-x LIFE_IMAGE)) start-y))]))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 5.1c. High Score

;; subtract-score: number -> number
;; takes a score, and subtracts 1 from it as long as
;; it is greater than 0
(define (subtract-score score)
  (cond [(<= score 0) 0]
        [(<= score 1000) (- score 1)]
        [else (- score 7)]))

;; draw-text: string -> image
;; Draws the text as an image
(define (draw-text text)
 (text/font text
            TEXT_SIZE 'black #f 'system 'normal 'normal #f))

;; place-info: info -> image
;; places the info in the info box
(define (place-info info)
  (place-image (score-image (info-score info))
               (/ (buffer-in-x SCORE_IMAGE) 2)
               INFO_LANE_1_CENTER
               (draw-lives 
                (info-lives info)
                (/ (buffer-in-x LIFE_IMAGE) 2) 
                INFO_LANE_2_CENTER)))

;; draws the info box on the background
(define (draw-info info)
  (place-image (place-info info)
               (/ (buffer-in-x (place-info info)) 2)
               LANE_1_CENTER
               BACKGROUND))
  



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 6. Drawing the Worlds
;;;; 6a. Drawing the Title Screen

;; The starting instance for a title screen
(define START_TITLE 
  (make-title-world (make-posn (posn-x LOCATION_1) (posn-y LOCATION_1))
                    (make-posn (posn-x LOCATION_6) (posn-y LOCATION_6))))

;; title-draw: title-world -> image
;; draws the title scene
(define (draw-title-world title-world)
  (place-image (rotate 180 CURSOR)
               (posn-x (title-world-cursor-1 title-world))
               (posn-y (title-world-cursor-1 title-world))
               (place-image CURSOR
                            (posn-x (title-world-cursor-2 title-world))
                            (posn-y (title-world-cursor-2 title-world))
                            TITLE_SCREEN)))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 6b. Drawing the Game Screen

;; defines the starting list of vehicles on the road
(define START_VEHICLES
  (list
   (list
    (make-vehicle 30 690 'right)
    (make-vehicle 330 690 'right)
    (make-vehicle 630 690 'right)
    (make-vehicle 930 690 'right))
   (list 
    (make-vehicle 680 630 'left) 
    (make-vehicle 290 630 'left))
   (list
    (make-vehicle 70 570 'right)
    (make-vehicle 370 570 'right)
    (make-vehicle 670 570 'right)
    (make-vehicle 970 570 'right))
   (list
    (make-vehicle 835 510 'left)
    (make-vehicle 445 510 'left)
    (make-vehicle 55 510 'left))
   (list
    (make-vehicle 140 450 'right)
    (make-vehicle 440 450 'right)
    (make-vehicle 740 450 'right))))

;; defines the starting list of swimmers in the water
(define START_SWIMMERS
  (list
   (list
    (make-swimmer 826 330 'left)
    (make-swimmer 496 330 'left)
    (make-swimmer 166 330 'left))
   (list
    (make-swimmer 185 270 'right)
    (make-swimmer 535 270 'right)
    (make-swimmer 885 270 'right))
   (list 
    (make-swimmer 665 210 'left)
    (make-swimmer 175 210 'left))
   (list
    (make-swimmer 134 150 'right)
    (make-swimmer 434 150 'right)
    (make-swimmer 734 150 'right))
   (list
    (make-swimmer 588 90 'left))))

;; The starting instance for a game screen
(define START_GAME 
  (make-game-world START_PLAYER START_VEHICLES START_SWIMMERS SCORE))

;; dead?: [game world] -> boolean
;; Determines if not the player in the game is out of lives
(define (dead? game-world)
  (= 0 (player-lives (game-world-player game-world))))

;; takes in where the player died and produces 
;; either dead frog left or dead frog right depending
;; on the traffic direction for that lane
(define (dead-where? player)
  (cond [(= LANE_2_CENTER (player-y player)) DEAD_FROG_RIGHT]
        [(= LANE_3_CENTER (player-y player)) DEAD_FROG_LEFT]
        [(= LANE_4_CENTER (player-y player)) DEAD_FROG_RIGHT]
        [(= LANE_5_CENTER (player-y player)) DEAD_FROG_LEFT]
        [(= LANE_6_CENTER (player-y player)) DEAD_FROG_RIGHT]
        [(= LANE_8_CENTER (player-y player)) empty-image]
        [(= LANE_9_CENTER (player-y player)) empty-image]
        [(= LANE_10_CENTER (player-y player)) empty-image]
        [(= LANE_11_CENTER (player-y player)) empty-image]
        [(= LANE_12_CENTER (player-y player)) empty-image]
        [else FROGGER]))

;; draw-what-swimmer?: swimmer -> image
;; determines what image to draw based on the location
;; of the swimmer in y
(define (draw-what-swimmer? s)
  (local ((define y (swimmer-y s)))
    (cond [(or (= LANE_8_CENTER y)
               (= LANE_10_CENTER y)
               (= LANE_12_CENTER y))
           TURTLE_LEFT]
          [else PLANK])))

;; draw-game-world: game-world -> image
;; draws the game world
(define (draw-game-world game-world)
  (local ((define LoS (game-world-swimmers game-world)) 
          (define LoS-image-list  (append (first LoS)
                                          (second LoS)
                                          (third LoS)
                                          (fourth LoS)
                                          (fifth LoS)))
          (define LoV (game-world-traffic game-world))
          (define LoV-image-list (append (first LoV)
                                         (second LoV)
                                         (third LoV)
                                         (fourth LoV)
                                         (fifth LoV)))
          (define the-player (game-world-player game-world))
          (define on-a-swimmer? 
            (cond [(on-swimmer? the-player LoS) true]
                  [else false]))
          (define (draw-swimmers a-LoS)
            (place-image (draw-what-swimmer? (first a-LoS))
                         (swimmer-x (first a-LoS))
                         (swimmer-y (first a-LoS))
                         (cond [(empty? (rest a-LoS))
                                (draw-info
                                 (make-info (game-world-score game-world)
                                            (player-lives the-player)))]
                               [else (draw-swimmers (rest a-LoS))])))
          (define (draw-player p)
            (cond [on-a-swimmer?
                   (place-image (cond [(= 0 (player-lives p)) empty-image]
                                      [else (orientation p)])
                                (new-player-x p LoS)
                                (player-y p)
                                (draw-swimmers LoS-image-list))]
                  [else (place-image (cond [(dead? game-world) (dead-where? p)]
                                           [else (orientation p)])
                                     (player-x p)
                                     (player-y p)
                                     (draw-swimmers LoS-image-list))]))
          (define (draw-vehicles LoV)
            (place-image VEHICLE_IMAGE
                         (vehicle-x (first LoV))
                         (vehicle-y (first LoV))
                         (cond [(empty? (rest LoV)) (draw-player the-player)]
                               [else (draw-vehicles (rest LoV))]))))       
    (draw-vehicles LoV-image-list)))  




;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 6c. Drawing the Restart Screen

;; Defines text within the restart box
(define RESTART_TEXT 
  (text/font 
   "RESTART? Y/N" TEXT_SIZE 'white #f 'system 'normal 'bold #f))
(define WINNING_TEXT 
  (text/font 
   "YOU WON! PLAY AGAIN? Y/N" TEXT_SIZE 'white #f 'system 'normal 'bold #f))

;; Defines the restart box shape
(define RESTART_BOX (rectangle (* 1.25 (image-width RESTART_TEXT))
                              (* 1.25 (image-height RESTART_TEXT))
                              'solid
                              'black))

(define WINNING_BOX (rectangle (* 1.25 (image-width WINNING_TEXT))
                               (* 1.25 (image-height WINNING_TEXT))
                               'solid
                               'black))

;; Defines the restart box image with text
(define RESTART_IMAGE
  (overlay RESTART_TEXT RESTART_BOX))

(define WINNING_IMAGE
  (overlay WINNING_TEXT WINNING_BOX))

;; draw-restart: game-world -> game-world
;; places the restart box image on the current game world
(define (draw-restart game-world)
  (place-image RESTART_IMAGE
               CENTER_CANVAS_X
               CENTER_CANVAS_Y
               (draw-game-world game-world)))


(define (draw-win-world game-world)
  (place-image WINNING_IMAGE
               CENTER_CANVAS_X
               CENTER_CANVAS_Y
               (draw-game-world game-world)))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 6d. Drawing the Quit Screen

;; Defines the quitting text
(define QUIT_TEXT (text/font "Thanks for playing!" 
                             (round (/ DIVISION_HEIGHT 2)) 
                             'black 
                             #f 
                             'system 
                             'normal 'bold #f))

;; Defines a blank scene with text
(define QUIT_SCREEN
  (place-image QUIT_TEXT
               CENTER_CANVAS_X
               CENTER_CANVAS_Y
               CANVAS))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 6e. Drawing the Score Screen

;; Defines the starting scores
(define START_SCORE (make-score-world empty))

;; draw-score-world: world -> image
;; draws the score world
(define (draw-score-world world)
  (draw-scores (top-3 world) LANE_6_CENTER))

;; top-3: [score world] -> list
;; produces a list of the top 3 scores in the score world
(define (top-3 world)
  (list-scores (order (score-world-list-of-scores world)) 3))

;; list-scores: list Number -> list
;; produces a list of the top X scores
(define (list-scores los num)
  (cond [(empty? los) empty]
        [(= 0 num) empty]
        [else (cons (first los)
                    (list-scores (rest los) (- num 1)))]))

;; biggest?: Number [Listof Numbers] -> boolean
;; determines if the number is the biggest in the list
(define (biggest? num lon)
  (cond [(empty? lon) true]
        [(> (first lon) num) false]
        [else (biggest? num (rest lon))]))

;; cycle-list: [Listof Numbers] -> [Listof Numbers]
;; places the top item of the list at the bottom
(define (cycle-list lon)
  (append (rest lon)
          (list (first lon))))

;; order: [Listof Numbers] -> [Listof Numbers]
;; arranges a list of numbers from largest to smallest
(define (order lon)
  (cond [(empty? lon) empty]
        [(biggest? (first lon) lon)
         (cons (first lon) (order (rest lon)))]
        [else (order (cycle-list lon))]))

;; score-text: Number -> image
;; produces the game score as an image
(define (score-text score)
  (text/font (number->string score)  
             TEXT_SIZE 'white #f 'system 'normal 'normal #f))

;; draw-scores: world number -> image
;; takes a world in a starting position in y and
;; draws the world on the background
(define (draw-scores los start-y)
  (cond [(empty? los)
         (place-image (text/font "Press ENTER to return to the main menu."
                                 TEXT_SIZE 'white #f 'system 'normal 'normal #f)
                      CENTER_CANVAS_X
                      LANE_2_CENTER
                      (place-image TITLE
                                   CENTER_CANVAS_X
                                   CUT_LINE_2
                                   BACKGROUND))]
        [else (place-image (score-text (first los))
                           CENTER_CANVAS_X
                           start-y
                           (draw-scores (rest los)
                                        (+ start-y DIVISION_HEIGHT)))]))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 7. "Ticking" the World
;;;; 7a. Ticks

;; game-action: game-world -> game-world
;; defines what happens when the game-world "ticks"
(define (game-action game-world)
  (local ((define the-player (game-world-player game-world))
          (define LoS (game-world-swimmers game-world))
          (define on-a-swimmer?
            (cond [(on-swimmer? the-player LoS) true]
                  [else false])))
    (make-game-world 
     (cond [on-a-swimmer?
            (move-frog-on-swimmer 
             (game-world-player game-world) (game-world-swimmers game-world))]
           [else (game-world-player game-world)])
     (destroy-car 
      (vehicle-movement (make-more-traffic (game-world-traffic game-world))))
     (kill-swimmers
      (swimmer-movement (make-more-swimmers (game-world-swimmers game-world))))
   (subtract-score (game-world-score game-world)))))




;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 8. "On-key" functions
;;;; 8a. Menu Keys

;; posn=?: posn posn -> boolean
;; determines if the two posns are the same
(define (posn=? posn1 posn2)
  (and (= (posn-x posn1) (posn-x posn2))
       (= (posn-y posn1) (posn-y posn2))))

;; move-cursor-up: cursor -> cursor
;; moves the cursor up a spot from its current position
(define (move-cursor-up cursor)
  (cond ;; For left cursor
        [(posn=? cursor LOCATION_1) LOCATION_5]
        [(posn=? cursor LOCATION_3) LOCATION_1]
        [(posn=? cursor LOCATION_5) LOCATION_3]
        ;; For right cursor
        [(posn=? cursor LOCATION_6) LOCATION_10]
        [(posn=? cursor LOCATION_8) LOCATION_6]
        [(posn=? cursor LOCATION_10) LOCATION_8]))


;; move-cursor-down cursor -> cursor
;; moves the cursor down a spot from its current position
(define (move-cursor-down cursor)
  (cond ;; For left cursor
        [(posn=? cursor LOCATION_1) LOCATION_3]
        [(posn=? cursor LOCATION_3) LOCATION_5]
        [(posn=? cursor LOCATION_5) LOCATION_1]
        ;; For right cursor
        [(posn=? cursor LOCATION_6) LOCATION_8]
        [(posn=? cursor LOCATION_8) LOCATION_10]
        [(posn=? cursor LOCATION_10) LOCATION_6]))


;; check-cursor-position: world -> world
;; checks the cursor's position and produces
;; the world associated with that position
(define (check-cursor-position god)
  (cond [(posn=? (title-world-cursor-1 (god-world-title-world god)) LOCATION_1)
         (make-god-world (god-world-title-world god)
                         (god-world-game-world god)
                         (god-world-score-world god)
                         1)];; New Game
        [(posn=? (title-world-cursor-1 (god-world-title-world god)) LOCATION_3)
         (make-god-world (god-world-title-world god)
                         (god-world-game-world god)
                         (god-world-score-world god)
                         3)] ;; High Scores
        [(posn=? (title-world-cursor-1 (god-world-title-world god)) LOCATION_5)
         (make-god-world (god-world-title-world god)
                         (god-world-game-world god)
                         (god-world-score-world god)
                         5)] ;; Quit Game
        [else god]))



;; title-keys: title-world key -> title-world
;; produces a title-world given a key
(define (title-keys god key)
  (cond [(key=? "up" key) 
         (make-god-world
          (make-title-world
           (move-cursor-up (title-world-cursor-1 (god-world-title-world god)))
           (move-cursor-up (title-world-cursor-2 (god-world-title-world god))))
          (god-world-game-world god)
          (god-world-score-world god)
          (god-world-placeholder god))]
        [(key=? "down" key) 
         (make-god-world
          (make-title-world 
           (move-cursor-down (title-world-cursor-1 (god-world-title-world god)))
          (move-cursor-down (title-world-cursor-2 (god-world-title-world god))))
          (god-world-game-world god)
          (god-world-score-world god)
          (god-world-placeholder god))]
        [(key=? "\r" key) (check-cursor-position god)]
        [else god]))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 8b. Restart Keys

;; restart-keys: game-world key -> world
;; determines where to go next from restart box
(define (restart-keys god key)
  (cond [(key=? "y" key) (make-god-world START_TITLE
                                         START_GAME
                                         (god-world-score-world god)
                                         1)]
        [(key=? "n" key) (make-god-world START_TITLE
                                          START_GAME
                                          (god-world-score-world god)
                                          0)]
        [else god]))



(define (win-keys god key)
  (cond [(key=? "y" key)
         (make-god-world
          START_TITLE
          START_GAME
          (make-score-world 
           (append (list (game-world-score (god-world-game-world god)))
                   (score-world-list-of-scores (god-world-score-world god))))
          1)]
        [(key=? "n" key) 
         (make-god-world 
          START_TITLE
          START_GAME
          (make-score-world 
           (append (list (game-world-score (god-world-game-world god)))
                   (score-world-list-of-scores (god-world-score-world god))))
          0)]
        [else god]))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 8c. Game Keys

;; move-frog: game-world key -> game-world
;; determines where to move the frog based on
;; the key that is pressed
(define (move-frog game-world key)
  (cond [(key=? "left" key)
         (cond [(on-screen? (move-frog-left (game-world-player game-world)))
                (make-game-world 
                 (move-frog-left (game-world-player game-world))
                 (game-world-traffic game-world)
                 (game-world-swimmers game-world)
                 (game-world-score game-world))]
               [else game-world])]
        [(key=? "right" key)
         (cond [(on-screen? (move-frog-right (game-world-player game-world)))
                (make-game-world
                 (move-frog-right (game-world-player game-world))
                 (game-world-traffic game-world)
                 (game-world-swimmers game-world)
                 (game-world-score game-world))]
               [else game-world])]
        [(key=? "up" key)
         (cond [(on-screen? (move-frog-up (game-world-player game-world)))
                (make-game-world 
                 (move-frog-up (game-world-player game-world))
                 (game-world-traffic game-world)
                 (game-world-swimmers game-world)
                 (game-world-score game-world))]
               [else game-world])]
        [(key=? "down" key)
         (cond [(on-screen? (move-frog-down (game-world-player game-world)))
                (make-game-world 
                 (move-frog-down (game-world-player game-world))
                 (game-world-traffic game-world)
                 (game-world-swimmers game-world)
                 (game-world-score game-world))]
               [else game-world])]       
        [else game-world]))



;; game-keys: god-world key -> god-world
;; determines what key strokes are available determined by
;; whether or not the game has ended
(define (game-keys god key)
  (cond [(win? god) (win-keys god key)]
        [(or (end-game? god) (no-lives? god)) (restart-keys god key)]
        [(key=? "escape" key)
         (make-god-world (god-world-title-world god)
                         START_GAME
                         (god-world-score-world god)
                         0)]
        [else 
         (make-god-world (god-world-title-world god)
                         (move-frog (god-world-game-world god) key)
                         (god-world-score-world god)
                         (god-world-placeholder god))]))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 8d. Score Keys

;; score-keys: score-world key -> world
;; defines what happens when keys are pressed on
;; a score world
(define (score-keys w k)
  (cond [(key=? "\r" k)
         (make-god-world 
          (make-title-world (make-posn (posn-x LOCATION_3) (posn-y LOCATION_3))
                            (make-posn (posn-x LOCATION_8) (posn-y LOCATION_8)))
          (god-world-game-world w)
          (make-score-world (top-3 (god-world-score-world w)))
          0)]
        [else w]))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 9. Animation
;;;; 9a. Handling the game

;; win?: god-world -> boolean
;; Determines if the player has won the game or not
(define (win? god)
  (= LANE_13_CENTER
     (player-y (game-world-player (god-world-game-world god)))))

;; draw-what?: god-world -> image
;; determines what to draw given the type of world
(define (draw-what? god )
  (cond [(= (god-world-placeholder god) 0) 
         (draw-title-world (god-world-title-world god))]
        [(= (god-world-placeholder god) 1) 
         (draw-what-game? god)]
        [(= (god-world-placeholder god) 3) 
         (draw-score-world (god-world-score-world god))]
        [(= (god-world-placeholder god) 5) QUIT_SCREEN]
        [else god]))
 
;; draw-what-game? game-world -> image
;; determines what type of game world to draw
(define (draw-what-game? god)
  (cond [(win? god)
         (draw-win-world (god-world-game-world god))]
        [(no-lives? god) (draw-restart (god-world-game-world god))]
        [(end-game? god)
         (cond [(= 1 (player-lives (game-world-player 
                                    (god-world-game-world god))))
                (draw-restart (god-world-game-world god))]
               ;; When player dies with 1 life, RESTART? is displayed ^
               [else (draw-game-world
                      (make-game-world 
                       (make-player (player-x START_PLAYER)
                                    (player-y START_PLAYER)
                                    (player-dir START_PLAYER)
                                    (player-lives (game-world-player
                                                   (god-world-game-world god))))
                       (game-world-traffic (god-world-game-world god))
                       (game-world-swimmers (god-world-game-world god))
                       (game-world-score (god-world-game-world god))))])]
        ;; Restarts the player's position when they die with more than 1 life ^
        [else (draw-game-world (god-world-game-world god))]))
        ;; Draws the normal game world when player isn't dead ^

;; key-handler: god-world key -> world
;; defines what happens when certain keys are pressed
(define (key-handler w k)
  (cond [(= (god-world-placeholder w) 0) (title-keys w k)]
        [(= (god-world-placeholder w) 1) (game-keys w k)]
        [(= (god-world-placeholder w) 3) (score-keys w k)]
        [else w]))

;; tick-what?: god-world -> god-world
;; determines what happens on each tick according to 
;; the type of world given
(define (tick-what? god)
  (cond [(= (god-world-placeholder god) 1) (make-new-game god)]
        [else god]))

;; make-new-game: god-world -> god-world
;; makes a new god with the game world changed  
(define (make-new-game god)
  (make-god-world (god-world-title-world god)
                  (tick-what-game? god)
                  (god-world-score-world god)
                  (god-world-placeholder god)))

;; no-lives?: god-world -> boolean
;; determines if the player has run out of lives
(define (no-lives? god)
  (= 0 (player-lives (game-world-player (god-world-game-world god)))))

;; tick-what-game?: game-world -> game-world
;; ticks the game world 
(define (tick-what-game? god)
  (cond [(win? god)
         (make-game-world 
          (game-world-player (god-world-game-world god))
          (destroy-car 
           (vehicle-movement 
            (make-more-traffic
             (game-world-traffic (god-world-game-world god)))))
          (kill-swimmers
           (swimmer-movement 
            (make-more-swimmers 
             (game-world-swimmers (god-world-game-world god)))))
          (game-world-score (god-world-game-world god)))]
        
        [(no-lives? god)
         (make-game-world 
          (make-player 
           (player-x (game-world-player (god-world-game-world god)))
           (player-y (game-world-player (god-world-game-world god)))
           (player-dir (game-world-player (god-world-game-world god)))
           0)
          (destroy-car 
           (vehicle-movement 
            (make-more-traffic 
             (game-world-traffic (god-world-game-world god)))))
          (kill-swimmers
           (swimmer-movement 
            (make-more-swimmers
             (game-world-swimmers (god-world-game-world god)))))
          (game-world-score (god-world-game-world god)))]   
        
        [(end-game? god) 
         (cond [(= 1 (player-lives (game-world-player 
                                    (god-world-game-world god))))
                (make-game-world 
                 (make-player 
                  (player-x (game-world-player (god-world-game-world god)))
                  (player-y (game-world-player (god-world-game-world god)))
                  (player-dir (game-world-player (god-world-game-world god)))
                  0)
                 (destroy-car 
                  (vehicle-movement 
                   (make-more-traffic (game-world-traffic
                                       (god-world-game-world god)))))
                 (kill-swimmers
                  (swimmer-movement 
                   (make-more-swimmers (game-world-swimmers 
                                        (god-world-game-world god)))))
                 (game-world-score (god-world-game-world god)))]
               [else (game-action
                      (make-game-world
                       (make-player (player-x START_PLAYER)
                                    (player-y START_PLAYER)
                                    (player-dir START_PLAYER)
                                    (- (player-lives 
                                        (game-world-player 
                                         (god-world-game-world god))) 1))
                       (game-world-traffic (god-world-game-world god))
                       (game-world-swimmers (god-world-game-world god))
                       (game-world-score (god-world-game-world god))))])]
        
        [else (game-action (god-world-game-world god))])) 



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; 9b. Big-bang


;; Defines the starting instance of the game
(define START_GOD (make-god-world START_TITLE START_GAME START_SCORE 0))

;; LET THERE BE LIGHT
(big-bang START_GOD
          (on-draw draw-what?)
          (on-key key-handler)
          (on-tick tick-what?))