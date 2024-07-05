import pygame

#size=(150,220)
size=(117,170)
#loading
ace_s = pygame.image.load('cards/ace_spades.png')
ace_c = pygame.image.load('cards/ace_clubs.png')
ace_h = pygame.image.load('cards/ace_hearts.png')
ace_d = pygame.image.load('cards/ace_diamonds.png')

king_s=pygame.image.load('cards/king_of_spades.png')
king_c=pygame.image.load('cards/king_of_clubs.png')
king_h=pygame.image.load('cards/king_of_hearts.png')
king_d=pygame.image.load('cards/king_of_diamonds.png')

queen_s=pygame.image.load('cards/queen_of_spades.png')
queen_c=pygame.image.load('cards/queen_of_clubs.png')
queen_h=pygame.image.load('cards/queen_of_hearts.png')
queen_d=pygame.image.load('cards/queen_of_diamonds.png')

jack_s=pygame.image.load('cards/jack_of_spades.png')
jack_c=pygame.image.load('cards/jack_of_clubs.png')
jack_h=pygame.image.load('cards/jack_of_hearts.png')
jack_d=pygame.image.load('cards/jack_of_diamonds.png')

ten_s=pygame.image.load('cards/10_spades.png')
ten_c=pygame.image.load('cards/10_clubs.png')
ten_h=pygame.image.load('cards/10_hearts.png')
ten_d=pygame.image.load('cards/10_diamonds.png')

nine_s=pygame.image.load('cards/9_spades.png')
nine_c=pygame.image.load('cards/9_clubs.png')
nine_h=pygame.image.load('cards/9_hearts.png')
nine_d=pygame.image.load('cards/9_diamonds.png')

eight_s=pygame.image.load('cards/8_spades.png')
eight_c=pygame.image.load('cards/8_clubs.png')
eight_h=pygame.image.load('cards/8_hearts.png')
eight_d=pygame.image.load('cards/8_diamonds.png')

seven_s=pygame.image.load('cards/7_spades.png')
seven_c=pygame.image.load('cards/7_clubs.png')
seven_h=pygame.image.load('cards/7_hearts.png')
seven_d=pygame.image.load('cards/7_diamonds.png')

six_s=pygame.image.load('cards/6_spades.png')
six_c=pygame.image.load('cards/6_clubs.png')
six_h=pygame.image.load('cards/6_hearts.png')
six_d=pygame.image.load('cards/6_diamonds.png')

five_s=pygame.image.load('cards/5_spades.png')
five_c=pygame.image.load('cards/5_clubs.png')
five_h=pygame.image.load('cards/5_hearts.png')
five_d=pygame.image.load('cards/5_diamonds.png')

four_s=pygame.image.load('cards/4_spades.png')
four_c=pygame.image.load('cards/4_clubs.png')
four_h=pygame.image.load('cards/4_hearts.png')
four_d=pygame.image.load('cards/4_diamonds.png')

three_s=pygame.image.load('cards/3_spades.png')
three_c=pygame.image.load('cards/3_clubs.png')
three_h=pygame.image.load('cards/3_hearts.png')
three_d=pygame.image.load('cards/3_diamonds.png')

two_s=pygame.image.load('cards/2_spades.png')
two_c=pygame.image.load('cards/2_clubs.png')
two_h=pygame.image.load('cards/2_hearts.png')
two_d=pygame.image.load('cards/2_diamonds.png')

#scaling
sized_ace_s=pygame.transform.scale(ace_s,size)
sized_ace_c=pygame.transform.scale(ace_c,size)
sized_ace_h=pygame.transform.scale(ace_h,size)
sized_ace_d=pygame.transform.scale(ace_d,size)

sized_king_s=pygame.transform.scale(king_s,size)
sized_king_c=pygame.transform.scale(king_c,size)
sized_king_h=pygame.transform.scale(king_h,size)
sized_king_d=pygame.transform.scale(king_d,size)

sized_queen_s=pygame.transform.scale(queen_s,size)
sized_queen_c=pygame.transform.scale(queen_c,size)
sized_queen_h=pygame.transform.scale(queen_h,size)
sized_queen_d=pygame.transform.scale(queen_d,size)

sized_jack_s=pygame.transform.scale(jack_s,size)
sized_jack_c=pygame.transform.scale(jack_c,size)
sized_jack_h=pygame.transform.scale(jack_h,size)
sized_jack_d=pygame.transform.scale(jack_d,size)

