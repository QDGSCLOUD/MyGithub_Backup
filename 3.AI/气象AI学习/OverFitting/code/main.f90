!****************************************************************************
!
!  PROGRAM: - Producing some samples artificially, and then  
!             investigate the overfitting problem.   
!
!  Author : Xiangjun.Shi   06-01-2022
!
!****************************************************************************	 

   program main   ! main program
      use pra_data_mod,only: Nt,Nx,Np
      use preliminary,only:LoadData,DataAnalyze
      use OverFitting,only:OFtestOffline
      implicit none

      call LoadData
      !call DataAnalyze
      
      call OFtestOffline

      
   endprogram main



    
