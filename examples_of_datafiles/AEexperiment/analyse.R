d = data.frame()
for (f in Sys.glob('*.dat'))
    {
        d = rbind(d, read.table(f, header=T))
    }
