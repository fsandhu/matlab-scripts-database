function readInput(inputFile)
fid99=fopen(inputFile, "r");
formatSpec="%d";
nums = fscanf(fid99, formatSpec, Inf)
i=1
x=[]
y=[]
z=[]
while(i < size(nums))
    x(i,1)=nums(i);
    y(i,1)=nums(i+1);
    z(i,1)=nums(i+2);
    i=i+3;
end
fclose(fid99);



