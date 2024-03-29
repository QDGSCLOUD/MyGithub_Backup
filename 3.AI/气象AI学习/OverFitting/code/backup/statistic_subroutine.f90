    module statistic_subroutine                   
       implicit none
       real, parameter :: Fthrehold=3.0    !!!!!!!!!Fthrehold should depend on N and a
       private
       save
       
       public :: normalization
       public :: Normalization_A_S
       public :: anomaly
       
       public :: smooth21point
       
       public :: array_sort
       public :: sorting
       
       public :: correlation
       public :: correlation_test
       public :: correlation_error
       public :: AveVar
       public :: Stwo
       
       public :: orthogonality

       public :: LeastSquareMethod
       public :: LeastSquareMethod_SyyUQF
       
       public :: regressionmine
       public :: regressionmine_S
    
       public :: RegStep 
       public :: RegNp

    contains
    
    !最小二乘法 
    subroutine LeastSquareMethod(X,Y,N,a,b)
      implicit none
      integer N
      real X(N),Y(N)
      real a,b           ! output
      real Xnormal(N),Ynormal(N)
      real Ax,Ay,Sx,Sy   ! A:average  S:mean square deviation
      real rxy           ! correlation
      integer i
      call Normalization_A_S(X,N,Xnormal,Ax,Sx)
      call Normalization_A_S(Y,N,Ynormal,Ay,Sy)
      rxy=0.
      do i=1,N
         rxy=rxy+Xnormal(i)*Ynormal(i)
      enddo
      rxy=rxy/N
      b=rxy*Sy/Sx
      a=Ay-Ax*b
    endsubroutine LeastSquareMethod
   
   !最小二乘法  包括做检验所需信息
   subroutine LeastSquareMethod_SyyUQF(X,Y,N,a,b,Syy,U,Q,F)
      implicit none
      integer N
      real X(N),Y(N)
      real a,b,Syy,U,Q,F ! output
      real Ax,Ay,Sx,Sy   ! A:average S:mean square deviation
      real Xnormal(N),Ynormal(N) 
      real rxy           ! correlation
      real Ytemp
      integer i
      call Normalization_A_S(X,N,Xnormal,Ax,Sx)
      call Normalization_A_S(Y,N,Ynormal,Ay,Sy)
      rxy=0.
      do i=1,N
         rxy=rxy+Xnormal(i)*Ynormal(i)
      enddo
      rxy=rxy/N
      b=rxy*Sy/Sx
      a=Ay-Ax*b
      Syy=0.
      U=0.
      Q=0.
      do i=1,N
         Ytemp=a+X(i)*b
         Syy=Syy+(Y(i)-Ay)**2
         U=U+(Ytemp-Ay)**2
         Q=Q+(Y(i)-Ytemp)**2
      enddo
      F=U*(N-2)/Q
    endsubroutine LeastSquareMethod_SyyUQF
   
   !求相关系数 
   subroutine correlation(X1,X2,N,out)
      implicit none
      integer N
      real X1(N),X2(N)
      real Xnormalization1(N),Xnormalization2(N)
      real out    ! correlation between X1 and X2
      real confidence_level,temp,sum
      integer i
      call normalization(X1,N,Xnormalization1)
      call normalization(X2,N,Xnormalization2)
      out=0.
      do i=1,N
         out=out+Xnormalization1(i)*Xnormalization2(i)
      enddo
      out=out/N
   endsubroutine correlation
   
   !正交化处理 
   subroutine orthogonality(Xin,Xout,Nx,Nt)
      implicit none
      real Xin(Nx,nt),Xout(Nx,Nt)
      integer Nx,Nt
      real Xtemp1(Nt),Xtemp2(Nt),S,S11,S12,Col
      real Xnormalization1(Nt),Xnormalization2(Nt)
      integer i,ii,it
      Xout=Xin
      do i=1,Nx
         Xtemp1(1:Nt)= Xout(i,1:Nt)
         call normalization(Xtemp1,Nt,Xnormalization1)
         Xtemp1=Xnormalization1
         Xout(i,1:Nt)=Xnormalization1
         do ii=i+1,Nx
            Xtemp2(1:Nt)= Xout(ii,1:Nt) 
            call normalization(Xtemp2,Nt,Xnormalization2)
            Xtemp2=Xnormalization2
            S11=0.
            S12=0.
            do it=1,Nt
               S11=S11+Xtemp1(it)*Xtemp1(it) 
               S12=S12+Xtemp1(it)*Xtemp2(it)
            enddo
            if (S11.eq.0.) return
            S=S12/S11
            Xtemp2=Xtemp2-Xtemp1*S 
            Xout(ii,1:Nt)=Xtemp2(1:Nt)
            !call correlation(Xtemp1(1:Nt),Xtemp2(1:Nt),Nt,Col) 
            !write(*,'(2i3,2x,4f12.8)') i,ii,S11,S12,S,Col
         enddo
      enddo   
   endsubroutine orthogonality
   
   
   !求相关系数 做了检验
   subroutine correlation_test(X1,X2,N,out)
      implicit none
      real,parameter :: critical_value=0.1  ! 0.1 0.05 0.01
      integer N						        ! between 20 and 70			 
      real X1(N),X2(N)
      real Xnormalization1(N),Xnormalization2(N)
      real out    ! correlation between X1 and X2, set out=0 under confidence level.
      real confidence_level,temp,sum
      integer i
      call normalization(X1,N,Xnormalization1)
      call normalization(X2,N,Xnormalization2)
      out=0.
      do i=1,N
         out=out+Xnormalization1(i)*Xnormalization2(i)
	    enddo
      out=out/N
      call confidence_value(critical_value,N,confidence_level) 
      if (abs(out).lt.confidence_level) out=0.
    endsubroutine correlation_test
   
   !不同critical_value对应的标准
   subroutine confidence_value(critical_value,N,out)
      implicit none
      real critical_value
      integer N
      real out ! confidence_level t检验
      real table(21:70,1:3)   
      data table(21:70,1:3) / &
          0.369, 0.360, 0.352, 0.344, 0.337, 0.330, 0.323, 0.317, 0.311, 0.306, &
          0.301, 0.296, 0.291, 0.287, 0.283, 0.279, 0.275, 0.271, 0.267, 0.264, &
          0.260, 0.257, 0.254, 0.251, 0.248, 0.246, 0.243, 0.240, 0.238, 0.235, &
          0.233, 0.231, 0.228, 0.226, 0.224, 0.222, 0.220, 0.218, 0.216, 0.214, &
          0.213, 0.211, 0.209, 0.207, 0.206, 0.204, 0.203, 0.201, 0.200, 0.198, &
          0.433, 0.423, 0.413, 0.404, 0.396, 0.388, 0.381, 0.374, 0.367, 0.361, &
          0.355, 0.349, 0.344, 0.339, 0.334, 0.329, 0.325, 0.320, 0.316, 0.312, &
          0.308, 0.304, 0.301, 0.297, 0.294, 0.291, 0.288, 0.285, 0.282, 0.279, &
          0.276, 0.273, 0.271, 0.268, 0.266, 0.263, 0.261, 0.259, 0.256, 0.254, &
          0.252, 0.250, 0.248, 0.246, 0.244, 0.242, 0.240, 0.239, 0.237, 0.235, &
          0.549, 0.537, 0.526, 0.515, 0.505, 0.496, 0.487, 0.479, 0.471, 0.463, &
          0.456, 0.449, 0.442, 0.436, 0.430, 0.424, 0.418, 0.413, 0.408, 0.403, &
          0.398, 0.393, 0.389, 0.384, 0.380, 0.376, 0.372, 0.368, 0.365, 0.361, &
          0.358, 0.354, 0.351, 0.348, 0.345, 0.341, 0.339, 0.336, 0.333, 0.330, &
          0.327, 0.325, 0.322, 0.320, 0.317, 0.315, 0.313, 0.310, 0.308, 0.306  /
      if ((N.lt.21).or.(N.gt.70)) then
         write(*,*) "N=",N
         write(*,*) "N must between 21 and 70"
         stop 353
      endif
      select case (int(critical_value*100+0.1))
      case(10)
         out=table(N,1)
      case(5)
         out=table(N,2)
      case(1)
         out=table(N,3)
      case default
         write(*,*) "critical_value=",critical_value
         write(*,*)  "critical_value must be set 0.1 0.05 0.01"
      stop 365
      end select 
   endsubroutine  confidence_value
   
   !求相关系数和差值的均方根
   subroutine correlation_error(X1,X2,N,Col,Err)
      implicit none
      integer N
      real X1(N),X2(N)
      real Xnormalization1(N),Xnormalization2(N)
      real Col    ! correlation between X1 and X2
      real Err    ! error between X1 and X2
      real temp,sum
      integer i
      call normalization(X1,N,Xnormalization1)
      call normalization(X2,N,Xnormalization2)
      Col=0.
      Err=0.
      do i=1,N
         Col=Col+Xnormalization1(i)*Xnormalization2(i)
         Err=Err+(X1(i)-X2(i))**2
      enddo
      Col=Col/N
      Err=sqrt(Err/N)
   endsubroutine correlation_error
   
   !求数组去掉平均值的平方和
   subroutine AveVar(Xin,N,Ave,Var)
      implicit none
      integer N
      real Xin(N)
      real Ave,Var
      integer i
      Ave=0.
      do i=1,N
         Ave=Ave+Xin(i) 
      enddo
      Ave=Ave/N
      Var=0.
      do i=1,N
         Var=Var+(Xin(i)-Ave)**2 
      enddo    
   end subroutine AveVar
   
   !求数组X和Y的协方差
   subroutine Stwo(Xin,Yin,N,S)
      implicit none
      integer N
      real Xin(N),Yin(N),S
      real Xave,Yave
      integer i
      Xave=0.
      Yave=0.
      do i=1,N
         Xave=Xave+Xin(i) 
         Yave=Yave+Yin(i)
      enddo
      Xave=Xave/N
      Yave=Yave/N
      S=0.
      do i=1,N
         S=S+(Xin(i)-Xave)*(Yin(i)-Yave) 
      enddo    
   end subroutine Stwo
   
   !标准化
   subroutine normalization(Xin,N,Xout)
      implicit none
      integer N
      real Xin(N),Xout(N)
      real sum
      integer i
      sum=0.
      do i=1,N
         sum=sum+Xin(i)
      enddo
      sum=sum/N
      do i=1,N
         Xout(i)=Xin(i)-sum
      enddo
      sum=0.
      do i=1,N
         sum=sum+Xout(i)**2
      enddo
      if (sum.eq.0.) return
      sum=sum/N
      sum=sqrt(sum)
      do i=1,N
         Xout(i)=Xout(i)/sum
      enddo
   endsubroutine normalization
   
