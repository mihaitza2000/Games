#include<SFML/Graphics.hpp>
#include <iostream>
#include <string>
using namespace sf;
using namespace std;
float Dist(float x1, float y1, float x2, float y2)
{
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}
int main() 
{
    bool start = false;
    float dist = 0, angle = 0, rap = 1;
    float dirX = 0, dirY = 0;
    float ballSpeed = 11, paddleSpeed = 10, playerSpeed = 9;
    float rBall = 10;
    float wPaddle = 140, hPaddle = 25;
    float d;
     
    RenderWindow window(VideoMode(800, 800), "Pong SFML C++", Style::Default);
    RectangleShape paddle(Vector2f(wPaddle, hPaddle));
    RectangleShape player(Vector2f(wPaddle, hPaddle));
    CircleShape ball(rBall,100U);
  
    window.setFramerateLimit(50);
    paddle.setFillColor(Color::Blue);
    paddle.setPosition(400-wPaddle/2, 800-hPaddle);
    ball.setPosition(400-rBall, 800-hPaddle-2*rBall);
    ball.setFillColor(Color::Red);
    player.setFillColor(Color::Blue);
    player.setPosition(400 - wPaddle / 2, 0);

    while (window.isOpen()) {
        if (Keyboard::isKeyPressed(Keyboard::Space) && !start)
        {
            start = true;
        }
        while (start)
        {
            if (Keyboard::isKeyPressed(Keyboard::A))
            {
                if (paddle.getPosition().x > 0)
                {
                    paddle.move(-paddleSpeed, 0);
                }
            }
            else if (Keyboard::isKeyPressed(Keyboard::D))
            {
                if (paddle.getPosition().x < 800 - wPaddle)
                {
                    paddle.move(paddleSpeed, 0);
                }
            }
            ball.move(dirX * ballSpeed, dirY * ballSpeed);
            //hit wall
            if (ball.getPosition().x < 0 || ball.getPosition().x > 800 - 2 * rBall)
            {
                dirX *= -1;
            }
            //get out in player side
            if (ball.getPosition().y <= 0)
            {
                start = false;
                player.setPosition(400 - wPaddle / 2, 0);
                paddle.setPosition(400 - wPaddle / 2, 800 - hPaddle);
                ball.setPosition(400 - rBall, 800 - hPaddle - 2 * rBall);;
                angle = 0;
                dirX = sin(angle);
                dirY = -cos(angle);
            }
            //hit my paddle
            if ((ball.getPosition().x + rBall >= paddle.getPosition().x &&
                  ball.getPosition().x + rBall <= paddle.getPosition().x + wPaddle &&
                  ball.getPosition().y + rBall <= paddle.getPosition().y &&
                  ball.getPosition().y + rBall >= paddle.getPosition().y - rBall) ||
                 (ball.getPosition().y >= paddle.getPosition().y &&
                  ball.getPosition().y + rBall <= 800 - rBall &&
                ((ball.getPosition().x  >= paddle.getPosition().x - 2*rBall && ball.getPosition().x + rBall <= paddle.getPosition().x) ||
                 (ball.getPosition().x >= paddle.getPosition().x + wPaddle && ball.getPosition().x <= paddle.getPosition().x + wPaddle))
                ))
            {
                dist = ball.getPosition().x + rBall - paddle.getPosition().x - wPaddle / 2;
                rap = 2 * dist / wPaddle;
                angle = ( rap * 3.14) / 4;
                dirY = -cos(angle);
                dirX = sin(angle);
            }
            //hit player paddle
            if ((ball.getPosition().x + rBall >= player.getPosition().x &&
                ball.getPosition().x + rBall <= player.getPosition().x + wPaddle &&
                ball.getPosition().y + rBall >= player.getPosition().y + hPaddle &&
                ball.getPosition().y <= player.getPosition().y + hPaddle))
            {
                cout << 1;
            }
            if ((ball.getPosition().x + rBall >= player.getPosition().x &&
                ball.getPosition().x + rBall <= player.getPosition().x + wPaddle &&
                ball.getPosition().y + rBall >= player.getPosition().y+hPaddle &&
                ball.getPosition().y  <= player.getPosition().y+hPaddle ) ||
               (ball.getPosition().y <= player.getPosition().y+hPaddle+rBall &&
                ball.getPosition().y + rBall >= rBall &&
              ((ball.getPosition().x >= player.getPosition().x - 2 * rBall && ball.getPosition().x + rBall <= player.getPosition().x) ||
               (ball.getPosition().x >= player.getPosition().x + wPaddle && ball.getPosition().x <= player.getPosition().x + wPaddle))
                    ))
            {
                dist = ball.getPosition().x + rBall - player.getPosition().x - wPaddle / 2;
                rap = 2 * dist / wPaddle;
                angle = (rap * 3.14) / 4;
                dirY = cos(angle);
                dirX = sin(angle);
            }
            //get out in my side
            if (ball.getPosition().y >= 800)
            {
                start = false;
                player.setPosition(400 - wPaddle / 2, 0);
                paddle.setPosition(400 - wPaddle / 2, 800 - hPaddle);
                ball.setPosition(400 - rBall, 800 - hPaddle-2*rBall);
                angle = 0;
                dirX = sin(angle);
                dirY = -cos(angle);

            }
            //close window
            Event event;
            while (window.pollEvent(event))
            {
                if (event.type == Event::Closed)
                {
                    window.close();
                }
            }
            //automatic control of player
            if (dirY < 0)
            {
                if (ball.getPosition().x <= player.getPosition().x || 
                    ball.getPosition().x >= player.getPosition().x + wPaddle - rBall)
                {
                    if (player.getPosition().x + wPaddle / 2 < ball.getPosition().x + rBall)
                    {
                        player.move(playerSpeed, 0);
                    }
                    else
                    {
                        player.move(-playerSpeed, 0);
                    }
                }
            }
            window.clear();
            window.draw(ball);
            window.draw(paddle);
            window.draw(player);
            window.display();
        }
        window.clear();
        window.draw(ball);
        window.draw(paddle);
        window.draw(player);
        window.display();
    }
    return 0;
}