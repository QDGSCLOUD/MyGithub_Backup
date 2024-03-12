function result = liti27(a,b,m,mm)
    %a 是积分下限
    %b是积分上限
    %m是函数的上界
    %mm 是随机实验次数
    frq = 0 ; 
    xrandnum = unifrnd(a,b,1,mm)
    yrandnum = unifrnd(a,b,1,mm)
    for ii = 1:mm 
        if(cos(xrandnum1,ii) +2 >=  yrandnumnum(1,ii)) 
            frq = frq + 1 
        end 
    end 
    result = frq* m * (b-a)/mm