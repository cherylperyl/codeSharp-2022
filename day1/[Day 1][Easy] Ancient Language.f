! Enter your code here. Read input from STDIN. Print output to STDOUT
Program prog
CHARACTER str*128
CHARACTER :: t
INTEGER :: i, length
READ(*, '(A)') str
!enter your code here
n = LEN_TRIM(str)
DO i = 1, n/2
 t = str(i:i)
 str(i:i) = str(n+1-i:n+1-i)
 str(n+1-i:n+1-i) = t
END DO
PRINT*, str
End Program prog