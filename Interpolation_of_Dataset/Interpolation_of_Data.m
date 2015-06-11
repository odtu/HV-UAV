
 clear all; close all; clc;
 x = [1 3 5 7 9 11 13 15 17 19 21 23 25 27 29];
 y=  [5 9 13 17];
 Z = [10 18 34 48 48 45 42 46 47 48 52 50 30 16 8
    17 20 31 33 40 38 34 32 32 36 46 40 31 20 16
    16 16 23 26 24 22 29 26 31 36 33 32 28 20 13
    14 14 23 24 23 20 23 22 24 28 26 27 22 20 15];

[X, Y] = meshgrid(x, y);

xi = linspace(1, 29, 100);
yi = linspace(5, 17, 100 * (12/28)); %keep the aspect ratio
[XI, YI] = meshgrid(xi, yi);

ZI1 = interp2(X,Y,Z,XI,YI)
figure
surf(XI,YI,ZI1);
title('Linear Interpolation of Data');
xlabel('Position') % x-axis label
ylabel('Height') % y-axis label

ZI2 = interp2(X,Y,Z,XI,YI,'spline')
figure
surf(XI,YI,ZI2);
title('Spline Interpolation of Data');
xlabel('Position') % x-axis label
ylabel('Height') % y-axis label


% spline Matrix to txt
fid = fopen('Mymatrix.txt','wt');
for ii = 1:size(ZI2,1)
    fprintf(fid,'%g\t',ZI2(ii,:));
    fprintf(fid,'\n');
end
fclose(fid)