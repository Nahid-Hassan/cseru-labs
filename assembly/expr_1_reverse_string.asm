; string reverse in assemlby programming intel 8086 processor

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
        je REVERSE_STRING
        
        mov [si], al                     ; same as msg[si], al
        inc si    
    loop READ_STRING
    
    REVERSE_STRING:
        ; newline
        lea dx, newline
        mov ah, 09
        int 21h
        ;OUTPUT PROMT
        lea dx, output_prompt
        mov ah, 09
        int 21h
        
        ; display string in reverse order
        dec si ; decrese the si
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
