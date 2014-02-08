alldata = data.frame()

for (f in Sys.glob('*.txt'))
     {
        print(sprintf("Processing %s...",f))
        print("")

        subj <- sub("(.*)_.*", "\\1", f)
        group <- sub(".*Successeur(.*)\\.txt", "\\1", f)
        data <- scan(f, what=character(), quiet=TRUE, sep='*')
        symb <- data[grepl("Symbol", data)]
        symb <- sub(".*(Symbole[89]).*", "\\1", symb)
        print(sprintf("subj=%s, group=%s, symb=%s", subj, group, symb))
        print("")
        
        responses <- data[grepl("(PasSur)|(Oui)|(Non)", data)]
        if (responses[1]=="NonSymb") { responses <- responses[-1] }
        cond <- data[grepl("(1by1)|(2by2)|(3by3)|(remove)", data)]

        if (length(responses)!=4) {
            print(sprintf("WARNING: %sdoes not have 4 responses, ignoring this file...",f))
        }
        else {
            alldata <- rbind(alldata, data.frame(subj=subj, group=group, symb=symb, cond=cond, resp=responses))
        }
        
     }

write.csv(alldata, "shadok_alldata.csv")

     
