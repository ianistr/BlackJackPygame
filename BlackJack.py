import pygame
import sys
import random
from cards import deck,values



# Initialize Pygame
pygame.init()
pygame.mixer.init()
sound_effect=pygame.mixer.Sound("swosh.mp3")
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height-60))
screen.fill((0, 100, 0)) 
pygame.display.set_caption('BlackJack')
icon=pygame.image.load("icon2.ico")
pygame.display.set_icon(icon)

clock=pygame.time.Clock()
FPS=30

#load back card
back_card=pygame.image.load('cards/back_card.png')
sized_back_card=pygame.transform.scale(back_card,(122,172))


# Rectangle dimensions and position
rect_width = 100
rect_height = 80
rect_x = 1100
rect_y= 400

# Create a Rect object for collision detection Deal
font = pygame.font.Font(None, 48)
rect_deal=pygame.Rect(rect_x, rect_y-100, rect_width, rect_height)
text_deal=font.render("Deal",True,(0,0,0))
text_rect_deal=text_deal.get_rect(center=rect_deal.center)
deal_visible=True


def game(clock,FPS):
    game_over=False
    win=False
    #initial player Values
    player_score=0
    player_cards=[]
    append_distance=300
    dealer_append_distance=300
    entire_deck=deck.copy()
    card1=random.choice(entire_deck)
    entire_deck.remove(card1)
    card2=random.choice(entire_deck)
    entire_deck.remove(card2)
    player_cards.append(values[card1])
    player_cards.append(values[card2])
    player_score=sum(player_cards)

    #Initial Dealer Values
    dealer_score=0
    dealer_cards=[]
    dealer_card_1=random.choice(entire_deck)
    entire_deck.remove(dealer_card_1)
    dealer_card_2=random.choice(entire_deck)
    entire_deck.remove(dealer_card_2)
    dealer_cards.append(values[dealer_card_1])
    dealer_cards.append(values[dealer_card_2])
    dealer_score=dealer_cards[0]

    back_card=pygame.image.load('cards/back_card.png')
    sized_back_card=pygame.transform.scale(back_card,(122,172))




    rect_hit = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
    rect_stand=pygame.Rect(rect_x,rect_y+100, rect_width, rect_height)
    rect_player_score=pygame.Rect(100,300,100,200)

    rect_dealer_score=pygame.Rect(100,200,100,200)

    # Draw text on the rectangle
    font = pygame.font.Font(None, 48)

    winner_text=font.render("Player has Won!",True,(255,255,255))
    looser_text=font.render("Player has Lost!",True,(255,255,255))
    draw_text=font.render("The hand is a Draw!",True,(255,255,255))


    winner_text_rect=winner_text.get_rect()
    looser_text_rect=looser_text.get_rect()
    draw_text_rect=draw_text.get_rect()

    winner_text_rect.center = (screen_width // 2, screen_height // 2)
    looser_text_rect.center = (screen_width // 2, screen_height // 2)
    draw_text_rect.center = (screen_width // 2, screen_height // 2)

    text_hit = font.render('Hit', True, (0,0,0))
    text_stand=font.render('Stand',True,(0,0,0))

    text_player_score=font.render(f'Player score: {player_score}',True,(255,255,255))
    text_dealer_score=font.render(f'Dealer score: {dealer_score}',True,(255,255,255))
    
    text_rect_hit = text_hit.get_rect(center=rect_hit.center)
    text_rect_stand=text_stand.get_rect(center=rect_stand.center)

    text_rect_player_score=text_player_score.get_rect(center=rect_player_score.center)
    text_rect_dealer_score=text_dealer_score.get_rect(center=rect_dealer_score.center)


    #display initial hand
    sound_effect.play()
    screen.blit(card1,(30,450))
    pygame.display.flip()
    pygame.time.wait(450)
    sound_effect.play()
    screen.blit(dealer_card_1,(30,100))
    pygame.display.flip()
    pygame.time.wait(450)
    sound_effect.play()
    screen.blit(card2,(165,450))
    pygame.display.flip()
    pygame.time.wait(450)
    sound_effect.play()
    screen.blit(sized_back_card,(165,100))


    pygame.draw.rect(screen, ((255,255,255)), rect_hit)
    pygame.draw.rect(screen, ((255,255,255)), rect_stand)
    

    screen.blit(text_hit, text_rect_hit)
    screen.blit(text_stand,text_rect_stand)

    screen.blit(text_player_score,text_rect_player_score) 
    screen.blit(text_dealer_score,text_rect_dealer_score) 
    pygame.display.flip()
    while game_over==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                if rect_hit.collidepoint(mouse_x,mouse_y):
                      
                    card=random.choice(entire_deck)
                    player_cards.append(values[card])
                    player_score=sum(player_cards)
                    entire_deck.remove(card)
                    rect_player_score=pygame.Rect(100,300,100,200)
                    text_player_score=font.render(f'Player score: {player_score}',True,(255,255,255))
                    text_rect_player_score=text_player_score.get_rect(center=rect_player_score.center)

                    
                    if 11 in player_cards and player_score>21:
                        player_cards.remove(11)
                        player_cards.append(1)
                        player_score=sum(player_cards)
                        rect_player_score=pygame.Rect(100,300,100,200)
                        text_player_score=font.render(f'Player score: {player_score}',True,(255,255,255))
                        text_rect_player_score=text_player_score.get_rect(center=rect_player_score.center)
                    sound_effect.play()
                    screen.blit(card,(append_distance,450))
                    append_distance+=135
                elif rect_stand.collidepoint(mouse_x,mouse_y):
                     sound_effect.play()
                     resizer=(117,170)
                     sized_back_card=dealer_card_2
                     resized_back_card=pygame.transform.scale(sized_back_card,resizer)
                     dealer_score=sum(dealer_cards)
                     screen.blit(resized_back_card,(165,100))
                     rect_dealer_score=pygame.Rect(100,200,100,200)
                     text_dealer_score=font.render(f'Dealer score: {dealer_score}',True,(255,255,255))
                     text_rect_dealer_score=text_dealer_score.get_rect(center=rect_dealer_score.center)
                     screen.fill((0, 100, 0),text_rect_dealer_score)
                     screen.blit(text_dealer_score,text_rect_dealer_score)
                     pygame.display.flip()
                    



                     
                     while dealer_score<17:
                          
                          pygame.time.wait(1000)
                          dealer_new_card=random.choice(entire_deck)
                          
                          dealer_cards.append(values[dealer_new_card])
                          dealer_score=sum(dealer_cards)
                          entire_deck.remove(dealer_new_card)
                          if 11 in dealer_cards and dealer_score>21:
                            dealer_cards.remove(11)
                            dealer_cards.append(1)
                            dealer_score=sum(dealer_cards)
                            rect_dealer_score=pygame.Rect(100,300,100,200)
                            text_dealer_score=font.render(f'Player score: {dealer_score}',True,(255,255,255))
                            text_rect_dealer_score=text_dealer_score.get_rect(center=rect_dealer_score.center)
                            screen.fill((0, 100, 0),text_rect_dealer_score)
                            screen.blit(text_dealer_score,text_rect_dealer_score)
                            pygame.display.flip()
                          sound_effect.play()
                          screen.blit(dealer_new_card,(dealer_append_distance,100))
                          dealer_append_distance+=135
                          rect_dealer_score=pygame.Rect(100,200,100,200)
                          text_dealer_score=font.render(f'Dealer score: {dealer_score}',True,(255,255,255))
                          text_rect_dealer_score=text_dealer_score.get_rect(center=rect_dealer_score.center)
                          screen.fill((0, 100, 0),text_rect_dealer_score)
                          screen.blit(text_dealer_score,text_rect_dealer_score)
                          pygame.display.flip()
                     if dealer_score>21:
                          screen.blit(winner_text,winner_text_rect)
                          pygame.display.flip()
                          game_over=True
                          #pygame.time.wait(2000)
                     
                     if player_score==dealer_score:
                        screen.blit(draw_text,draw_text_rect)
                        pygame.display.flip()
                        game_over=True
                        #pygame.time.wait(2000)
                     elif player_score>dealer_score:
                          screen.blit(winner_text,winner_text_rect)
                          pygame.display.flip()
                          game_over=True
                          #pygame.time.wait(2000)
                     elif player_score<dealer_score and dealer_score<=21:
                          screen.blit(looser_text,looser_text_rect)
                          pygame.display.flip()
                          game_over=True
                          #pygame.time.wait(2000)
                          
                          
        
                    
                    
                    
        screen.blit(text_hit, text_rect_hit)
        screen.blit(text_stand,text_rect_stand)
        screen.fill((0, 100, 0),text_rect_player_score)
        screen.fill((0, 100, 0),text_rect_dealer_score)
        screen.blit(text_player_score,text_rect_player_score)
        screen.blit(text_dealer_score,text_rect_dealer_score)
        pygame.display.flip()
        
        if 11 in player_cards and player_score>21:
             player_cards.remove(11)
             player_cards.append(1)
             player_score=sum(player_cards)
             rect_player_score=pygame.Rect(100,300,100,200)
             text_player_score=font.render(f'Player score: {player_score}',True,(255,255,255))
             text_rect_player_score=text_player_score.get_rect(center=rect_player_score.center)
             
        elif player_score>21:
                        screen.blit(looser_text,looser_text_rect)
                        pygame.display.flip()
                        game_over=True
                        #pygame.time.wait(2000)
                        
        


        if 11 in dealer_cards and dealer_score>21:
             dealer_cards.remove(11)
             dealer_cards.append(1)
             dealer_score=sum(dealer_cards)
             
        elif dealer_score>21:
              screen.blit(winner_text,winner_text_rect)
              pygame.display.flip()
              game_over=True
              #pygame.time.wait(2000)
        clock.tick(FPS)
    screen.fill((0,100,0),rect_hit)
    screen.fill((0,100,0),rect_stand)
    pygame.display.flip()
    
    
   
# Main loop
running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type==pygame.MOUSEBUTTONDOWN:
             mouse_x, mouse_y = pygame.mouse.get_pos()

             if rect_deal.collidepoint(mouse_x, mouse_y):
                 deal_visible=False
                 pygame.display.flip()
                 screen.fill((0,100,0))
                 game(clock,FPS)
                 #screen.fill((0,100,0))
                 deal_visible=True
                 pygame.display.flip()
                 
                 
                 
                 
    
    
    if deal_visible:
        pygame.draw.rect(screen,((255,255,255)),rect_deal)
        screen.blit(text_deal,text_rect_deal)       
                

    
    pygame.display.flip()
    pygame.time.delay(100)
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()



        


   


    



