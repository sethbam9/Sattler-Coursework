;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname |Ch. 20 Notes|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(require 2htdp/universe)
(require 2htdp/batch-io)
(require 2htdp/abstraction)
(require htdp/dir)

; * * * * * Model 1 * * * * ;

; A Dir.v1 (short for directory) is one of: 
; – '()
; – (cons File.v1 Dir.v1)
; – (cons Dir.v1 Dir.v1)
 
; A File.v1 is a String.

; * * * * * Model 2 * * * * ;

(define-struct dir1 [name content])

; A Dir.v2 is a structure: 
;   (make-dir String LOFD)
 
; An LOFD (short for list of files and directories) is one of:
; – '()
; – (cons File.v2 LOFD)
; – (cons Dir.v2 LOFD)
 
; A File.v2 is a String.

; * * * * * Model 3 * * * * ;

; First, we define a structure for files:
(define-struct file1 [name size content])

; Second, we provide a data definition:
; A File.v3 is a structure: 
;   (make-file String N String)

(define-struct dir.v3 [name dirs files])

; Here is the refined data definition:

; A Dir.v3 is a structure: 
;   (make-dir.v3 String Dir* File*)
 
; A Dir* is one of: 
; – '()
; – (cons Dir.v3 Dir*)
 
; A File* is one of: 
; – '()
; – (cons File.v3 File*)

; * * * * * * * 20.3 Refining Functions * * * * * * * * * ;
(define O (create-dir "/Users/...")) ; on OS X 
;(define L (create-dir "/var/log/")) ; on Linux
(define W (create-dir "C:\\Users\\...")) ; on Windows 
