!====================================================================  
!  Auther: Xiangjun Shi(Ê·Ïæ¾ü)  
!  Email: shixj@nuist.edu.cn  
!====================================================================  
    module preliminary  
       use pra_data_mod,only: Nt,Nx,Np,Ntrain,Samplesdir, &
                              Xsamples,Ysample,Bgiven,Ygiven,Yrandom,Fgiven,XsamplesRank,YsampleRank,YgivenRank,YgivenRankMethod, &
                              ORProduceData,SeedData
       use ran_mod,only: SetSeed,Rnormal
       use statistic_subroutine,only: AveVar,normalization,orthogonality,Normalization_A_S,correlation,Stwo,sorting
       implicit none
       character(len=8) cSeed
       private
       save

       public :: LoadData
       public :: DataAnalyze

    contains

    subroutine ProduceObsData
       implicit none
       real mean,sigma,Rantemp(Nt)
       real Xtemp1(Nx+1,Nt),Xtemp2(Nx+1,Nt),Ayy,Syy
       integer ix,i
       write(cSeed(1:8),'(i8)') mod(SeedData,10000000)+10000000
       call SetSeed(SeedData)    
       mean=0.
       sigma=1.0
       do i=1,Nt
       do ix=1,Nx+1
          Xtemp1(ix,i)=Rnormal(mean,sigma)
       enddo
       enddo 
       call orthogonality(Xtemp1,Xtemp2,Nx+1,Nt)
       Xsamples(1:Nx,1:Nt)=Xtemp2(1:Nx,1:Nt)
       Rantemp(1:Nt)=Xtemp2(Nx+1,1:Nt)
       call normalization(Rantemp,Nt,Yrandom)
       do i=1,Nt
          Ygiven(i)=0. 
          do ix=1,Np
             Ygiven(i)=Ygiven(i)+Xsamples(ix,i)*Bgiven(ix) 
          enddo 
       enddo
       call Normalization_A_S(Ygiven,Nt,Rantemp,Ayy,Syy)
       !write(*,*) "Ygiven,Ave,Var:",Ayy,Syy
       if (Fgiven.ge.1e-20) then
          Yrandom=Yrandom*Syy*sqrt((1.0-Fgiven)/Fgiven)       !!!!!
          Ysample=Ygiven+Yrandom
       else
          Ygiven=0.
          Ysample=Ygiven+Yrandom
       endif   
       open(22,file=Samplesdir//cSeed//"_samples.txt",form="formatted")
       do i=1,Nt
          write(22,('(i6,2x,<Nx>f8.4,2x,f8.4,2x,f8.4,2x,f8.4)')) i,Xsamples(1:Nx,i),Ygiven(i),Yrandom(i),Ysample(i)
       enddo
       close(22)
    endsubroutine ProduceObsData
    
    subroutine LoadData
       implicit none
       real Xtemp(Nx),Ytemp1,Ytemp2,Ytemp3
       real ave,cor,Xone(Nt),Sxy,sum,Syy,U,Q
       integer itemp,i
       if (ORProduceData) then
          call ProduceObsData
       else    
          write(cSeed(1:8),'(i8)') mod(SeedData,10000000)+10000000
          open(22,file=Samplesdir//cSeed//"_samples.txt",form="formatted")
          do i=1,Nt
             read(22,('(i6,2x,<Nx>f8.4,2x,f8.4,2x,f8.4,2x,f8.4)')) itemp,Xtemp(1:Nx),Ytemp1,Ytemp2,Ytemp3
             Xsamples(1:Nx,i)=Xtemp(1:Nx)
             Ygiven(i)=Ytemp1
             Yrandom(i)=Ytemp2
             Ysample(i)=Ytemp3
             !write(*,('(i6,2x,<Np>f8.4,2x,f8.4,2x,f8.4)')) i,Xsamples(1:Np,i),Ygiven(i),Ysample(i)
             !write(*,('(i6,2x,<Nx>f8.4,2x,f8.4,2x,f8.4,2x,f8.4)')) i,Xsamples(1:Nx,i),Ygiven(i),Yrandom(i),Ysample(i)
          enddo
          close(22)
       endif 
       call AveVar(Ysample,Nt,ave,Syy)
       call AveVar(Ygiven ,Nt,ave,U)
       call AveVar(Yrandom,Nt,ave,Q)
       write(*,*) "All samples ", Nt
       write(*,'(a18,3f12.3,5x,2f8.4)') "Syy,U,Q,U/Syy,cor:",Syy,U,Q,U/Syy,sqrt(U/Syy) 
       sum=0.
       do i=1,Np
          Xone(1:Nt)=Xsamples(i,1:Nt)
          call correlation(Xone,Ysample,Nt,cor)
          call Stwo(Xone,Ysample,Nt,Sxy)
          write(*,'(a5,i2,4x,f8.3,2x,2f10.5)') "Y--X",i,Bgiven(i),cor,Bgiven(i)*Sxy/Syy
          sum=sum+Bgiven(i)*Sxy/Syy
       enddo 
       write(*,*) "sum of Bgiven(i)*Sxy/Syy",sum
       XsamplesRank(:,:)=0
       YsampleRank(:)=0
       YgivenRank(:)=0
    endsubroutine LoadData
     
    subroutine DataAnalyze
       implicit none
       real Xone(Nt),Yhigh,Ylow
       integer itemp,ix,i,isort(Nt),N25,N75,isumH,isumL,isumN,isum
       N25=Nt/4
       N75=Nt-N25+1
       YsampleRank(:)=0
       call sorting(Ysample,Nt,isort)
       Yhigh=0.5*(Ysample(isort(N25))+Ysample(isort(N25+1)))
       Ylow =0.5*(Ysample(isort(N75))+Ysample(isort(N75-1)))
       write(*,*) "Yhigh,Ylow:",Yhigh,Ylow
       do i=1,Nt
          itemp=isort(i)
          if (i.le.N25) YsampleRank(itemp)= 1
          if (i.ge.N75) YsampleRank(itemp)=-1
          !write(*,*) i,itemp,Ysample(itemp),YsampleRank(itemp)
       enddo  
       YgivenRank(:)=0
       if (YgivenRankMethod.eq.0) then
          call sorting(Ygiven,Nt,isort)
          do i=1,Nt
             itemp=isort(i)
             if (i.le.N25) YgivenRank(itemp)= 1
             if (i.ge.N75) YgivenRank(itemp)=-1
             !write(*,*) i,itemp,Ygiven(i),YgivenRank(itemp)
          enddo
       endif
       if (YgivenRankMethod.eq.1) then
          do i=1,Nt
             if (Ygiven(i).gt.Yhigh) YgivenRank(i)= 1
             if (Ygiven(i).lt.Ylow)  YgivenRank(i)=-1
             !write(*,*) i,Ygiven(i),YgivenRank(i)
          enddo
       endif   
       if ((YgivenRankMethod.ne.0).and.(YgivenRankMethod.ne.1)) then
          write(*,*)   "YgivenRankMethod must be 0 1"
          stop 2323
       endif 
       XsamplesRank(:,:)=0
       do ix=1,Np !!Np or Nx
          !write(*,*) "ix",ix
          Xone(1:Nt)=Xsamples(ix,1:Nt)
          call sorting(Xone,Nt,isort)
          do i=1,Nt
             itemp=isort(i)
             if (i.le.N25) XsamplesRank(ix,itemp)= 1
             if (i.ge.N75) XsamplesRank(ix,itemp)=-1
             !write(*,*) i,itemp,Xsamples(ix,itemp),XsamplesRank(ix,itemp)
          enddo 
       enddo
       do ix=1,Np  !!Np or Nx  
          isumH=0
          isumN=0
          isumL=0
          isum=0
          do i=1,Nt
          if (XsamplesRank(ix,i).eq.1) then
             isum=isum+1
             if (YsampleRank(i).eq. 1)  isumH=isumH+1
             if (YsampleRank(i).eq. 0)  isumN=isumN+1
             if (YsampleRank(i).eq.-1)  isumL=isumL+1
          endif   
          enddo 
          write(*,'(i5,a6,i5,a12,3i5)') ix," XHigh",isum,"YRank L N H",isumL,isumN,isumH
          isumH=0
          isumN=0
          isumL=0
          isum=0
          do i=1,Nt   
          if (XsamplesRank(ix,i).eq.-1) then
             isum=isum+1
             if (YsampleRank(i).eq. 1)  isumH=isumH+1
             if (YsampleRank(i).eq. 0)  isumN=isumN+1
             if (YsampleRank(i).eq.-1)  isumL=isumL+1
          endif   
          enddo 
          write(*,'(i5,a6,i5,a12,3i5)') ix," XLow ",isum,"YRank L N H",isumL,isumN,isumH
       enddo
       isumH=0
       isumN=0
       isumL=0
       isum=0
       do i=1,Nt
       if (YgivenRank(i).eq.1) then
          isum=isum+1
          if (YsampleRank(i).eq. 1)  isumH=isumH+1
          if (YsampleRank(i).eq. 0)  isumN=isumN+1
          if (YsampleRank(i).eq.-1)  isumL=isumL+1
       endif   
       enddo 
       write(*,'(a13,i5,a12,3i5)') "YgivenHigh ",isum,"YRank L N H",isumL,isumN,isumH
       if (isum.gt.0) write(*,'(a13,i5,a12,3i5)') "YgivenHigh%",isum*100/nt,"YRank L N H",isumL*100/isum,isumN*100/isum,isumH*100/isum
       isumH=0
       isumN=0
       isumL=0
       isum=0
       do i=1,Nt
       if (YgivenRank(i).eq.-1) then
          isum=isum+1
          if (YsampleRank(i).eq. 1)  isumH=isumH+1
          if (YsampleRank(i).eq. 0)  isumN=isumN+1
          if (YsampleRank(i).eq.-1)  isumL=isumL+1
       endif   
       enddo 
       write(*,'(a13,i5,a12,3i5)') "YgivenLow ",isum,"YRank L N H",isumL,isumN,isumH
       if (isum.gt.0) write(*,'(a13,i5,a12,3i5)') "YgivenLow%",isum*100/nt,"YRank L N H",isumL*100/isum,isumN*100/isum,isumH*100/isum
       isumH=0
       isumN=0
       isumL=0
       isum=0
       do i=1,Nt
       if (YsampleRank(i).eq. 1) then
          isum=isum+1
          if (Ygiven(i).gt.Yhigh)  isumH=isumH+1
          if ((Ygiven(i).le.Yhigh).and.(Ygiven(i).ge.Ylow))  isumN=isumN+1
          if (Ygiven(i).lt.Ylow)  isumL=isumL+1
       endif   
       enddo 
       write(*,'(a11,i5,a12,3i5)') "YsampleHigh",isum,"Ygiven L N H",isumL,isumN,isumH
       isumH=0
       isumN=0
       isumL=0
       isum=0
       do i=1,Nt
       if (YsampleRank(i).eq.-1) then
          isum=isum+1
          if (Ygiven(i).gt.Yhigh)  isumH=isumH+1
          if ((Ygiven(i).le.Yhigh).and.(Ygiven(i).ge.Ylow))  isumN=isumN+1
          if (Ygiven(i).lt.Ylow)  isumL=isumL+1
       endif   
       enddo 
       write(*,'(a11,i5,a12,3i5)') "YsampleLow ",isum,"Ygiven L N H",isumL,isumN,isumH
    endsubroutine DataAnalyze   
    
    end module preliminary


