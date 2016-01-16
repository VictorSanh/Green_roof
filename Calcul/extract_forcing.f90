

PROGRAM PLOT_VAR
!----------------------------------------------------------------------
!Adrien Napoly 10/12/2015
!----------------------------------------------------------------------
IMPLICIT NONE
 CHARACTER*100              :: CREPOUT='TXT/'   ! repertoire de sortie
 CHARACTER*1000             :: fichier,FORCAGE,POINT
 INTEGER                    :: J
 REAL,DIMENSION(8760)       :: Z
 REAL,DIMENSION(8760)       :: Y


 ! A modifier
 POINT = '1'
 
 READ *, POINT


 !Pas touche à partir d'ici

 fichier='FORCAGE/Forc_LW.bin_france_2013_2014'
 OPEN(UNIT=10,FILE=fichier,STATUS='OLD',FORM='UNFORMATTED', ACCESS='DIRECT'&
	,CONVERT='BIG_ENDIAN',RECL=9892*4)


 DO J=1,8760
  READ (10,REC=J)Z(J)
 ENDDO

 CLOSE(UNIT=10)
 
 fichier='FORCAGE/Forc_SW.bin_france_2013_2014'
 OPEN(UNIT=20,FILE=fichier,STATUS='OLD',FORM='UNFORMATTED', ACCESS='DIRECT'&
	,CONVERT='BIG_ENDIAN',RECL=9892*4)


 DO J=1,8760
  READ (20,REC=J)Y(J)
 ENDDO

 CLOSE(UNIT=20)

 OPEN(UNIT=11,FILE='irradiance_totale_point_'//trim(POINT)//'.txt')
 DO J=1,8760
 WRITE(11,*)Z(J)+Y(J)
 ENDDO
 CLOSE(UNIT=11)



END PROGRAM PLOT_VAR


