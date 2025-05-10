from breezypythongui import EasyFrame
from tkinter import PhotoImage

#FinalDemo class
class FinalDemo(EasyFrame):
    #frame setup
    def __init__(self):
        EasyFrame.__init__(self, title = "factory code")
        self.setResizable(True)
        self.setSize(750,500)


        #initial prompt
        self.label = self.addLabel(text="Enter the Code of the product or part", row=0, column=1, columnspan=2, sticky="NSEW")
        self.inputField = self.addTextField(text="", row=2, column=1)
        #to promt the initial answer from the user

        #initital question
        imageLabel_1 = self.addLabel(text="is this the part or product",row=0, column=1, sticky="NSEW")
        self.image_1 = PhotoImage(file = r"C:\Users\sting\OneDrive\Pictures\longmetal.png")
        imageLabel_1["longmetal"] = self.image_2
        imageLabel_2 = self.addLabel(text="is this the part or product",row=0, column=1, sticky="NSEW")
        self.image_2 = PhotoImage(file = r"shortmetal.png")
        imageLabel_2["shortmetal"] = self.image_2
        #to show the images to the user

        #buttons
        self.YesButton= self.addButton(text="Yes", row=1, column=1, command= open)
        self.NoButton = self.addButton(text="No", row=1, column=2, command=self.__init__)
        self.ExitButton = self.addButton(Factory, text="exit", row=1, column=3, command=Factory.destroy).pack()
        Factory.mainloop()
        #to have the user make a choice off the given options


        #class for images
        class Images(self):
            EasyFrame.__init__(self, imageLabel_1, imageLabel_2)
            from sting import Image
            try:
                imageLabel_1 = Image.open(r"C:\Users\sting\OneDrive\Pictures\longmetal.png")
            except IOError:
                print("a long thin metal piece")
                pass
            from sting import Image
            try:
                imageLabel_2 = Image.open(r"shortmatel.png")
            except IOError:
                print("a long thin metal piece")
                pass
        #to make the images work

    # Parts introduction
    def part():
        Square = 1, 
        LongMetal = 2,
        ShortMetal = 3, 
        Arm = 4,
        BaggedScrews = 10, 
        Circle = 11
                
    # product introduction
    def product():
        WindowWipers = A, 
        Clamps = B
def main():
    FinalDemo().mainloop()

if __name__ == "__main__":
    main()