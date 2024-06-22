'''要使用pygame库制作一个打砖块（通常称为“Breakout”或“砖块破坏者”）游戏，我们需要创建几个主要的元素：挡板（paddle）、球（ball）、砖块（bricks）以及控制挡板移动的逻辑。以下是一个简单的打砖块游戏的示例代码：

python
'''
import pygame  
import sys  
  
# 初始化pygame  
pygame.init()  
  
# 设置窗口大小  
WINDOW_WIDTH = 800  
WINDOW_HEIGHT = 600  
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  
pygame.display.set_caption('打砖块游戏')  
  
# 设置颜色  
WHITE = (255, 255, 255)  
RED = (255, 0, 0)  
GREEN = (0, 255, 0)  
  
# 加载图片（可选，可以用矩形代替）  
ball_img = pygame.Surface([20, 20])  
ball_img.fill(RED)  
ball_rect = ball_img.get_rect(center=[WINDOW_WIDTH // 2, WINDOW_HEIGHT - 30])  
  
paddle_width = 75  
paddle_height = 15  
paddle_rect = pygame.Rect(WINDOW_WIDTH // 2 - paddle_width // 2, WINDOW_HEIGHT - paddle_height - 10, paddle_width, paddle_height)  
  
# 砖块布局和颜色  
BRICK_WIDTH = 75  
BRICK_HEIGHT = 20  
BRICK_ROW_COUNT = 5  
BRICK_OFFSET_TOP = 30  
BRICK_SPACING = 10  
bricks = []  
for c in range(BRICK_ROW_COUNT):  
    row = []  
    for i in range(BRICK_ROW_COUNT - c):  
        rect = pygame.Rect(i * (BRICK_WIDTH + BRICK_SPACING) + BRICK_SPACING,  
                           BRICK_OFFSET_TOP + c * (BRICK_HEIGHT + BRICK_SPACING),  
                           BRICK_WIDTH, BRICK_HEIGHT)  
        row.append(rect)  
        bricks.append(rect)  
  
# 球的初始速度和方向  
ball_dx = 2  
ball_dy = -2  
  
# 游戏主循环  
running = True  
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  
        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_LEFT:  
                paddle_rect.move_ip(-10, 0)  
            if event.key == pygame.K_RIGHT:  
                paddle_rect.move_ip(10, 0)  
        elif event.type == pygame.KEYUP:  
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  
                paddle_rect.clamp_ip(pygame.Rect(0, WINDOW_HEIGHT - paddle_height - 10, WINDOW_WIDTH, paddle_height))  
  
    # 移动球  
    ball_rect.move_ip(ball_dx, ball_dy)  
  
    # 边界碰撞检测  
    if ball_rect.left < 0 or ball_rect.right > WINDOW_WIDTH:  
        ball_dx = -ball_dx  
    if ball_rect.top < 0:  
        ball_dy = -ball_dy  
  
    # 挡板碰撞检测  
    if ball_rect.colliderect(paddle_rect):  
        ball_dy = -ball_dy  
  
    # 砖块碰撞检测  
    hit_list = []  
    for brick in bricks[:]:  
        if ball_rect.colliderect(brick):  
            hit_list.append(brick)  
            ball_dy = -ball_dy  
            break  
    for brick in hit_list:  
        bricks.remove(brick)  
  
    # 绘制砖块  
    screen.fill(WHITE)  
    for brick in bricks:  
        pygame.draw.rect(screen, GREEN, brick)  
  
    # 绘制挡板  
    pygame.draw.rect(screen, GREEN, paddle_rect)  
  
    # 绘制球  
    screen.blit(ball_img, ball_rect)  
  
    # 更新屏幕显示  
    pygame.display.flip()  
  
    # 控制游戏速度  
    pygame.time.Clock().tick(60)  
  
# 退出pygame
pygame.quit()
