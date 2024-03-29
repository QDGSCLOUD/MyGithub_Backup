FC     = ifort 
###FFLAGS = -r8 -i4 -C 
FFLAGS = -check bounds -r8 -i4 -C
OBJS   = main.o \
         statistic_subroutine.o ran_mod.o \
         pra_data_mod.o OverFitting.o preliminary.o 
#----------------------------------------
ROOT_DIR = /home/FCtest/OverFitting
EXEC     = $(ROOT_DIR)/test
VPATH    = $(ROOT_DIR)/code
#----------------------------------------
.PHONY  : all
all     : $(EXEC)
	@echo "EXEC have compiled"
$(EXEC) : $(OBJS)
	$(FC) $(FFLAGS) $^ -o $@  
main.o  : main.f90 pra_data_mod.o preliminary.o OverFitting.o
	$(FC) -c $(FFLAGS) $< -o $@ 
preliminary.o:preliminary.f90 pra_data_mod.o ran_mod.o statistic_subroutine.o
	$(FC) -c $(FFLAGS) $< -o $@
OverFitting.o: OverFitting.f90 statistic_subroutine.o pra_data_mod.o
	$(FC) -c $(FFLAGS) $< -o $@
pra_data_mod.o: pra_data_mod.f90 
	$(FC) -c $(FFLAGS) $< -o $@
statistic_subroutine.o: statistic_subroutine.f90
	$(FC) -c $(FFLAGS) $< -o $@
ran_mod.o: ran_mod.f90 
	$(FC) -c $(FFLAGS) $< -o $@
#----------------------------------------
.PHONY  : clean
clean   :
	rm -f *.mod *.o $(EXEC)
#----------------------------------------
.PHONY  : debug
debug   :
	@echo "VPATH :"$(VPATH)
	@echo "FFLAGS:"$(FFLAGS)

