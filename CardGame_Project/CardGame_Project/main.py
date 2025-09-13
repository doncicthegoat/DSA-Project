import pygame
from sys import exit
import random
from sorting_functions import merge_sort, heap_sort, binary_insertion_sort, quick_sort
from detecting_functions import detect_royal_flush, detect_flush, detect_four_of_a_kind, detect_straight_flush, \
    detect_straight, detect_three_of_a_kind, detect_full_house, detect_two_pair, detect_one_pair

pygame.init()
info = pygame.display.Info()

width=info.current_w - 200
height = info.current_h - 100


a=width/1720
b=height/980


"""Classes construction"""

class SpriteSheet:                  #Thanks to Eric Matthes

    def __init__(self, filename):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)


    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA)  # Transparent surface
        image.blit(self.sheet, (0, 0), rect)
        return image


class Button:
    def __init__(self, x, y, width, height, text, font, text_color=(255, 255, 255),image=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.text_color = text_color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = image


    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()


        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def draw_image(self,surface):

        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        surface.blit(self.image, self.rect)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)



    def is_clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )


counter = {
    "Royal Flush": 0,
    "Straight Flush": 0,
    "Four of a Kind": 0,
    "Full House": 0,
    "Flush": 0,
    "Straight": 0,
    "Three of a Kind": 0,
    "Two Pair": 0,
    "One Pair": 0,
    "No Hand" : 0
}

class Card:
    values = {14: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack",
              12: "Queen", 13: "King"}
    def __init__(self,value,suit,size= a*2):
        self.suit = suit
        self.value = value
        self.height = 50*size
        self.width = 34*size
        self.image = sprite_dict[self.suit].image_at(values_cord[self.value])
        self.image = pygame.transform.scale(self.image, (self.width, self.height))


    def __str__(self):


        return f"{self.values[self.value]} of {self.suit}"

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.value <= other

    def __gt__(self, other):
        return self.value > other

    def __ge__(self, other):
        return self.value >= other

    def show(self,dest):
        screen.blit(self.image,dest)



class Hand:
    def __init__(self,cards):
        self.cards = cards
        self.poker_hands = []

    def print_poker_hands(self):

        return f"{[str(hand[0]) + hand[1] for hand in self.poker_hands]}"


    def detect_poker_hands(self):
        detected = True
        while detected:

            if detect_royal_flush(self.cards):
                temp = detect_royal_flush(self.cards)
                self.poker_hands.append((Hand(temp), "Royal Flush"))
                self.update_hand(temp)
                counter["Royal Flush"] += 1

            elif detect_straight_flush(self.cards):
                temp = detect_straight_flush(self.cards)
                self.poker_hands.append((Hand(temp), "Straight Flush"))
                self.update_hand(temp)
                counter["Straight Flush"] += 1

            elif detect_four_of_a_kind(self.cards):
                temp = detect_four_of_a_kind(self.cards)
                self.poker_hands.append((Hand(temp), "Four of a Kind"))
                self.update_hand(temp)
                counter["Four of a Kind"] += 1

            elif detect_full_house(self.cards):
                temp = detect_full_house(self.cards)
                self.poker_hands.append((Hand(temp), "Full House"))
                self.update_hand(temp)
                counter["Full House"] += 1

            elif detect_flush(self.cards):
                temp = detect_flush(self.cards)
                self.poker_hands.append((Hand(temp), "Flush"))
                self.update_hand(temp)
                counter["Flush"] += 1

            elif detect_straight(self.cards):
                temp = detect_straight(self.cards)
                self.poker_hands.append((Hand(temp), "Straight"))
                self.update_hand(temp)
                counter["Straight"] += 1

            elif detect_three_of_a_kind(self.cards):
                temp = detect_three_of_a_kind(self.cards)
                self.poker_hands.append((Hand(temp), "Three of a Kind"))
                self.update_hand(temp)
                counter["Three of a Kind"] += 1

            elif detect_two_pair(self.cards):
                temp = detect_two_pair(self.cards)
                self.poker_hands.append((Hand(temp), "Two Pair"))
                self.update_hand(temp)
                counter["Two Pair"] += 1

            elif detect_one_pair(self.cards):
                temp = detect_one_pair(self.cards)
                self.poker_hands.append((Hand(temp), "One Pair"))
                self.update_hand(temp)
                counter["One Pair"] += 1

            elif len(self.poker_hands) == 0:
                self.poker_hands.append((Hand([]), "There are no poker hands"))
                counter["No Hand"] += 1
                detected = False

            elif detected:
                detected = False


    def merge_sort(self):
        self.cards = merge_sort(self.cards)

    def binary_insertion_sort(self):
        self.cards = binary_insertion_sort(self.cards)

    def heap_sort(self):
        self.cards = heap_sort(self.cards)

    def quick_sort(self):
        self.cards = quick_sort(self.cards)

    def update_hand(self, lst):
        new_cards = []
        for card in self.cards:
            if all((card.value,card.suit) != (card1.value,card1.suit) for card1 in lst):
                new_cards.append(card)
        self.cards = new_cards

    def __str__(self):
        return f"{[str(card) for card in self.cards]}"

    def show_hand(self,dest):
        images = [card.image for card in self.cards]
        for i in range(len(images)):
            screen.blit(images[i], (dest[0]+70*i,dest[1]))


