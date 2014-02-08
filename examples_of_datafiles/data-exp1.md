Analyse de Data-Experiment1
===========================



```r
exp1 <- read.csv("Data-Experiment1.csv")
str(exp1)
```

```
## 'data.frame':	3200 obs. of  6 variables:
##  $ X      : int  1 2 3 4 5 6 7 8 9 10 ...
##  $ Trial  : int  1 2 3 4 5 6 7 8 9 10 ...
##  $ Cond   : Factor w/ 2 levels "condA","condB": 1 1 1 1 1 1 1 1 1 1 ...
##  $ Subject: Factor w/ 32 levels "s1","s10","s11",..: 1 1 1 1 1 1 1 1 1 1 ...
##  $ Hit    : int  1 1 1 0 1 1 1 1 1 1 ...
##  $ RT     : num  1123 1254 1102 1029 1141 ...
```


On compte le nombre de sujets, le nombre de données par sujet, on cherche la relation entre sujet et condition..


```r
nlevels(exp1$Subject)
```

```
## [1] 32
```

```r
table(exp1$Subject)
```

```
## 
##  s1 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19  s2 s20 s21 s22 s23 s24 s25 
## 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 
## s26 s27 s28 s29  s3 s30 s31 s32  s4  s5  s6  s7  s8  s9 
## 100 100 100 100 100 100 100 100 100 100 100 100 100 100
```

```r
table(exp1$Subject, exp1$Cond)
```

```
##      
##       condA condB
##   s1     50    50
##   s10    50    50
##   s11    50    50
##   s12    50    50
##   s13    50    50
##   s14    50    50
##   s15    50    50
##   s16    50    50
##   s17    50    50
##   s18    50    50
##   s19    50    50
##   s2     50    50
##   s20    50    50
##   s21    50    50
##   s22    50    50
##   s23    50    50
##   s24    50    50
##   s25    50    50
##   s26    50    50
##   s27    50    50
##   s28    50    50
##   s29    50    50
##   s3     50    50
##   s30    50    50
##   s31    50    50
##   s32    50    50
##   s4     50    50
##   s5     50    50
##   s6     50    50
##   s7     50    50
##   s8     50    50
##   s9     50    50
```



On cherche les pourcentages de réponses correctes par sujet


```r
mean(exp1$Hit)
```

```
## [1] 0.8962
```

```r
hist(with(exp1, tapply(Hit, Subject, mean)), nclass = 10)
```

![plot of chunk unnamed-chunk-3](figure/unnamed-chunk-3.png) 



On inspecte les temps de réaction


```r
hist(exp1$RT[exp1$Hit == 1], nclass = 25)
rug(exp1$RT[exp1$Hit == 1])
```

![plot of chunk unnamed-chunk-4](figure/unnamed-chunk-4.png) 



```r
exp1clean <- subset(exp1, Hit == 1)
nrow(exp1clean)
```

```
## [1] 2868
```



On calcule, pour chaque sujet, le temps de réaction moyen sur les essais corrects



```r
sumdata <- with(exp1clean, aggregate(RT, list(Subject = Subject, Cond = Cond), 
    mean))
```



On regarde l'effet de Cond. 


```r
with(sumdata, tapply(x, Cond, mean))
```

```
## condA condB 
## 481.6 499.9
```

```r

with(sumdata, summary(aov(x ~ Cond + Error(Subject/Cond))))
```

```
## 
## Error: Subject
##           Df Sum Sq Mean Sq F value Pr(>F)
## Residuals 31   9693     313               
## 
## Error: Subject:Cond
##           Df Sum Sq Mean Sq F value Pr(>F)  
## Cond       1   5336    5336    6.24  0.018 *
## Residuals 31  26521     856                 
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

```r
with(sumdata, t.test(x ~ Cond, paired = T))
```

```
## 
## 	Paired t-test
## 
## data:  x by Cond
## t = -2.498, df = 31, p-value = 0.01802
## alternative hypothesis: true difference in means is not equal to 0
## 95 percent confidence interval:
##  -33.176  -3.349
## sample estimates:
## mean of the differences 
##                  -18.26
```