!标准化
   subroutine smooth21point(Xin,N,Xaverageout,Xanomalyout)
      implicit none
      integer N
      real Xin(N),Xaverageout(N),Xanomalyout(N)
      real sum
      integer i,ii
      if (N.le.21) then
         write(*,*) "smooth21point, N must > 21",N  
         stop 2323        
      endif   
      do i=11,N-10
         sum=0.
         do ii=i-10,i+10
            sum=sum+Xin(ii)
         enddo
         Xaverageout(i)=sum/21
      enddo 
      Xaverageout(1:10)=Xaverageout(11)
      Xaverageout(N-9:N)=Xaverageout(N-10)
      do i=1,N
         Xanomalyout(i)=Xin(i)-Xaverageout(i)
      enddo
   endsubroutine smooth21point
   
   subroutine array_sort(Var,yys,yye,yysort)
      implicit none
      integer,intent(in) :: yys,yye
      real,intent(in) :: Var(yys:yye)
      integer,intent(out) :: yysort(yye-yys+1)
      integer yy,ii,yytemp(yys:yye),inttemp
      real realtemp,Vartemp(yys:yye)
      do yy=yys,yye
         yytemp(yy)=yy
         Vartemp(yy)=Var(yy)
      enddo
      do ii=1,yye-yys
         do yy=yys,yye-ii
            if (Vartemp(yy).gt.Vartemp(yy+1)) then
               realtemp=Vartemp(yy)
               Vartemp(yy)=Vartemp(yy+1)
               Vartemp(yy+1)=realtemp
               inttemp=yytemp(yy)
               yytemp(yy)=yytemp(yy+1)
               yytemp(yy+1)=inttemp
            endif
         enddo
      enddo
      do ii=1,yye-yys+1
         yy=yys+ii-1
         yysort(ii)=yytemp(yy)
      enddo
   endsubroutine array_sort

   ! sort(1:N)记录从大到小排序，即sort(1)的值表示Var数组中最大值拍在第几个
   subroutine sorting(Var,N,sort)
      implicit none
      integer,intent(in) :: N
      real,intent(in) :: Var(1:N)
      integer,intent(out) :: sort(1:N)
      integer i,ii,sorttemp(1:N),inttemp
      real realtemp,Vartemp(1:N)
      do ii=1,N
         sorttemp(ii)=ii
         Vartemp(ii)=Var(ii)
      enddo
      do i=1,N
         do ii=1,N-i
            if (Vartemp(ii).gt.Vartemp(ii+1)) then
               realtemp=Vartemp(ii)
               Vartemp(ii)=Vartemp(ii+1)
               Vartemp(ii+1)=realtemp
               inttemp=sorttemp(ii)
               sorttemp(ii)=sorttemp(ii+1)
               sorttemp(ii+1)=inttemp
            endif
         enddo
      enddo
      do ii=1,N
         sort(ii)=sorttemp(N+1-ii)
      enddo
    endsubroutine sorting
   
   !标准化 包括Average,MeanSquareDeviation
   subroutine Normalization_A_S(Xin,N,Xout,Average,MeanSquareDeviation)
      implicit none
      integer N
      real Xin(N),Xout(N)
      real Average,MeanSquareDeviation  ! output variable
      real sum
      integer i
      sum=0.
      do i=1,N
         sum=sum+Xin(i)
      enddo
      sum=sum/N
      Average=sum
      do i=1,N
         Xout(i)=Xin(i)-sum
      enddo
      sum=0.
      do i=1,N
         sum=sum+Xout(i)**2
      enddo
      if (sum.eq.0.) return
      sum=sum/N
      sum=sqrt(sum)
      MeanSquareDeviation=sum
      do i=1,N
         Xout(i)=Xout(i)/sum
      enddo
    endsubroutine Normalization_A_S
   
   !求距平
    subroutine anomaly(Xin,N,Xout)
      implicit none
      integer N
      real Xin(N),Xout(N)
      real sum
      integer i
      sum=0.
      do i=1,N
         sum=sum+Xin(i)
      enddo
      sum=sum/N
      do i=1,N
         Xout(i)=Xin(i)-sum
      enddo
    endsubroutine anomaly
    
    ! 求矩阵Ain(N,N)的逆矩阵Aout(N,N)
    subroutine GaussElimination(Ain,N,Aout)
      implicit none
      integer N
      real Ain(N,N),Aout(N,N)  !(i行,j列)
      real T(N,N),temp(N)
      real max,f
      integer i,j,imax
      Aout(:,:)=0.0
      do i=1,N
         Aout(i,i)=1.0
      enddo
      T(:,:)=Ain(:,:)
      do j=1,N-1
         max=T(j,j)
         imax=j
         do i=j+1,N
            if (abs(T(i,j)).gt.abs(max)) then
               max=T(i,j)
               imax=i
            endif
         enddo
         !write(*,*) "j,max,imax  ",j,imax,max
         if (imax.ne.j) then  
            temp(:)=T(j,:)
            T(j,:)=T(imax,:)
            T(imax,:)=temp(:)
            temp(:)=Aout(j,:)
            Aout(j,:)=Aout(imax,:)
            Aout(imax,:)=temp(:)           
         endif
         if (abs(max).gt.1e-20) then
            do i=j+1,N
               f=T(i,j)/T(j,j)
               T(i,:)   =T(i,:)   -T(j,:)   *f
               Aout(i,:)=Aout(i,:)-Aout(j,:)*f
            enddo
         else
            write(*,*) "!!!no inverse matrix!!!  stop " 
            stop 222
         endif         
         !write(*,*) "3x3 test ",j
         !do i=1,3
         !   write(*,'(i3,3x,3f8.1,3x,3f8.1)') i,T(i,:),Aout(i,:)
         !enddo
         !write(*,*) 
      enddo
      if (abs(T(N,N)).le.1e-20) then
         write(*,*) "!!!no inverse matrix!!!  stop " 
         stop 222 
      endif
      do j=N,2,-1
         do i=1,j-1
            f=T(i,j)/T(j,j)
            T(i,:)   =T(i,:)   -T(j,:)   *f
            Aout(i,:)=Aout(i,:)-Aout(j,:)*f
         enddo
         !write(*,*) "3x3 test ",j
         !do i=1,3
         !   write(*,'(i3,3x,3f8.1,3x,3f8.1)') i,T(i,:),Aout(i,:)
         !enddo
         !write(*,*) 
      enddo
      do i=1,N
         f=T(i,i)
         T(i,:)   =T(i,:)   /f
         Aout(i,:)=Aout(i,:)/f        
      enddo    
      !write(*,*) "3x3 test    T  Aout "
      !do i=1,3
      !   write(*,'(i3,3x,3f8.1,3x,3f8.1)') i,T(i,:),Aout(i,:)
      !enddo
      !write(*,*)
    endsubroutine GaussElimination

    ! 求样本Xin(P,N)、Yin(N)的多元线性回归
    subroutine regressionmine(Xin,Yin,N,P,Bout)
      implicit none
      integer P,N    !N样本数，P预报因子数
      real Xin(P,N),Yin(N)  ! 原始数据
      real Bout(0:P)        ! B各因子系数
      real Xmean(P),Ymean   ! 平均值
      real X(P,N),Y(N)      ! 距平
      real Sxx(P,P),Sxy(P),Sxx_1(P,P)  !S协方差矩阵，S_1为S的逆矩阵 (i行,j列)
      real sum
      integer i,j,t  
      sum=0.0
      do t=1,N
         sum=sum+Yin(t)
      enddo
      Ymean=sum/N
      do t=1,N
         Y(t)=Yin(t)-Ymean
      enddo
      do i=1,P
         sum=0.0
         do t=1,N
            sum=sum+Xin(i,t)
         enddo
         Xmean(i)=sum/N
         do t=1,N
            X(i,t)=Xin(i,t)-Xmean(i)
         enddo
      enddo     
      do i=1,P
      do j=1,P
         sum=0.0
         do t=1,N
            sum=sum+X(i,t)*X(j,t)      
         enddo
         Sxx(i,j)=sum/N    
      enddo
      enddo
      do i=1,p
         sum=0.0
         do t=1,N
            sum=sum+X(i,t)*Y(t)      
         enddo
         Sxy(i)=sum/N
      enddo
      call GaussElimination(Sxx,P,Sxx_1)
      do i=1,P
         Bout(i)=0.0
         do j=1,P
            Bout(i)=Bout(i)+Sxx_1(i,j)*Sxy(j)
         enddo
      enddo
      Bout(0)=Ymean
      do i=1,P
         Bout(0)=Bout(0)-Bout(i)*Xmean(i)
      enddo  
    endsubroutine regressionmine

    ! 求样本Xin(P,N)、Yin(N)的多元线性回归,给出S协方差矩阵
    subroutine regressionmine_S(Xin,Yin,N,P,Bout,Sout,Sout_1)
      implicit none
      integer P,N    !N样本数，P预报因子数
      real Xin(P,N),Yin(N)  ! 原始数据
      real Bout(0:P)        ! B各因子系数
      real Sout(P,P),Sout_1(P,P)   ! S协方差矩阵，S_1为S的逆矩阵 (i行,j列)
      real Xmean(P),Ymean   ! 平均值
      real X(P,N),Y(N)      ! 距平
      real Sxx(P,P),Sxy(P),Sxx_1(P,P)  !S协方差矩阵，S_1为S的逆矩阵 (i行,j列)
      real sum
      integer i,j,t  
      sum=0.0
      do t=1,N
         sum=sum+Yin(t)
      enddo
      Ymean=sum/N
      do t=1,N
         Y(t)=Yin(t)-Ymean
      enddo
      do i=1,P
         sum=0.0
         do t=1,N
            sum=sum+Xin(i,t)
         enddo
         Xmean(i)=sum/N
         do t=1,N
            X(i,t)=Xin(i,t)-Xmean(i)
         enddo
      enddo     
      do i=1,P
      do j=1,P
         sum=0.0
         do t=1,N
            sum=sum+X(i,t)*X(j,t)      
         enddo
         !Sxx(i,j)=sum/N  
         Sxx(i,j)=sum
      enddo
      enddo
      Sout=Sxx
      do i=1,p
         sum=0.0
         do t=1,N
            sum=sum+X(i,t)*Y(t)      
         enddo
         !Sxy(i)=sum/N
         Sxy(i)=sum
      enddo
      call GaussElimination(Sxx,P,Sxx_1)
      Sout_1=Sxx_1
      do i=1,P
         Bout(i)=0.0
         do j=1,P
            Bout(i)=Bout(i)+Sxx_1(i,j)*Sxy(j)
         enddo
      enddo
      Bout(0)=Ymean
      do i=1,P
         Bout(0)=Bout(0)-Bout(i)*Xmean(i)
      enddo  
    endsubroutine regressionmine_S
    
