from graphics import Window, Point, Line
from cell import Cell



def main():
    win = Window(800,600)
    point1 = Point(50,100)
    point2 = Point(700,500)
    line1 = Line(point1,point2)
    win.draw_line(line1,"red")
    cell1 = Cell(Point(100,100),Point(200,200),1,1,1,1)
    win.draw_cell(cell1)
    cell2 = Cell(Point(300,300),Point(400,400),0,1,0,1)
    win.draw_cell(cell2)
    win.wait_for_close()


main()
