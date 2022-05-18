# CSE-3232 (Microprocessor and Assembly Language Lab)

**Table of Contents**:

- [CSE-3232 (Microprocessor and Assembly Language Lab)](#cse-3232-microprocessor-and-assembly-language-lab)
  - [Some Basic Terminology for String Operation in Assembly Language](#some-basic-terminology-for-string-operation-in-assembly-language)
    - [Take String Input and Display Output](#take-string-input-and-display-output)
    - ["Line Feed" Vs "Carriage Return"](#line-feed-vs-carriage-return)
    - [`lea` and `offset`](#lea-and-offset)
  - [Experiment-1 (String Reverse)](#experiment-1-string-reverse)

## Some Basic Terminology for String Operation in Assembly Language

**Note**: File `./Basics.pdf` contains some basic information with proper examples. 

- Hello world
- Service Routine
- Input and Output
- Loop (Simple and Nested)
- Jump (Both Conditional and Unconditional)

### Take String Input and Display Output

```assembly
; read string 
.model small
.stack 100h

.data                        
; msg is a array variable with length 50, we places '$' in dup() because in assembly
; string ends with character '$'

msg db 50 dup('$')            
newline db 10, 13, '$'   ; 10 -> line feed and 13 carriage return

.code 
main proc
    ; initialize data segment
    mov ax, @data
    mov ds, ax
        
    ; below both statement are same
    ;mov si, offset msg
    ; To access array we need to define the si register with start offset address of the variable   
    lea si, msg                  ; mov starting offset address into the si register
    
    
    ; read string and store into the variable msg
    loop_1:
        mov ah, 01                ; read single character and by default it store on the al register
        int 21h
        
        ; if user press enter key the program jumpped into the display_and_exit where we display 
        ; what we store on the msg variable
        cmp al, 13 ; 13 enter key  
        je display_and_exit   
        
        
        mov [si], al
        ; increment offset
        inc si
    loop loop_1
        
    
    display_and_exit:
        ; we need to print newline because if we don't print newline
        ; the result is shown above the input ... you getting confused.
        mov dx, offset newline
        ; lea dx, newline 
        mov ah, 09         ; print string until find '$' sign
        int 21h                                                  
        
        ; lea dx,  msg
        mov dx, offset msg
        mov ah, 09
        int 21h
        
        mov ah, 4ch
        int 21h
        
main endp
end main
```

### "Line Feed" Vs "Carriage Return"

![images](./images/cflf.png)

### `lea` and `offset` 

![images](images/lea-and-offset.png)

> If you are already familiar with take string input and display it on the monitor then you are ready for perform various string operation.

## Experiment-1 (String Reverse)

> Simple enough: VISUALIZATION

```
READ abcdef

si[0]   si[1]   si[2]   si[3]   si[4]   si[5]   si[6]
   a       b       c       d       e       f     final si offset value
```

1. So first we need to decrease `si` by `1`
2. Then `mov` one by one value into the `dl` register and decrease the `si` register.
3. If `si` is `zero` then `exit` the program.

```assembly
.model small
.stack 100h

.data
    msg db 100 dup('$')                     ; to store string 
    newline db 10,13,'$'                    ; for newline
    input_prompt db 'Enter the string: $'    ; PROMPT for take input
    output_prompt db 'After modifying: $'    ; PROMPT for display result

.code

MAIN proc
    ; initialize data segment
    mov ax, @data
    mov ds, ax
    
    ; initialize the input_array
    mov si, offset msg
    ;lea si, msg
    
    
    ; INPUT PROMPT
    lea dx, input_prompt
    mov ah, 09
    int 21h
        
    READ_STRING:   
        ; read characters one by one
        mov ah, 01
        int 21h
        
        ; if user press enter key -> stop reading and jump equal in REVERSE_STRING label
        cmp al, 13              ; 13 is the ascii value for enter key
        je REVERSE_STRING
        
        mov [si], al                     ; same as msg[si], al
        inc si    
    loop READ_STRING
    
    REVERSE_STRING:
        ; newline
        lea dx, newline
        mov ah, 09
        int 21h
        ;OUTPUT PROMPT
        lea dx, output_prompt
        mov ah, 09
        int 21h
        
        ; display string in reverse order
        dec si ; decrease the si register
        LOOP_REVERSE:
            mov dl, [si]  ; read the value of msg[si]   

            mov ah, 02
            int 21h
            
            cmp si, 0     ; compare with 0, if si == 0 then it is now in starting address and exit
            je EXIT
        
            dec si
        loop LOOP_REVERSE
     
    EXIT:
        mov ah, 4ch
        int 21h
            
MAIN endp ; end procedure main
end main
```