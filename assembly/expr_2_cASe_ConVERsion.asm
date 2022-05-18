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
    
    
    ; INPUT PROMT
    lea dx, input_prompt
    mov ah, 09
    int 21h
        
    READ_STRING:   
        ; read characters one by one
        mov ah, 01
        int 21h
        
        ; if user press enter key -> stop reading and jump equal in REVERSE_STRING label
        cmp al, 13              ; 13 is the ascii value for enter key
        je DISPLAY_STRING
        
        ; -----------------------------------------------
        ; before store change the lowercase to uppercase 
        ; IF NOT alphabet no need to change
        ;------------------------------------------------
        cmp al, 'z'
        jg NOCHANGE       ; if char greater than 'z' NOCHANGE
        cmp al, 'A'
        jl NOCHANGE       ; if char less than 'A' NOCHANGE
        cmp al, 'Z'
        jg TOP            ; if char greater than 'Z' MOVE to TOP label
        
        jmp CC            ; cc -> CaSE ConvERsion
        TOP:
            cmp al, 'a'
            jl NOCHANGE   ; Now if char less than 'a' NOCHANGE
        CC: 
            ; xor with 32 convert lower to upper and upper to lower
            xor al, 32    ; Everything else change the char 
        
        NOCHANGE:
            mov [si], al                     ; same as msg[si], al
            inc si    
    loop READ_STRING
    
    DISPLAY_STRING:
        ; newline
        lea dx, newline
        mov ah, 09
        int 21h
        ;OUTPUT PROMT
        lea dx, output_prompt
        mov ah, 09
        int 21h
        
        lea dx, msg
        mov ah, 09
        int 21h
        
    EXIT:
        mov ah, 4ch
        int 21h
            
MAIN endp ; end procedure main
end main