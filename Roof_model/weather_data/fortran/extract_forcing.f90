

PROGRAM PLOT_VAR
!----------------------------------------------------------------------
! Eida  10/12/2015
!----------------------------------------------------------------------
IMPLICIT NONE
 CHARACTER*100              :: CREPOUT='TXT/'   ! repertoire de sortie
 CHARACTER*1000             :: fichier,FORCAGE
 CHARACTER*100              :: PATH1, PATH2
 INTEGER                    :: J, POINTI
 REAL,DIMENSION(8760)       :: Z
 REAL,DIMENSION(8760)       :: Y

 CHARACTER(len=32) :: arg
 CHARACTER(len=10) :: POINT

 CALL getarg(1, PATH1)
 !READ (arg, '(A)') PATH
 ! '(A)'

 CALL getarg(2, PATH2)
 
 CALL getarg(3, POINT)
 READ(POINT,*) POINTI
 !WRITE(*,*), POINTI
 !READ (arg, *) POINTX

 !Pas touche à partir d'ici

 fichier= trim(PATH1)//'/Forc_LW.bin_france_2013_2014'
 OPEN(UNIT=10,FILE=fichier,STATUS='OLD',FORM='UNFORMATTED', ACCESS='DIRECT'&
	,CONVERT='BIG_ENDIAN',RECL=9892*4) !9892


 DO J=1,8760
  READ (10,REC=J)Z(J)
 ENDDO

 CLOSE(UNIT=10)
 
 fichier=trim(PATH1)//'/Forc_SW.bin_france_2013_2014'
 OPEN(UNIT=20,FILE=fichier,STATUS='OLD',FORM='UNFORMATTED', ACCESS='DIRECT'&
	,CONVERT='BIG_ENDIAN',RECL=9892*4) !9892

 DO J=1,8760
  READ (20,REC=J)Y(J)
 ENDDO

 CLOSE(UNIT=20)

 OPEN(UNIT=11,FILE=trim(PATH2)//'/irradiance_totale_point_'//trim(POINT)//'.txt')
 DO J=1,8760
 WRITE(11,*)Z(J)+Y(J)
 ENDDO
 CLOSE(UNIT=11)

END PROGRAM PLOT_VAR
