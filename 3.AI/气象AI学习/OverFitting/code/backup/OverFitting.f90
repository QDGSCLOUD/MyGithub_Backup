module OverFitting        
   use pra_data_mod,only: Nt,Nx,Np,Ntrain,Xsamples,Ysample,Bgiven,Ygiven,Yrandom,Fgiven
   use statistic_subroutine,only: RegStep,RegNp
   implicit none
   private
   save
   
   public :: OFtestOffline ! test overfitting based on Training Set
   
        
   contains
    

    
     subroutine OFtestOffline 
	   real Xin(Nx,Ntrain),Yin(Ntrain)
       real Bout(0:Nx)  ! 各因子对应回归系数，Bout(0)常数项
       real Fout(0:Nx)  ! 各因子的方差贡献，Fout(0)总贡献
       integer Npout,it,i
       do it=1,Ntrain
          Xin(1:Nx,it)=Xsamples(1:Nx,it)
          Yin(it)=Ysample(it)
       enddo   
       write(*,*)  "----Using RegStep----"
       call RegStep(Xin,Yin,Nx,Ntrain,Npout,Bout,Fout)
       write(*,'(a18,2x,2i3,f10.5)') "Ntrain,Np,U/Syy:",Ntrain,Npout,Fout(0)
       do i=1,Nx
          if (Fout(i).gt.1e-30) then
             write(*,'(a5,i2,4x,f8.3,2x,f10.5)') "Y--X",i,Bout(i),Fout(i)
          endif
          if (Fout(i).lt.-1e-30) then
             write(*,'(a5,i2,4x,f8.3,2x,f10.5)') "Y--X",i,Bout(i),Fout(i)
             write(*,*) "F<0"
             stop 
          endif
       enddo 
       write(*,*)  "----Using RegNp----"
       call RegNp(Xin,Yin,Nx,Ntrain,Np,Bout,Fout)
       write(*,'(a18,2x,2i3,f10.5)') "Ntrain,Np,U/Syy:",Ntrain,Np,Fout(0)
       do i=1,Np
          if (Fout(i).gt.1e-30) then
             write(*,'(a5,i2,4x,f8.3,2x,f10.5)') "Y--X",i,Bout(i),Fout(i)
          endif
          if (Fout(i).lt.-1e-30) then
             write(*,'(a5,i2,4x,f8.3,2x,f10.5)') "Y--X",i,Bout(i),Fout(i)
             write(*,*) "F<0"
             stop 
          endif
       enddo 
       
       
     endsubroutine OFtestOffline
     
    
end module OverFitting


