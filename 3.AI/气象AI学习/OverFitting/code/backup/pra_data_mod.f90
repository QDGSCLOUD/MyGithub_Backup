!====================================================================    
!  Auther: Xiangjun Shi(Ê·Ïæ¾ü)  
!  Email: shixj@nuist.edu.cn  
!====================================================================   
    module pra_data_mod
      implicit none
      
      integer,parameter :: Nt=4000                                ! the size of samples, suggest <99999
      integer,parameter :: Nx=10                                  ! the size of all input predictors, > Np
      integer,parameter :: Ntrain=100                             ! Training Set. <=Nt

      character(len = *), parameter :: rootdir="/home/FCtest/OverFitting/"    ! root dir include code directory
      character(len = *), parameter :: Samplesdir=trim(rootdir)//"samples/"
        
      integer,parameter :: Np=5                                  ! the size of usefull predictors, < Nx
      real Bgiven(Np)
      data Bgiven(1:Np) / 2.0, 1.0,-1.0, 0.5, 0. / 
      !data Bgiven(1:Np) / 5.0,-3.0, 2.0,-1.5,-1.0 / 
      real, parameter :: Fgiven=0.30                              ! the fraction of prediction is known by given equation 
      !logical, parameter :: ORProduceData = .False.    ! False,Read Produced Data. 
      logical, parameter :: ORProduceData = .True.      ! Ture,Producing Samples based on a given equation
      integer,parameter ::  SeedData=4553421               ! used for the producing data 
      real Xsamples(Nx,Nt),Ysample(Nt),Ygiven(Nt),Yrandom(Nt)
      integer XsamplesRank(Nx,Nt),YsampleRank(Nt),YgivenRank(Nt)      ! 0=normal 25%-75%; 1=high; -1=low  
      integer,parameter ::  YgivenRankMethod=0               ! 0---based on sorting
                                                             ! 1---based on the threshould from Ysample

    endmodule pra_data_mod
    








