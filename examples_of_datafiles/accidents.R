a<-read.table('accidents.dat',header=T,sep='\t')
attach(a)

table(Sexe,Travail,Accident)
ftable(Sexe,Travail,Accident)


table(Travail,Accident)
chisq.test(table(Travail,Accident))

table(Sexe,Accident)
chisq.test(table(Sexe,Accident))

