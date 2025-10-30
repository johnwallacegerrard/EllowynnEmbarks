import character_classes
import weapons

class Ellowynn:
    def __init__(self):
        self.characterClass= None
        self.inventory= []
        self.health=100
        self.weapon = None

    def setClass(self, choice):
        self.characterClass = choice


    def attack(self, stat, weapon):
        stat = self.characterClass.str
        weapon = self.weapon
        hitPoints = stat * weapon.damage
        return hitPoints

print("The last thing your father, the King, said to you was meant to be comforting. It was not. When the castle was stormed and enemy forces began to overwhelm the Royal Gaurd, the King ordered his brother, the famous scholar Muu, to take you through the secret escape-way. He was charged with keeping you safe. You are afraid for your father, and for the kingdom. You have been on the move for the last two weeks and you are currently staying with a farmer in a small village in the countryside. Uncle Muu has heard only bad news from the capitol, and finally decides it is time to address the next course of action:")

player = Ellowynn()

print("")

print("'Ellowynn, I have not heard any news of your the father. We have to assume the worst. The evil priestess Moghedien now controls the kingdom. Since there has been no execution, or public announcement of the kings death, it is safe to assume he is being held captive. You have a choice to make Ellie. You can stay with me, and I can teach you the ways of mysticism. Learn to wield the powers of Delilah-Lee and join me to find a way to defeat Moghedien with magic. I can also deliver you to your other Uncle, General Ahlah. He was away on a diplomatic mission during the attack. You can continue your training with him, and fight Moghedien directly. Which will it be Princess?'")

print("")

classChoice = input("Uncle Muu (Sorceress) or Uncle Ahlah (Warrior)?")


if classChoice == "Uncle Ahlah":
    player.setClass(character_classes.Warrior())
    print("")
    print("The general should have recieved the news by now. I have been told he is gathering his forces, along with the lords of the Great Houses, at the port city of Wallace. You will be a very important figure for the resistance. The whole kingdom will look to you for leadership, and you will rally many fighters to our cause. Moghedien cannot be allowed to hold control of the Realm. You have been training to fight for most fo your life. I imagine Uncle Ahlah will continue that training. I pray to Delilah-Lee that Moghedien has kept your father alive, that she may have a purpose as yet known to us. It is safe to assume that the Kings trusted advisors have not been spared, though. The General has been separated from his great commanders. My brother is a great warrior, and an even better tactician. But he is often hot-headed, and acts impulsively. If we are to succeed in saving the Kingdom, you need to be the voice of reason to your Uncle Ahlah. We leave at first light.")
    print(vars(player.characterClass))
    


if classChoice == "Uncle Muu":
    player.setClass(character_classes.Sorceress())

print("")   

print("You awake before dawn. Uncle Muu has gathered some supplies and has prepared for departure. He explains that the road wil be dangerous, no doubt full of unseen threats. He offers you a choice of weapon:")
print("")

weaponChoice=input("Sword or Axe?")

if weaponChoice == "Sword":
    player.weapon = weapons.Sword
    print(vars(player))

if weaponChoice == "Axe":
    player.weapon = weapons.Axe
    print(vars(player))

print("Your uncle")

    












