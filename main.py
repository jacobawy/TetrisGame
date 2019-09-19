import sys
import pygame


# 窗口宽度
screen_width = 1200
# 窗口高度
screen_height = 900
# 方块在20x10个单元格组成的游戏区内移动。每个单元格的边长是40个像素。
cell_width = 40
# 一行10个单元格
game_area_width = cell_width * 10
# 一共20行
game_area_height = cell_width * 20
# 游戏区左侧的空白区的宽度/
game_area_left = (screen_width - game_area_width) // 2
# 游戏区顶部的空白区的宽度
game_area_top = screen_height - game_area_height
# 游戏区单元格边界线的颜色
edge_color = (0, 0, 0)
# 单元格填充色
cell_color = (100, 100, 100)
# 窗口背景色
bg_color = (230, 230, 230)


def main():
    # 初始化pygame，在程序开始阶段执行
    pygame.init()
    # 创建屏幕对象（窗口）， 参数表示分辨率时1200*900
    screen = pygame.display.set_mode((screen_width, screen_height))
    # 窗口标题
    pygame.display.set_caption("俄罗斯方块")

    # 游戏主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            # 关闭窗口事件
            if event.type == pygame.QUIT:
                sys.exit()

        # 填充屏幕背景色
        screen.fill(bg_color)

        draw_game_area(screen)
        # 刷新屏幕
        pygame.display.flip()


def draw_game_area(screen):
    "绘制游戏区域"
    # 绘制一条线
    pygame.draw.line(screen, (0, 0, 0), (100, 100), (200, 200))


if __name__ == '__main__':
    main()
