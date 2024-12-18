import pyxel



class App:
    def __init__(self):
        # Initialize the Pyxel window (width, height)
        pyxel.init(160, 120)

        # Set the initial position of the square
        self.x = 80
        self.y = 60
        self.score = 0

        # Set the initial position and velocity of the sprite
        self.sprite_x = 80
        self.sprite_y = 60
        self.sprite_dx = 2
        self.sprite_dy = 2

        pyxel.load("my_resource.pyxres")


        self.bullets = []
        self.start_screen = True
        self.game_over = False
        
        # Start the game loop
        pyxel.run(self.update, self.draw)






    def update(self):
        if self.start_screen:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.start_screen = False
        elif not self.game_over:
        # Update the square's position based on arrow keys
            if pyxel.btn(pyxel.KEY_UP):
                self.y -= 2
            if pyxel.btn(pyxel.KEY_DOWN):
                self.y += 2
            if pyxel.btn(pyxel.KEY_LEFT):
                self.x -= 2
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.x += 2
            self.x %= 160

        #if pyxel.btnp(pyxel.KEY_LEFT):
            #self.player.move_left()
        #elif pyxel.btnp(pyxel.KEY_RIGHT):
            #self.player.move_right()
        # Simple interaction: Increase score when square reaches top-left corner
            #if self.x <= 10 and self.y <= 10:
                #self.score += 1

        # Update the sprite's position
            self.sprite_x += self.sprite_dx
            self.sprite_y += self.sprite_dy

        #Bounce the sprite off the edges of the screen
            if self.sprite_x <= 0 or self.sprite_x >= 160:
                self.sprite_dx *= -1
            if self.sprite_y <= 0 or self.sprite_y >= 120:
                self.sprite_dy *= -1


            circle_hit_player = False

            if abs(self.x - self.sprite_x ) < 5 and abs(self.y - self.sprite_y < 5):
                if not circle_hit_player:
                    self.score -= 1
                    circle_hit_player = True


            for bullet in self.bullets:
                bullet[0] += bullet[2]
                bullet[1] += bullet[3]
                if bullet[1] < 0 or bullet[1] > 120:
                    self.bullets.remove(bullet)

                if abs(bullet[0] - self.sprite_x) < 10 and abs(bullet[1] - self.sprite_y) < 10:
                    self.score += 1
                    self.bullets.remove(bullet)

            if pyxel.btnp(pyxel.KEY_SPACE):
                self.shoot()

            if self.score >= 20:
                self.game_over = True

            


    def draw(self):
        # Clear the screen with black (color 0)
        pyxel.cls(0)

        if self.start_screen:
            pyxel.text(20, 10, "Shoot the the snow to gain points!", 7)
            pyxel.text(40, 60, "Press Enter to Start", 7)
            pyxel.text(30, 100, "(Press space bar to shoot)", 7)
        elif self.game_over:
            pyxel.text(60, 50, "Game Over", 7)
            pyxel.text(50, 100, "Congradulation!!!", 7)
        else:

            for i in range(50):
            #pyxel.pset(i * 3 % 160, (i * 7 + pyxel.frame_count) % 120, 7)  # White stars
                pyxel.pset(i * 100 % 160, (i * 100 + pyxel.frame_count) % 120, 7)



            pyxel.bltm(0, 0, 0, 0, 7, 145, 130, 0)

        # Draw a square (color 9)
        # pyxel.rect(self.x, self.y, 10, 10, 9)
            pyxel.blt(self.x, 85, 0, 96, 24, 30, 30, 0)

        # Draw the moving sprite (color 11)
            
            pyxel.circ(self.sprite_x, self.sprite_y, 5, 7)

        # Display the score
            pyxel.text(5, 5, f"Score: {self.score}", 7)

        # Display a message when score is high
            if self.score >= 5:
                pyxel.text(50, 50, "You’re doing great!", 8)

            

            for bulle in self.bullets:
                pyxel.pset(bulle[0], bulle[1], 8)

    def shoot(self):
        self.bullets.append([self.x, 100, 0, -5])






# Run the game
App()