!   逐步回归 最少用三个因子
    subroutine RegStep(Xin,Yin,Nx,Nt,Npout,Bout,Fout) 
      implicit none
      integer Nx,Nt    !Nt样本数，Nx总预报因子数
      real Xin(Nx,Nt),Yin(Nt)  ! 原始数据
      integer Npout             ! 所用预报因子个数
      real Bout(0:Nx)          ! B各因子系数  
      real Fout(0:Nx)          ! Fout(0)=U/Syy, Fout(1:Nx)各个因子的贡献
      real cor,XYcor(Nx)
      real B(0:Nx)             ! 各因子系数 B(0)常数项 仅前0:Np有效
      real, dimension(:,:), allocatable :: SS,SS_1          ! SS(Np,Np)协方差矩阵，SS_1(Np,Np)为SS的逆矩阵 (行,列)
      real, dimension(:,:), allocatable :: Xreg             ! Xreg(Np,Nt)  
      real Fmin,Xone(Nt),YU(Nt),YQ(Nt),U,Q,Syy,Sxy,ave,Uone,Umin,cormax,sumF
      integer i,ii,t,Np,ix,imin,imax,sort(Nx),Xuse(Nx),Xstate(Nx),xcount,addstate
      if (Nx.lt.3 ) then
         write(*,*) "RegStep Nx must >=3", Nx
         stop  
      endif    
      do i=1,Nx
         Xone(1:Nt)=Xin(i,1:Nt)
         call correlation(Xone,Yin,Nt,cor)
         XYcor(i)=cor*cor
         !write(*,'(i2,2x,2f10.5)') i,XYcor(i),cor 
      enddo
      call sorting(XYcor,Nx,sort)
      Xuse(:)=0
      Xstate(:)=0
      Np=2
      allocate(Xreg(Np,Nt))
      do i=1,Np
         ii=sort(i)
         Xuse(i)=ii
         Xstate(ii)=1
         Xreg(i,1:Nt)=Xin(ii,1:Nt)
         !write(*,'(2i3,2x,2i3)') i,ii,Xuse(i),Xstate(ii)
      enddo
      B(:)=0.
      call regressionmine(Xreg(1:Np,1:Nt),Yin(1:Nt),Nt,Np,B(0:Np))
      do t=1,Nt
         YU(t)=B(0)
         do ix=1,NP
            YU(t)=YU(t)+Xreg(ix,t)*B(ix) 
         enddo
         YQ(t)=Yin(t)-YU(t)
         !write(*,'(i3,2x,3f8.3)') t,YU(t),YQ(t),Yin(t)
      enddo
      call AveVar(Yin,Nt,ave,Syy)
      !write(*,*) ave,Syy
      call AveVar(YU ,Nt,ave,U) ! test only
      !write(*,*) ave,U
      call AveVar(YQ ,Nt,ave,Q) ! test only
      !write(*,*) ave,Q
      !write(*,'(a18,i2,3f12.3,5x,f8.4)') "Np,Syy,U,Q,U/Syy:",Np,Syy,U,Q,U/Syy 
      deallocate(Xreg)
      addstate=1
      do while(addstate.gt.0) !!
         xcount=0 
         Xuse(:)=0
         do ix=1,Nx
         if (Xstate(ix).eq.1) then
             xcount=xcount+1
             Xuse(xcount)=ix
         endif       
         enddo
         Np=xcount
         xcount=0 
         XYcor(:)=0.
         cormax=-999.9
         imax=-9999
         do ix=1,Nx
         if (Xstate(ix).eq.0) then
            xcount=xcount+1
            Xone(1:Nt)=Xin(ix,1:Nt)
            call correlation(Xone,YQ,Nt,cor) !!! 
            XYcor(ix)=cor*cor
            if (cormax.le.XYcor(ix)) then
                cormax=XYcor(ix)
                imax=ix
            endif    
            !write(*,'(2i4,2x,f8.4)') xcount,ix,XYcor(ix)
         endif       
         enddo    
         if (xcount.gt.0) then 
            Np=Np+1 
            !write(*,*) "Np & add imax",Np,imax
            Xuse(Np)=imax
            Xstate(imax)=1
            allocate(Xreg(Np,Nt))
            allocate(SS(Np,Np))
            allocate(SS_1(Np,Np))
            do i=1,Np
               ii=Xuse(i) 
               Xreg(i,1:Nt)=Xin(ii,1:Nt)
               !write(*,'(2i4,2x,2i4)') i,ii,Xuse(i),Xstate(ii)
            enddo
            B(:)=0.
            SS(:,:)=-999.9
            SS_1(:,:)=-999.9
            call regressionmine_S(Xreg(1:Np,1:Nt),Yin(1:Nt),Nt,Np,B(0:Np),SS(1:Np,1:Np),SS_1(1:Np,1:Np))
            do t=1,Nt
               YU(t)=B(0)
               do ix=1,NP
                  YU(t)=YU(t)+Xreg(ix,t)*B(ix) 
               enddo
               YQ(t)=Yin(t)-YU(t)
               !write(*,'(i3,2x,3f8.3)') t,YU(t),YQ(t),Yin(t)
            enddo
            call AveVar(YU ,Nt,ave,U) ! test only
            call AveVar(YQ ,Nt,ave,Q)
            !write(*,'(a18,i2,3f12.3,5x,f8.4)') "Np,Syy,U,Q,U/Syy:",Np,Syy,U,Q,U/Syy 
            Umin=1e20
            imin=-999
            do ix=1,Np
               Uone=B(ix)**2/SS_1(ix,ix)
               if (Umin.gt.Uone) then
                  Umin=Uone
                  imin=ix
               endif   
               !write(*,'(a18,2i4,f12.3,5x,f8.4)') "ix,Uone,Uone/Syy: ", ix,Xuse(ix),Uone,Uone/Syy
            enddo  
            Fmin=Umin*(Nt-Np-1)/Q
            !write(*,'(a28,2i4,2f8.3)') "imin,Xuse(imin),Umin,Fmin: ", imin,Xuse(imin),Umin,Fmin
            deallocate(Xreg)
            deallocate(SS)
            deallocate(SS_1)
            if (Fmin.le.Fthrehold)  then
                Xstate(Xuse(imin))=-1
                !write(*,*) "remove:",Xuse(imin)
                if (Xuse(imin).eq.imax) addstate=0
            endif
         else   
            !write(*,*) "xcount.eq.0",addstate
            addstate=0
         endif
         !write(*,*) "addstate",addstate
      end do !do while
      xcount=0 
      Xuse(:)=0
      do ix=1,Nx
      if (Xstate(ix).eq.1) then
         xcount=xcount+1
         Xuse(xcount)=ix
      endif       
      enddo
      Np=xcount
      if (Np.lt.2) stop "RegStep Stop"
      allocate(Xreg(Np,Nt))
      allocate(SS(Np,Np))
      allocate(SS_1(Np,Np))
      do i=1,Np
         ii=Xuse(i) 
         Xreg(i,1:Nt)=Xin(ii,1:Nt)
         !write(*,'(2i4)') i,ii
      enddo
      B(:)=0.
      SS(:,:)=-999.9
      SS_1(:,:)=-999.9
      !call regressionmine(Xreg(1:Np,1:Nt),Yin(1:Nt),Nt,Np,B(0:Np))
      call regressionmine_S(Xreg(1:Np,1:Nt),Yin(1:Nt),Nt,Np,B(0:Np),SS(1:Np,1:Np),SS_1(1:Np,1:Np))
      do t=1,Nt
         YU(t)=B(0)
         do ix=1,NP
            YU(t)=YU(t)+Xreg(ix,t)*B(ix) 
         enddo
         YQ(t)=Yin(t)-YU(t)
         !write(*,'(i3,2x,3f8.3)') t,YU(t),YQ(t),Yin(t)
      enddo
      call AveVar(YU ,Nt,ave,U) 
      !call AveVar(YQ ,Nt,ave,Q) ! test only
      !write(*,'(a18,i2,3f12.3,5x,f8.4)') "Np,Syy,U,Q,U/Syy:",Np,Syy,U,Q,U/Syy 
      if ((Np.eq.2).and.(U/Syy.lt.2*Fthrehold/Nt)) then   !!!  
         !write(*,*) "Np,U/Syy:",Np,U/Syy 
         U=0.
         Np=0
         B(:)=0.
      endif   
      Fout(:)=0.
      Fout(0)=U/Syy
      Npout=Np
      Bout(:)=0.
      Bout(0)=B(0)
      sumF=0.
      do i=1,Np
         ii=Xuse(i) 
         Bout(ii)=B(i)
         !!!!! U/Syy=sumF,  F might <0
         Xone(1:Nt)=Xin(ii,1:Nt)
         call Stwo(Xone,Yin,Nt,Sxy)
         Fout(ii)=B(i)*Sxy/Syy
         !!!!! U/Syy.ne.sumF, F allways > 0
         !Fout(ii)=Bout(ii)**2/SS_1(i,i)/Syy
         sumF=sumF+Fout(ii)
         !write(*,'(2i4,2x,2f8.3)') i,ii,Bout(ii),Fout(ii)
      enddo
      !write(*,'(a18,i4,2x,f8.3,2x,2f8.3)') "Np,B0,U/Syy,sumF",Np,Bout(0),Fout(0),sumF
      deallocate(Xreg)
      deallocate(SS)
      deallocate(SS_1)
      !do i=1,Nx
      !   write(*,'(i4,2x,2f8.3)') i,Bout(i),Fout(i)
      !enddo
    endsubroutine RegStep
    
