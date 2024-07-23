import ROOT as R

def plot():
    global f
    f = R.TF1("f1", "sin(x)/x", 0., 10.)
    f.Draw()
    f.SaveAs("plotsin.pdf")
plot()
