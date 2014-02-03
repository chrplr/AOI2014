(TeX-add-style-hook "tips_and_tricks_for_phd"
 (lambda ()
    (LaTeX-add-environments
     "bcases")
    (TeX-add-symbols
     "seti"
     "conti")
    (TeX-run-style-hooks
     "times"
     "graphicx"
     "skak"
     "verbatim"
     "amsmath"
     "qtree"
     "latex2e"
     "beamer10"
     "beamer")))

