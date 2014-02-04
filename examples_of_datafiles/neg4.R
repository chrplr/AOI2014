d<-read.table('neglige4.txt')
x<-d$V1
a<-gl(2,12,24)
b<-gl(2,6,24)
table(a,b)
tapply(x,list(a=a,b=b),mean)
interaction.plot(a,b,x)
l<-aov(x~a*b)
summary(l)
model.tables(l,se=T)
t.test(x[a==1 & b==1],x[a==1 & b==2])
t.test(x[a==2 & b==1],x[a==2 & b==2])