sized_ten_s=pygame.transform.scale(jack_s,size)
sized_ten_c=pygame.transform.scale(jack_c,size)
sized_ten_h=pygame.transform.scale(jack_h,size)
sized_ten_d=pygame.transform.scale(jack_d,size)

sized_nine_s=pygame.transform.scale(nine_s,size)
sized_nine_c=pygame.transform.scale(nine_c,size)
sized_nine_h=pygame.transform.scale(nine_h,size)
sized_nine_d=pygame.transform.scale(nine_d,size)

sized_eight_s=pygame.transform.scale(eight_s,size)
sized_eight_c=pygame.transform.scale(eight_c,size)
sized_eight_h=pygame.transform.scale(eight_h,size)
sized_eight_d=pygame.transform.scale(eight_d,size)

sized_seven_s=pygame.transform.scale(seven_s,size)
sized_seven_c=pygame.transform.scale(seven_c,size)
sized_seven_h=pygame.transform.scale(seven_h,size)
sized_seven_d=pygame.transform.scale(seven_d,size)

sized_six_s=pygame.transform.scale(six_s,size)
sized_six_c=pygame.transform.scale(six_c,size)
sized_six_h=pygame.transform.scale(six_h,size)
sized_six_d=pygame.transform.scale(six_d,size)

sized_five_s=pygame.transform.scale(five_s,size)
sized_five_c=pygame.transform.scale(five_c,size)
sized_five_h=pygame.transform.scale(five_h,size)
sized_five_d=pygame.transform.scale(five_d,size)

sized_four_s=pygame.transform.scale(four_s,size)
sized_four_c=pygame.transform.scale(four_c,size)
sized_four_h=pygame.transform.scale(four_h,size)
sized_four_d=pygame.transform.scale(four_d,size)

sized_three_s=pygame.transform.scale(three_s,size)
sized_three_c=pygame.transform.scale(three_c,size)
sized_three_h=pygame.transform.scale(three_h,size)
sized_three_d=pygame.transform.scale(three_d,size)

sized_two_s=pygame.transform.scale(two_s,size)
sized_two_c=pygame.transform.scale(two_c,size)
sized_two_h=pygame.transform.scale(two_h,size)
sized_two_d=pygame.transform.scale(two_d,size)

#main deck
deck=[sized_ace_s,sized_ace_c,sized_ace_h,sized_ace_d,
      sized_king_s,sized_king_c,sized_king_h,sized_king_d,
      sized_queen_s,sized_queen_c,sized_queen_h,sized_queen_d,
      sized_jack_s,sized_jack_c,sized_jack_h,sized_jack_d,
      sized_ten_s,sized_ten_c,sized_ten_h,sized_ten_d,
      sized_nine_s,sized_nine_c,sized_nine_h,sized_nine_d,
      sized_eight_s,sized_eight_c,sized_eight_h,sized_eight_d,
      sized_seven_s,sized_seven_c,sized_seven_h,sized_seven_d,
      sized_six_s,sized_six_c,sized_six_h,sized_six_d,
      sized_five_s,sized_five_c,sized_five_h,sized_five_d,
      sized_four_s,sized_four_c,sized_four_h,sized_four_d,
      sized_three_s,sized_three_c,sized_three_h,sized_three_d,
      sized_two_s,sized_two_c,sized_two_h,sized_two_d
      ]

values={
    sized_ace_s:11,sized_ace_c:11,sized_ace_h:11,sized_ace_d:11,
    sized_king_s:10,sized_king_c:10,sized_king_h:10,sized_king_d:10,
    sized_queen_s:10,sized_queen_c:10,sized_queen_h:10,sized_queen_d:10,
    sized_jack_s:10,sized_jack_c:10,sized_jack_h:10,sized_jack_d:10,
    sized_ten_s:10,sized_ten_c:10,sized_ten_h:10,sized_ten_d:10,
    sized_nine_s:9,sized_nine_c:9,sized_nine_h:9,sized_nine_d:9,
    sized_eight_s:8,sized_eight_c:8,sized_eight_h:8,sized_eight_d:8,
    sized_seven_s:7,sized_seven_c:7,sized_seven_h:7,sized_seven_d:7,
    sized_six_s:6,sized_six_c:6,sized_six_h:6,sized_six_d:6,
    sized_five_s:5,sized_five_c:5,sized_five_h:5,sized_five_d:5,
    sized_four_s:4,sized_four_c:4,sized_four_h:4,sized_four_d:4,
    sized_three_s:3,sized_three_c:3,sized_three_h:3,sized_three_d:3,
    sized_two_s:2,sized_two_c:2,sized_two_h:2,sized_two_d:2


    
}