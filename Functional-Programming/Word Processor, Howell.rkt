;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname |Word Processor, Howell|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(require 2htdp/universe)
(require 2htdp/batch-io)

; Global Variables for text box
(define WIDTH 200)
(define HEIGHT 20)
(define CURS-WIDTH 1)
(define CURS-HEIGHT (- HEIGHT 2))
(define FONT-SIZE (- CURS-HEIGHT 2))
(define FONT-COLOR "black")
(define FONT-FAMILY "roman")
(define FONT-STYLE "normal")
(define FONT-WEIGHT "normal")

; Images
(define TEXTBOX (rectangle WIDTH HEIGHT "outline" "black"))
(define CURSOR (rectangle CURS-WIDTH CURS-HEIGHT "solid" "red"))

; Editor Struct
(define-struct editor [pre post])

; Render
; Editor -> Img
(define (textRender ed)
  (cond
   [(> (image-width TEXTBOX) (image-width (textPos ed)))
    (place-image/align (textPos ed) (/ FONT-SIZE 2) (/ HEIGHT 2) "left" "center" TEXTBOX)]
   [else
    (place-image/align (textPos ed) (* -1 WIDTH) (/ HEIGHT 2) "left" "center"
                 TEXTBOX)]))
  
; Render Aux
; Editor -> Img
(define (textPos ed)
  (beside (allText (reverse (editor-pre ed)))
          CURSOR
          (allText (editor-post ed))))

; All Text
; List -> Img
(define (allText L)
  (text/font (implode L)
        FONT-SIZE FONT-COLOR
        #f FONT-FAMILY FONT-STYLE FONT-WEIGHT #f))
  
; Key Event
; Editor/Key-event -> Editor
(define (keyHandler ed k)
  (cond
    [(key=? k "left") (cursLeft ed)]
    [(key=? k "right") (cursRight ed)]
    [(key=? k "\b") (backspace ed)]
    [(key=? k "\r") (saveFile ed)]
    [(key=? k "\t") ed]
    [ (= (string-length k) 1); (> (image-width TEXTBOX) (image-width (textPos ed))))
          (newChar ed k)]
    [else ed]))
    
; Cursor Left
; Editor -> Editor
(define (cursLeft ed)
  (cond ; https://github.com/eareese/htdp-exercises/blob/master/part02-arbitrarily-large-data/179-editor-functions.rkt
    [(<= 1 (length (editor-pre ed)))
     (make-editor (rest (editor-pre ed))
                  (cons (first (editor-pre ed)) (editor-post ed)))]
    [else ed]))

; Cursor Right
; Editor -> Editor
(define (cursRight ed)
   (cond ; https://github.com/eareese/htdp-exercises/blob/master/part02-arbitrarily-large-data/179-editor-functions.rkt
    [(<= 1 (length (editor-post ed)))
     (make-editor (cons (first (editor-post ed)) (editor-pre ed))
                  (rest (editor-post ed)))]
    [else ed]))

; Backspace
; Editor -> Editor
(define (backspace ed)
  (cond ; https://github.com/eareese/htdp-exercises/blob/master/part02-arbitrarily-large-data/179-editor-functions.rkt
    [(<= 1 (length (editor-pre ed)))
     (make-editor (rest (editor-pre ed))
                  (editor-post ed))]
    [else ed]))

; Save File
; Editor -> Editor
(define (saveFile ed)
    (write-file (string-append (substring (implode (reverse (editor-pre ed))) 0 9) ".txt") ;name the file after first 9 chars of editor-pre. 
              (implode (append (reverse (editor-pre ed))
           (editor-post ed)))))

; Add New Character
; Editor/Key-event -> Editor
(define (newChar ed k)
   (make-editor (cons k (editor-pre ed)) (editor-post ed)))

; Main Function
(define (run L)
  (big-bang (make-editor empty empty )
    [on-key keyHandler]
    [to-draw textRender]))

(run empty)

  