! 多元线性回归  仅采用前Np个预测因子
    subroutine RegNp(Xin,Yin,Nx,Nt,Np,Bout,Fout) 
      implicit none
      integer Nx,Nt,Np         ! Nt样本数，Nx总预报因子数 仅采用前Np个预测因子
      real Xin(Nx,Nt),Yin(Nt)  ! 原始数据
      real Bout(0:Nx)          ! B各因子系数   各因子系数 B(0)常数项 仅前0:Np有效
      real Fout(0:Nx)          ! Fout(0)=U/Syy, Fout(1:Nx)各个因子的贡献
      real Xreg(Np,Nt),B(0:Np)             ! 各因子系数 B(0)常数项 仅前0:Np有效
      real Xone(Nt),YU(Nt),YQ(Nt),U,Q,Syy,Sxy,ave,sumF 
      integer ix,it,i
      do it=1,Nt
         Xreg(1:Np,it)=Xin(1:Np,it)
      enddo    
      call regressionmine(Xreg(1:Np,1:Nt),Yin(1:Nt),Nt,Np,B(0:Np))
      do it=1,Nt
         YU(it)=B(0)
         do ix=1,Np
            YU(it)=YU(it)+Xreg(ix,it)*B(ix) 
         enddo
         YQ(it)=Yin(it)-YU(it)
         !write(*,'(i3,2x,3f8.3)') it,YU(it),YQ(it),Yin(it)
      enddo
      call AveVar(Yin,Nt,ave,Syy)
      call AveVar(YU ,Nt,ave,U) 
      Fout(:)=0.
      Fout(0)=U/Syy
      Bout(:)=0.
      Bout(0)=B(0)
      sumF=0.
      do i=1,Np
         Bout(i)=B(i)
         Xone(1:Nt)=Xin(i,1:Nt)
         call Stwo(Xone,Yin,Nt,Sxy)
         Fout(i)=B(i)*Sxy/Syy
         sumF=sumF+Fout(i)
         !write(*,'(i4,2x,2f8.3)') i,Bout(i),Fout(i)  
      enddo
      !write(*,'(a18,i4,2x,f8.3,2x,2f8.3)') "Np,B0,U/Syy,sumF",Np,Bout(0),Fout(0),sumF
    endsubroutine RegNp 
    
    end module statistic_subroutine