
function script5
%SCRIPT5   Complete the exercise only using the core MATLAB programming language
%and the following functions as needed: load, rng, size, zeros, randsample,
%randperm figure, imagesc, title, xlabel, ylabel, print, trace, fitctree,
%predict,view
   

A = load('leaf.mat');
idx = randperm(340);
c = A.c;
x = A.x;
% current pointer
c = c(idx,1);
% next pointer
x = x(idx,:);

% 340 fold
m = 340/340;
a = zeros(30);
for i = 1:340
    i0 = (i-1)*m+1;
    i1 = i*m;
 
    c1 = [c(1:i0-1,:); c(i1+1:end,:)];
    x1 = [x(1:i0-1,:); x(i1+1:end,:)];
 
    x2 = x(i0:i1,:);
    c2 = c(i0:i1,:);
 
    M = fitctree(x1,c1);
    c2_hat = predict(M,x2);
 
    for k = 1:m
        a(c2_hat(k),c2(k)) = a(c2_hat(k),c2(k)) + 1;
    end 
end
 
acc340 = trace(a)/340
figure
imagesc(a)


%2 fold
m = 340/2;
a = zeros(30);
for i = 1:2
    i0 = (i-1)*m+1;
    i1 = i*m;
 
    c1 = [c(1:i0-1,:); c(i1+1:end,:)];
    x1 = [x(1:i0-1,:); x(i1+1:end,:)];
 
    x2 = x(i0:i1,:);
    c2 = c(i0:i1,:);
 
    M = fitctree(x1,c1);
    
    c2_hat = predict(M,x2);
 
    for k = 1:m
        a(c2_hat(k),c2(k)) = a(c2_hat(k),c2(k)) + 1;
    end 
end
 
acc2 = trace(a)/340
figure
imagesc(a)

%17 fold
m = 340/17;
a = zeros(30);
for i = 1:17
    i0 = (i-1)*m+1;
    i1 = i*m;
 
    c1 = [c(1:i0-1,:); c(i1+1:end,:)];
    x1 = [x(1:i0-1,:); x(i1+1:end,:)];
 
    x2 = x(i0:i1,:);
    c2 = c(i0:i1,:);
 
    M = fitctree(x1,c1);
    c2_hat = predict(M,x2);
 
    for k = 1:m
        a(c2_hat(k),c2(k)) = a(c2_hat(k),c2(k)) + 1;
    end 
end
 
acc17 = trace(a)/340
figure
imagesc(a)

M = fitctree(x,c);
view(M,'Mode','graph')
return

end