class Deck:
    def __init__(self):
        self.deck = [Card(value,f"{suit}" ) for suit in ["Hearts","Clubs","Diamonds","Spades"] for value in range(2,15)]
        self.image = SpriteSheet("Card_Machine.png").image_at((0,40,80,70))
        self.image = pygame.transform.scale(self.image, (160, 128))

    def __str__(self):
        return f"{[str(card) for card in self.deck]}"

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self,n):
        hand = Hand(self.deck[:n])
        return hand


"""Game Initialization"""


screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Card Game")
clock = pygame.time.Clock()

table = pygame.image.load('Poker_Table.png').convert()
table = pygame.transform.scale(table,(width,height))
sprite_dict = {"Diamonds":SpriteSheet("Diamonds.png"),"Clubs":SpriteSheet("Clubs.png"),"Spades":SpriteSheet("Spades.png"),"Hearts":SpriteSheet("Hearts.png")}
values_cord = {14 :(7,7,34,50),13:(55, 7, 34, 50),12:(103, 7, 34, 50),11:(151, 7, 34, 50),10:(199, 135, 34, 50),9:(151, 135, 34, 50),8:(103, 135, 34, 50),7:(55, 135, 34, 50),6:(7, 135, 34, 50),5:(151, 71, 34, 50),4:(103, 71, 34, 50),3:(55, 71, 34, 50),2:(7, 71, 34, 50)}


deck = Deck()           #deck initialization
deck.shuffle()


n_cards = 3
alg = 0
temp=Hand([])
hand = Hand([])


font = pygame.font.Font("Montserrat-Bold.ttf", int(a*36)  )
buttons = SpriteSheet("buttons.png")
dealer_sprite = SpriteSheet("Dealer.png")

dealer_clicked = False
game_state = "opening_menu"         #First game state
opening_screen = pygame.Surface((width,height))
opening_screen.fill((122,161,76))
green_button = buttons.image_at((102,80, 34,16))
dealer_image = dealer_sprite.image_at((80,5,40,44))
dealer_image = pygame.transform.scale(dealer_image,(120,132))
sorting_algs = ["Merge Sort","Heap Sort", "Binary Insertion Sort","Quick Sort"]

"""---------------Buttons---------------"""

