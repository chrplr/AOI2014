rm(list=ls()) # nettoie le workspace

# dossier négligence
negl<-read.table('neglige2.txt',header=T)
negl
attach(negl)
stripchart(score~groupe,method='jitter')
tapply(score,groupe,summary)
t.test(score~groupe)
t.test(score~groupe,var.equal=T)
wilcox.test(score~groupe)
detach()

# dossier sommeil
sommeil<-read.table('sommeil1.txt',header=T)
sommeil
attach(sommeil)
summary(M1)
summary(M2)

plot(M1,M2,xlim=c(0,10),ylim=c(0,10),col=2)
identify(M1,M2,SOMMEIL)
abline(0,1)

stripchart(M2-M1,method='stack')
t.test(M2-M1)

t.test(M1,M2,paired=T)
detach()

# dossier family
fam<-read.table('family.txt',header=T)
fam
attach(fam)
data<-as.matrix(fam[,-1])
pairs(data,panel=panel.smooth)
cor(data)
cor.test(FATH,GIRL)
cor.test(MOTH,GIRL)
cor.test(INST,GIRL)

l<-lm(GIRL ~ FATH + MOTH + INST)
summary(l)
detach(fam)


with(fam,{
  data<-as.matrix(fam[,-1])
  pairs(data,panel=panel.smooth)
  cor(data)
  cor.test(FATH,GIRL)
  cor.test(MOTH,GIRL)
  cor.test(INST,GIRL)

  l<-lm(GIRL ~ FATH + MOTH + INST)
  summary(l)
  }
)
