! This is a simple Fortran program to demonstrate basic syntax and operations.

program hello
    ! The implicit none statement is used to ensure that all variables must be explicitly declared.
    implicit none

    ! Declare variables. In this case, we are using integer type variables.
    integer :: a, b, sum

    ! Initialize variables with values.
    a = 5
    b = 10

    ! Calculate the sum of the two variables.
    sum = a + b

    ! Print the result to the console. The * after print specifies default formatting.
    print *, "The sum of", a, "and", b, "is", sum

end program hello
