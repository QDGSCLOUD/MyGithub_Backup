!====================================================================
!  Random Variables or Array   
!  Auther: Xiangjun Shi(Ê·Ïæ¾ü)  
!  Email: shixj@nuist.edu.cn  
!====================================================================   
    module ran_mod
       implicit none
       private
       save
       integer , save :: Reverseflag = 0
       
       public :: Rnormal             !  return a normal distribution normal(mean,sigma)
       public :: RandomSorting       !  integer, intent(out) :: Sout(N)
       public :: SetSeed             !  SeedValue<=0,random_seed is set based on system_clock
                                     !  SeedValue>0, random_seed is set based on SeedValue
    contains

    subroutine SetSeed(SeedValue)
      implicit none
      integer, intent(in) :: SeedValue
      integer,dimension(:),allocatable :: Rseed
      integer n,clock
      !write(*,*) "<<<<random_seed>>>>"
      call random_seed(SIZE=n)
      !write(*,*) "SIZE=n",n
      allocate(Rseed(n))
      if (SeedValue.le.0) then
         call system_clock(COUNT=clock)
         !write(*,*) "clock",clock
         Rseed=clock
      else
         Rseed=SeedValue+1809648271
      endif    
      call random_seed(PUT=Rseed) 
      call random_seed(GET=Rseed)
      !write(*,*) "GET=Rseed",Rseed 
      Reverseflag = 0  !!!! Reverseflag=0 after seting seedNumber
    endsubroutine SetSeed
        
    function Rnormal(mean,sigma)
       implicit none
       real, parameter :: pi = 3.1415926
       real :: Rnormal
       real :: mean, sigma
       real :: u1, u2, y1, y2
       call random_number(u1)     !returns random number between 0 - 1 
       call random_number(u2)
       if (Reverseflag.eq.0) then
          y1 = sqrt(-2.0*log(u1))*cos(2.0*pi*u2)
          Rnormal = mean + sigma*y1
          Reverseflag = 1
       else
          y2 = sqrt(-2.0*log(u1))*sin(2.0*pi*u2)
          Rnormal = mean + sigma*y2
          Reverseflag = 0
       endif 
    end function Rnormal

    subroutine RandomSorting(N,Sout)
      implicit none
      integer, intent(in) :: N
      integer, intent(out) :: Sout(N) 
      real rantemp(N),Rrandom
      integer i,ii,itemp
      !call random_seed()
      do i=1,N
         call random_number(Rrandom)
         rantemp(i)=Rrandom
         Sout(i)=i
      enddo
      do i=1,N
         do ii=i,N
            if (rantemp(i).lt.rantemp(ii)) then
               Rrandom=rantemp(i)
               rantemp(i)=rantemp(ii)
               rantemp(ii)=Rrandom
               itemp=Sout(i)
               Sout(i)=Sout(ii)
               Sout(ii)=itemp
            endif    
         enddo    
      enddo   
    endsubroutine RandomSorting

    endmodule ran_mod
