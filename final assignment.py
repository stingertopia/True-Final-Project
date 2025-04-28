from breezypythongui import EasyFrame

class FinalDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.label = self.addLabel(text="Enter the Code of the product or part", row=0, column=1, columnspan=2, sticky="NSEW")
        self.inputField = self.addTextField(text="", row=2, column=1)



        self.YesButton= self.addButton(text="Yes", row=1, column=1)

        self.NoButton = self.addButton(text="No", row=1, column=2)
        if NoButton_clicked:
            self.label = self.addLabel(text="Enter the Code of the product or part", row=0, column=1, columnspan=2, sticky="NSEW")
            self.inputField = self.addTextField(text="", row=2, column=1)


def part(
    Square = 1,
    LongMetal = 2,
    ShortMetal = 3,
    Arm = 4,
    BaggedScrews = 10,
    Circle = 11):

def product(
WindowWipers = A,
Clamps = B):



def main():
    FinalDemo().mainloop()

if __name__ == "__main__":
    main()