more = Button((width-a*600),b*200,a*60,b*60,"+", font,(255, 255, 255),green_button)
less = Button(a*600 ,b*200,a*60,b*60,"-", font,(255, 255, 255),green_button)
n_cards_button = Button(width//2, b*200 , a*60 ,b*60,f"{n_cards}", font,(255,255,255))


sorting_algs_button = Button((width//2-(a*300)//2) ,(height-b*300),a*300,b*60,sorting_algs[0], font,(255,255,255))
next_button = Button((width - a*500) ,(height-b*300),a*100,b*60,"next", font,(255, 255, 255),green_button)
previous_button = Button((a*500-b*60),(height-b*300),a*200,b*60,"previous", font,(255, 255, 255),green_button)

card_machine  = Button(width//2,height//2, a*160,b*128,"",font,(255, 255, 255),deck.image)

start_button = Button((width-200)//2, (height-60)//2, a*200, b*60, "START", font,(255, 255, 255),green_button)

dealer = Button(width-(a*160), height-(b*172), a*120, b*132, "", font,(255, 255, 255),dealer_image)

"""--------Different game states--------"""

def opening_menu():
    global game_state
    screen.blit(opening_screen,(0,0))
    start_button.draw_image(screen)

    for event in events:
        if start_button.is_clicked(event):
            game_state = "cards_drawn"


def cards_drawn():
    global game_state
    global n_cards
    global alg
    global hand
    global temp
    less.draw_image(screen)
    more.draw_image(screen)
    n_cards_button.draw(screen)
    next_button.draw_image(screen)
    previous_button.draw_image(screen)
    sorting_algs_button.draw(screen)
    card_machine.draw_image(screen)


    for event in events:
        if less.is_clicked(event) and n_cards>3:
            n_cards -= 1
            n_cards_button.text=f"{n_cards}"
        elif more.is_clicked(event) and n_cards<15:
            n_cards += 1
            n_cards_button.text = f"{n_cards}"
        elif next_button.is_clicked(event) and alg<len(sorting_algs)-1:
            alg += 1
            sorting_algs_button.text =  f"{sorting_algs[alg]}"

        elif previous_button.is_clicked(event) and alg>0:
            alg -= 1
            sorting_algs_button.text =  f"{sorting_algs[alg]}"
        elif card_machine.is_clicked(event):
            game_state = "show_hand"
            hand = deck.draw(n_cards)


            if alg == 0:
                hand.merge_sort()
            elif alg == 1:
                hand.heap_sort()
            elif alg == 2:
                hand.binary_insertion_sort()
            elif alg == 3:
                hand.quick_sort()

            temp = Hand(hand.cards[:])
            hand.detect_poker_hands()

def show_hand():
    global game_state
    global dealer_clicked
    play_again = Button(dealer.x-a*230,dealer.y,a*250,b*60,"Play Again",font,(255,255,255),green_button)
    end_session = Button(dealer.x-a*230,dealer.y-b*70,a*250,b*60,"End Session",font,(255,255,255),green_button)
    temp.show_hand((a*100,b*100))
    for i in range(len(hand.poker_hands)):
        hand.poker_hands[i][0].show_hand((a*100,b*(205+105*i)))
        Button(a*(width-500), b*(205+105*i), a*200,b*60 ,f"{hand.poker_hands[i][1]}", font, (255, 255, 255)).draw(screen)
    dealer.draw_image(screen)

    for event in events:
        if dealer.is_clicked(event) and not dealer_clicked:
            dealer_clicked = True
        elif dealer.is_clicked(event) and dealer_clicked:
            dealer_clicked = False
        elif play_again.is_clicked(event):
            deck.shuffle()
            game_state = "cards_drawn"
        elif end_session.is_clicked(event):
            game_state = "final"

    if dealer_clicked:
        play_again.draw_image(screen)
        end_session.draw_image(screen)



def final():
    quit = Button(width//2-(b*60//2),height-(b*150),a*250,b*60,"Quit",font,(255,255,255),green_button)

    height_counter = b*100
    quit.draw_image(screen)
    for key in counter.keys():

        text = font.render(f"{key} : "+str(counter[key]), True, (255, 255, 255))
        text_rect = text.get_rect(topleft=(a*100, height_counter))
        screen.blit(text,text_rect)
        height_counter +=b*70

    for event in events:
        if quit.is_clicked(event):
            pygame.quit()
            exit()



"""Game loop"""

if __name__ == "__main__":   #Driver code
    running = True
    while running:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        screen.blit(table,(0,0))
        if game_state == "opening_menu":
            opening_menu()
        elif game_state == "cards_drawn":
            cards_drawn()
        elif game_state == "show_hand":
            show_hand()
        elif game_state == "final":
            final()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    exit()