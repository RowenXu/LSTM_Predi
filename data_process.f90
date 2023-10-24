!--------------Data_source--------------
!SST of Nino34:coming from ERA5 monthly 
!height in 500hPa:coming from ERA5 monthly
!REFERENCE
!Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J., Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D., Thépaut, J-N. (2023): ERA5 monthly averaged data on pressure levels from 1940 to present. Copernicus Climate Change Service (C3S) Climate Data Store (CDS), DOI: 10.24381/cds.6860a573 (Accessed on DD-MMM-YYYY)
program data_process

USE netcdf

implcit none
!variable DEFINITION
integer,parameter::yy=40,mm=12 !Time of the data
real sst_initial(yy,mm),height_initial(yy,mm),uwind_inition(yy,mm),vwind_inition(yy,mm) !ORIGINAL DATA IMPORTED 
integer i,j,k !recycing variable
end program data_process