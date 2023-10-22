%aushnayee ba dade
%import data
%1
histogram(Classes);
histogram(Data);
%2 alef
mean(Data);
X_mc=Data-mean(Data);
%2 be
X_t_mc = transpose(X_mc);
S=X_t_mc * X_mc;
%2 jym
S_EIG = eig(S);
%3
n=[];
for i=1:length(Classes)
    for j=3
        if Classes(i)==1
        n(i,1)=1;
        elseif Classes(i)==2
        n(i,2)=1;
        elseif Classes(i)==3
        n(i,3)=1;
        else
            n(i,j)=0;
        end
    end
end
  


%pca
%1 ghesmat 59 darsad monde

[coeff,score,latent,tsquared,explained] = pca(Data);

explained
%2
y=score(:,1);
z=score(:,2);
c = linspace(1,10,length(y));
scatter(y,z,[],c), grid on
ylabel('pc1'), zlabel('pc2')
%3
X_AUOTO_SCALE=X_mc/(max(X_mc)-min(X_mc));

[coeff,score,latent,tsquared,explained] = pca(X_AUOTO_SCALE);

explained
