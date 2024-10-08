program check_even_odd
    implicit none

    ! Declare variables
    integer, dimension(8) :: n = (/1, 2, 3, 4, 5, 6, 7, 8/)
    integer :: sum_even = 0
    integer :: sum_odd = 0
    integer :: count_even = 0
    integer :: count_odd = 0
    integer :: i

    ! Loop through the array with a step of 3
    do i = 1, 8, 1
        if (mod(n(i), 2) == 0) then
            sum_even = sum_even + n(i)
            count_even = count_even + 1
        else
            sum_odd = sum_odd + n(i)
            count_odd = count_odd + 1
        end if
    end do

    ! Print results
    print *, "The total sum of even numbers:", sum_even
    print *, "Count of even numbers:", count_even
    print *, "The total sum of odd numbers:", sum_odd
    print *, "Count of odd numbers:", count_odd

end program check_even_odd
