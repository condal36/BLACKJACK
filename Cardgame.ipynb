{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "suits=('Hearts','Diamonds','Spades','Clubs')\n",
    "ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')\n",
    "values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}\n",
    "\n",
    "playing=True\n",
    "#遊戲中?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Card():\n",
    "    \n",
    "    def __init__(self,suit,rank):\n",
    "        self.suit=suit\n",
    "        self.rank=rank\n",
    "        \n",
    "    def __str__(self):\n",
    "        return self.rank+\" of \"+self.suit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Deck:\n",
    "    def __init__(self):\n",
    "        self.deck=[]\n",
    "        for suit in suits:\n",
    "            for rank in ranks:\n",
    "                self.deck.append(Card(suit,rank))\n",
    "    \n",
    "    def __str__(self):\n",
    "        deck_comp=''\n",
    "        for card in self.deck:\n",
    "            deck_comp+=\"\\n\"+card.__str__()\n",
    "        return \"The deck has: \"+deck_comp\n",
    "    \n",
    "    def shuffle(self):\n",
    "        random.shuffle(self.deck)\n",
    "        \n",
    "    def deal(self):\n",
    "        single_card = self.deck.pop()\n",
    "        return single_card"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The deck has: \n",
      "Seven of Diamonds\n",
      "Jack of Spades\n",
      "Three of Hearts\n",
      "King of Hearts\n",
      "Ten of Diamonds\n",
      "Four of Hearts\n",
      "Seven of Hearts\n",
      "Jack of Diamonds\n",
      "Eight of Clubs\n",
      "Six of Spades\n",
      "Eight of Spades\n",
      "Queen of Hearts\n",
      "Three of Spades\n",
      "Four of Spades\n",
      "Ten of Spades\n",
      "Six of Diamonds\n",
      "Two of Spades\n",
      "Ace of Spades\n",
      "Jack of Hearts\n",
      "Ten of Clubs\n",
      "Four of Clubs\n",
      "Queen of Clubs\n",
      "Six of Hearts\n",
      "Eight of Hearts\n",
      "Eight of Diamonds\n",
      "Two of Clubs\n",
      "Three of Diamonds\n",
      "Five of Spades\n",
      "Nine of Diamonds\n",
      "Ace of Clubs\n",
      "King of Diamonds\n",
      "Ace of Hearts\n",
      "Four of Diamonds\n",
      "Nine of Hearts\n",
      "King of Spades\n",
      "Three of Clubs\n",
      "Five of Diamonds\n",
      "Ten of Hearts\n",
      "Two of Diamonds\n",
      "Nine of Spades\n",
      "Two of Hearts\n",
      "Five of Clubs\n",
      "Five of Hearts\n",
      "Nine of Clubs\n",
      "Ace of Diamonds\n",
      "Seven of Clubs\n",
      "Queen of Diamonds\n",
      "Queen of Spades\n",
      "Seven of Spades\n",
      "Six of Clubs\n",
      "Jack of Clubs\n",
      "King of Clubs\n",
      "---------------------\n",
      "King of Clubs\n"
     ]
    }
   ],
   "source": [
    "test_deck=Deck()\n",
    "test_deck.shuffle()\n",
    "print(test_deck)\n",
    "print(\"---------------------\")\n",
    "print(test_deck.deal())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Hand:\n",
    "    def __init__(self):\n",
    "        self.cards=[] #start with an empty list as we did the Deck class\n",
    "        self.value=0 #start with zero value\n",
    "        self.aces=0 #add an attribute to keep track of aces\n",
    "        \n",
    "    def add_card(self,card):\n",
    "        #card passed in form deck.deal()->single Card(suit,rank)\n",
    "        self.cards.append(card)\n",
    "        self.value+=values[card.rank]\n",
    "        \n",
    "        #track aces\n",
    "        if card.rank=='Ace':\n",
    "            self.aces+=1\n",
    "        \n",
    "        \n",
    "        \n",
    "    def adjust_for_ace(self):\n",
    "        #if total value>21 and still have an ace than change my ace to be a 1 instead of a 11#\n",
    "        while self.value>21 and self.aces:\n",
    "            self.value-=10\n",
    "            self.aces-=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ace of Diamonds\n",
      "11\n"
     ]
    }
   ],
   "source": [
    "test_deck = Deck()\n",
    "test_deck.shuffle()\n",
    "\n",
    "#Player\n",
    "test_player=Hand()\n",
    "pulled_card=test_deck.deal()\n",
    "print(pulled_card)\n",
    "test_player.add_card(pulled_card)\n",
    "print(test_player.value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Three of Clubs\n",
      "14\n"
     ]
    }
   ],
   "source": [
    "pulled_card=test_deck.deal()\n",
    "print(pulled_card)\n",
    "test_player.add_card(pulled_card)\n",
    "print(test_player.value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Six of Diamonds\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "pulled_card=test_deck.deal()\n",
    "print(pulled_card)\n",
    "test_player.add_card(pulled_card)\n",
    "print(test_player.value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Chips:\n",
    "    \n",
    "    def __init__(self,total=100):\n",
    "        self.total=total #this can set to a default value or supplied by a user input\n",
    "        self.bet=0\n",
    "        \n",
    "    def win_bet(self):\n",
    "        self.total+=self.bet\n",
    "        \n",
    "    def lose_bet(self):\n",
    "        self.total-=self.bet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def take_bet(chips):\n",
    "    \n",
    "    while True:\n",
    "        try:\n",
    "            chips.bet=int(input(\"How many chips would yuou like to bet?\"))\n",
    "        except:\n",
    "            print(\"Sorry please provide an integer\")\n",
    "        else:\n",
    "            if chips.bet>chips.total:\n",
    "                print(\"Sorry, your bet doesn't enough! You have :{} \".format(chips.total))\n",
    "            else:\n",
    "                break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "def hit(deck,hand):\n",
    "    \n",
    "    single_card=deck.deal()\n",
    "    hand.add_card(single_card)\n",
    "    hand.adjust_for_ace()\n",
    "def show_some(player,dealer):\n",
    "    print(\"\\nDealer's Hand:\")\n",
    "    print(\" <card hidden>\")\n",
    "    print('',dealer.cards[1])  \n",
    "    print(\"\\nPlayer's Hand:\", *player.cards, sep='\\n ')\n",
    "    \n",
    "def show_all(player,dealer):\n",
    "    print(\"\\nDealer's Hand:\", *dealer.cards, sep='\\n ')\n",
    "    print(\"Dealer's Hand =\",dealer.value)\n",
    "    print(\"\\nPlayer's Hand:\", *player.cards, sep='\\n ')\n",
    "    print(\"Player's Hand =\",player.value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "def hit_or_stand(deck,hand):\n",
    "    global playing\n",
    "    \n",
    "    while True:\n",
    "        x=input('Hit or Stand? Enter H or S')\n",
    "        \n",
    "        if x[0].lower()=='h':\n",
    "            hit(deck,hand)\n",
    "        elif x[0].lower()=='s':\n",
    "            print(\"player stands up dealer's turn\")\n",
    "            playing=False\n",
    "        else:\n",
    "            print(\"Please enter h or s only\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "def player_busts(player,dealer,chips):\n",
    "    print(\"BUST PLAYER!\")\n",
    "    chips.lose_bet()\n",
    "def player_wins(player,dealer,chips):\n",
    "    print(\"PLAYER WINS!\")\n",
    "    chips.win_bet()\n",
    "def dealer_busts(player,dealer,chips):\n",
    "    print(\"PLAYER WINS!DEALER BUSTED\")\n",
    "    chips.win_bet()\n",
    "    \n",
    "def dealer_wins(player,dealer,chips):\n",
    "    print(\"DEALEL WINS!\")\n",
    "    chips.lose_bet()\n",
    "def push(player,dealer):\n",
    "    print(\"Dealer and player tie!PUSH\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to BJ\n",
      "How many chips would yuou like to bet?100\n",
      "\n",
      "Dealer's Hand:\n",
      " <card hidden>\n",
      " Queen of Clubs\n",
      "\n",
      "Player's Hand:\n",
      " Three of Hearts\n",
      " Seven of Clubs\n",
      "Hit or Stand? Enter H or SH\n",
      "Hit or Stand? Enter H or SH\n",
      "Hit or Stand? Enter H or SH\n",
      "Hit or Stand? Enter H or SS\n",
      "player stands up dealer's turn\n",
      "Hit or Stand? Enter H or SS\n",
      "player stands up dealer's turn\n",
      "Hit or Stand? Enter H or SS\n",
      "player stands up dealer's turn\n",
      "Hit or Stand? Enter H or SS\n",
      "player stands up dealer's turn\n",
      "Hit or Stand? Enter H or SS\n",
      "player stands up dealer's turn\n",
      "Hit or Stand? Enter H or SS\n",
      "player stands up dealer's turn\n",
      "Hit or Stand? Enter H or SS\n",
      "player stands up dealer's turn\n",
      "Hit or Stand? Enter H or SS\n",
      "player stands up dealer's turn\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    print(\"Welcome to BJ\")\n",
    "    deck=Deck()\n",
    "    deck.shuffle()\n",
    "    \n",
    "    player_hand=Hand()\n",
    "    player_hand.add_card(deck.deal())\n",
    "    player_hand.add_card(deck.deal())\n",
    "    \n",
    "    dealer_hand=Hand()\n",
    "    dealer_hand.add_card(deck.deal())\n",
    "    dealer_hand.add_card(deck.deal())\n",
    "    \n",
    "    player_chips=Chips()\n",
    "    \n",
    "    take_bet(player_chips)\n",
    "    show_some(player_hand,dealer_hand)\n",
    "    \n",
    "    while playing:\n",
    "        hit_or_stand(deck,player_hand)\n",
    "        show_some(player_hand,dealer_hand)\n",
    "        if player_hand.value>21:\n",
    "            player_busts(player_hand,dealer_hand,player_chips)\n",
    "            \n",
    "            break\n",
    "            \n",
    "            \n",
    "    if player_hand.value<21:\n",
    "        while dealer_hand.value<17:\n",
    "            hit(deck,dealer_hand)\n",
    "        show_all(player_hand,dealer_hand)\n",
    "        if dealer_hand.value>21:\n",
    "            dealer_busts(player_hand,dealer_hand,player_chips)\n",
    "        elif dealer_hand.value>player_hand.value:\n",
    "            dealer_wins(player_hand,dealer_hand,player_chips)\n",
    "        elif dealer_hand.value<player_hand.value:\n",
    "            player_wins(player_hand,dealer_hand,player_chips)\n",
    "        else:\n",
    "            push(player_hand,dealer_hand)\n",
    "            \n",
    "            \n",
    "    print('\\n Player total chips are at : {}'.format(player_chips.total))\n",
    "    new_game=input(\"Would you like to play another hand? y/n\")\n",
    "    if new_game[0].lower()=='y':\n",
    "        playing=True\n",
    "        continue\n",
    "    else:\n",
    "        print(\"Thank you for playing!\")\n",
    "        break\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
