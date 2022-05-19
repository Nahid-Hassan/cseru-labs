.model small
.stack 100h

.data
    newline db 10,13,'$'                    ; for newline
    input_prompt db 'Enter the string: $'    ; PROMPT for take input
    MX db 'MAX: $'    ; PROMPT for display result 
    MN db 'MIN: $'    
    
.code

MAIN proc
    ; initialize data segment
    mov ax, @data
    mov ds, ax
    
    ; INPUT PROMT                                                       
    lea dx, input_prompt
    mov ah, 09
    int 21h
 
    mov bl, 'z'
    mov bh, '0'
        
    READ_STRING:   
        ; read characters one by one
        mov ah, 01
        int 21h
        
        ; if user press enter key -> stop reading and jump equal in REVERSE_STRING label
        cmp al, 13              ; 13 is the ascii value for enter key
        je DISPLAY_RESULT
        
        cmp al, bh        
        jg MAX
        
        cmp al, bl
        jl MIN
        
        MAX:
           mov bh, al
           jmp END
        MIN:
            mov bl, al
        
        END:
    loop READ_STRING
    
    DISPLAY_RESULT:
        ; newline
        lea dx, newline
        mov ah, 09
        int 21h
        
        ; prompt for max 
        lea dx, MX
        mov ah, 09
        int 21h
        
        mov dl, bh ; MAX
        mov ah, 02
        int 21h
        
        ; newline
        lea dx, newline
        mov ah, 09
        int 21h
        
        ; prompt for min
        lea dx, MN
        mov ah, 09
        int 21h
        
        mov dl, bl ; MIN
        mov ah, 02
        int 21h
    EXIT:
        mov ah, 4ch
        int 21h
            
MAIN endp ; end procedure main
end main